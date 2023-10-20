import cv2

# Initialize the webcam (0 represents the default camera, but you can change it to a different camera index if needed)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        break

    # Display the captured frame
    cv2.imshow('Video', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
