import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, GLib

import numpy as np
import cv2

# Initialize GStreamer and GObject
GObject.threads_init()
Gst.init(None)

# Define the pipelines
pipeline_str1 = "qtiqmmfsrc camera=1 ! video/x-raw, format=NV12, width=1280, height=720, framerate=15/1 ! videoconvert ! waylandsink"
pipeline_str2 = "qtiqmmfsrc camera=2 ! video/x-raw, format=NV12, width=1280, height=720, framerate=15/1 ! videoconvert ! waylandsink"

# Create the pipelines
pipeline1 = Gst.parse_launch(pipeline_str1)
pipeline2 = Gst.parse_launch(pipeline_str2)

# Start the pipelines
pipeline1.set_state(Gst.State.PLAYING)
pipeline2.set_state(Gst.State.PLAYING)

# Main loop
while True:
    # Handle key events
    k = cv2.waitKey(5)
    if k == 27:
        break
    elif k == ord("s"):
        # Save the frames to disk
        # Get the current frame from each pipeline
        success1, img1 = pipeline1.get_by_name("waylandsink0").get_current_frame()
        success2, img2 = pipeline2.get_by_name("waylandsink0").get_current_frame()
        if success1 and success2:
            cv2.imwrite("images/stereoLeft/imageL" + str(num) + ".png", img1)
            cv2.imwrite("images/stereoright/imageR" + str(num) + ".png", img2)
            print("Images saved!")
            num += 1

# Stop the pipelines
pipeline1.set_state(Gst.State.NULL)
pipeline2.set_state(Gst.State.NULL)
