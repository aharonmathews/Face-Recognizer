import cv2

# Path to your image file
image_path = 'dataset/Aarsha.jpg'

# Load the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained HOG face detector
    hog_face_detector = cv2.HOGDescriptor()
    hog_face_detector.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Detect faces in the image
    faces, _ = hog_face_detector.detectMultiScale(gray)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Face Recognition (HOG)', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
