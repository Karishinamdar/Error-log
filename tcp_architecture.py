# import the opencv library
import cv2

# define a video capture object
cap = cv2.VideoCapture("tcp://10.0.0.184:5037/video?x=1")

while(cap.isOpened()):

        # Capture the video frame
        # by frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imwrite("tcp7.jpg", frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
