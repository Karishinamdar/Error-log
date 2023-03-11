###  1.Error-log for StereoCamera_display.py :

When using below lines in the code:   
cap1 = cv2.VideoCapture(display_camera(1))   
cap2 = cv2.VideoCapture(display_camera(2))   


Output on the screen: (One Video plays on the weston display from camera 1 only)   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 2
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   


When using below lines in the code:   
cap1 = cv2.VideoCapture(1)   
cap2 = cv2.VideoCapture(2)   

Output on the screen:   
gbm_create_device(156): Info: backend name is: msm_drm    
Started Liveview for camera 2   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   
Unable to stop the stream: Inappropriate ioctl for device   
VIDEOIO ERROR: V4L: index 2 is not correct!   
Failed to open cameras for recording   

###   2.Error-log for direct_Gstpipeline.py:

There is no ouput to this. Code runs smoothly without errors but doesn't show anything. 

###   3.Error-log for tcp_architecture.py:

Code runs for one camera at a time and saves images, but doesn't allow to acess both cameras at the same time. 

###   4.Error-log for gstpipeline_test.py (Video plays from camera 2 only, and no other error shows)

output on the screen:    
gbm_create_device(156): Info: backend name is: msm_drm   
gbm_create_device(156): Info: backend name is: msm_drm   




