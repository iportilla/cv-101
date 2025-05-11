# Real-time webcam capture with OpenCV
# Note: On Mac, you may need to grant camera permissions to VS Code/Terminal

import cv2
import numpy as np

def webcam_capture():
    # Create VideoCapture object
    # 0 represents default camera (usually built-in webcam)
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        print("On Mac, try running from terminal with proper permissions.")
        return
    
    print("Webcam activated. Press 'q' to quit, 's' to save a screenshot.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
        
        # Display the frame using cv2.imshow (works in terminal applications)
        cv2.imshow('Webcam Feed (press q to quit)', frame)
        
        # Wait for key press (1ms)
        key = cv2.waitKey(1) & 0xFF
        
        # If 'q' is pressed, break the loop
        if key == ord('q'):
            print("Exiting webcam feed.")
            break
        # If 's' is pressed, save the current frame
        elif key == ord('s'):
            cv2.imwrite('webcam_screenshot.jpg', frame)
            print("Screenshot saved as 'webcam_screenshot.jpg'")
    
    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the webcam capture function
webcam_capture()