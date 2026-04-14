import os
from ultralytics import YOLO
import cv2

image_path = 'images/p.jpg'
OUTPUT_DIR = os.path.join('.', 'validate')
output_image_path = os.path.join(OUTPUT_DIR, 'output.jpg')

# Load an image
oframe = cv2.imread(image_path)
frame = cv2.resize(oframe, (420,640  ))
H, W, _ = frame.shape

model_path ='pan_best.pt'

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

# Perform inference on the image
results = model(frame)[0]

# List to track detected classes
detected_classes = []
print(results.boxes.data.tolist())
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    if score > threshold:
        detected_classes.append(results.names[int(class_id)])
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
        cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        # Print information for each detected box
        print("Detected:", results.names[int(class_id)], " with confidence:", score)

# Save the output image
cv2.imwrite(output_image_path, frame)

# Specify the classes to check for detection
specified_classes = ['Photo', 'Header', 'PI', 'Emblem']

# Check if all specified classes are detected
missing_classes = [cls for cls in specified_classes if cls not in detected_classes]

if not missing_classes:
    print("Verified: All specified classes are detected.")
else:
    print("Not Verified: Some specified classes are not detected.")
    print("Missing classes:", missing_classes)