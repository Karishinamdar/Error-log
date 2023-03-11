import cv2

pipeline_str = "qtiqmmfsrc camera=%d ! video/x-raw, format=NV12, width=1280, height=720, framerate=15/1 ! videoconvert ! waylandsink"
cap1 = cv2.VideoCapture(pipeline_str, cv2.CAP_GSTREAMER)

pipeline_str2 = "qtiqmmfsrc camera=2 ! video/x-raw, format=NV12, width=1280, height=720, framerate=15/1 ! videoconvert ! waylandsink"
cap2 = cv2.VideoCapture(pipeline_str2, cv2.CAP_GSTREAMER)

while True:
    ret, frame = cap1.read()  # read a frame from the video stream

    if not ret:
        break  # if the frame was not read successfully, break out of the loop

    cv2.imshow("Camera 1", frame)  # display the frame on a window named "Camera 1"

    if cv2.waitKey(1) == ord('q'):  # exit the loop if 'q' is pressed
        break

while True:
    ret, frame = cap2.read()  # read a frame from the video stream

    if not ret:
        break  # if the frame was not read successfully, break out of the loop

    cv2.imshow("Camera 2", frame)  # display the frame on a window named "Camera 2"

    if cv2.waitKey(1) == ord('q'):  # exit the loop if 'q' is pressed
        break

cap1.release()  # release the video capture object for camera 1
cap2.release()  # release the video capture object for camera 2
cv2.destroyAllWindows()  # close all windows
