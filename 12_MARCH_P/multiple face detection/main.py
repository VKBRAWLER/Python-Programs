import cv2
import dlib

# Create a face detector
face_detector = dlib.get_frontal_face_detector()

# Open the video capture device (webcam)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_detector(gray_frame)

    # Loop through each face found in the frame
    for face in faces:
        # Get the coordinates of the face
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame with detected faces
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
video_capture.release()
cv2.destroyAllWindows()
