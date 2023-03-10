# Error-log for StereoCamera_display.py :

When using below lines in the code:   
cap1 = cv2.VideoCapture(display_camera(1))   
cap2 = cv2.VideoCapture(display_camera(2))   


Output: (One Video plays on the weston display from camera 1 only)   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 2
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   


When using below lines in the code:   
cap1 = cv2.VideoCapture(1)   
cap2 = cv2.VideoCapture(2)   


Output:   

gbm_create_device(156): Info: backend name is: msm_drm    
Started Liveview for camera 2   
gbm_create_device(156): Info: backend name is: msm_drm   
Started Liveview for camera 1   
Unable to stop the stream: Inappropriate ioctl for device   
VIDEOIO ERROR: V4L: index 2 is not correct!   
Failed to open cameras for recording   

