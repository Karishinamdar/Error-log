import cv2
import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GLib
 
# Initialize GStreamer
Gst.init(None)

def display_camera(camera_id):
    pipeline = Gst.Pipeline.new("video-display")

    # create element
    source = Gst.ElementFactory.make("qtiqmmfsrc", "qmmf-source")
    framefilter = Gst.ElementFactory.make("capsfilter", "frame-filter")
    sink = Gst.ElementFactory.make("waylandsink", "display")

    if not pipeline or not source or not framefilter or not sink:
        print("Create element failed")
        return

    source.set_property("camera", camera_id)

    # Modify the properties for framefilter
    if camera_id == 0:
        framefilter.set_property("caps",
                                 Gst.caps_from_string("video/x-raw,format=NV12,framerate=30/1,width=1920,height=1080"))
    else:
        framefilter.set_property("caps",
                                 Gst.caps_from_string("video/x-raw,format=NV12,framerate=15/1,width=1280,height=720"))

    # Modify the properties for sink
    sink.set_property("x", 200)
    sink.set_property("y", 200)
    sink.set_property("width", 1280)
    sink.set_property("height", 720)

    # Build the pipeline
    pipeline.add(source)
    pipeline.add(framefilter)
    pipeline.add(sink)

    if not source.link(framefilter):
        print("ERROR: Could not link source to framefilter")
        return
    if not framefilter.link(sink):
        print("ERROR: Could not link framefilter to sink")
        return

    # Start playing
    pipeline.set_state(Gst.State.PLAYING)
    print("Started Liveview for camera %d" % camera_id)

    return pipeline
# Start display pipelines for the cameras
camera_id1 = 2
pipeline_str = display_camera(camera_id1)

camera_id2 = 1
pipeline_str2 = display_camera(camera_id2)

# Open video capture for recording
#cap1 = cv2.VideoCapture(pipeline_str, cv2.CAP_GSTREAMER)
#cap2 = cv2.VideoCapture(pipeline_str2, cv2.CAP_GSTREAMER)

#cap1 = cv2.VideoCapture(1)
#cap2 = cv2.VideoCapture(2)

cap1 = cv2.VideoCapture(display_camera(1))
cap2 = cv2.VideoCapture(display_camera(2))

# Check if the video capture objects were successfully opened
if not cap1.isOpened() or not cap2.isOpened():
    print("Failed to open cameras for recording")
    exit()

num = 0

while True:
    success1, img1 = cap1.read()
    success2, img2 = cap2.read()

    if not success1 or not success2:
        print("Failed to read from cameras")
        break

    k = cv2.waitKey(5)
 
    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('images/stereoLeft/imageL' + str(num) + '.png', img1)
        cv2.imwrite('images/stereoright/imageR' + str(num) + '.png', img2)
        print("images saved!")
        num += 1

    cv2.imshow('Camera 1', img1)
    cv2.imshow('Camera 2', img2)

    # Check for keyboard input
    if cv2.waitKey(1) == 27:
        break

# Stop and cleanup the pipelines
pipeline_str.set_state(Gst.State.NULL)
pipeline_str2.set_state(Gst.State.NULL)

# Release and destroy all windows before termination
cap1.release()
cap2.release()
cv2.destroyAllWindows()
