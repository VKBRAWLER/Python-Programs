import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
  # Read the frame from the camera
  ret, frame = cap.read()

  # Convert the frame to grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces in the grayscale frame
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  # Draw rectangles around the detected faces
  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

  # Resize the frame to increase the window size
  resized_frame = cv2.resize(frame, (1920, 1080))

  # Display the resulting frame
  cv2.imshow('Multiple Face Detection', resized_frame)

  # Break the loop if 'q' is pressed
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()