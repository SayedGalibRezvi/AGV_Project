# qr_localization.py
import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

print("🔍 Looking for QR codes... Press 'q' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        print("Camera error!")
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None:
        # Draw the bounding box
        for i in range(len(bbox)):
            pt1 = tuple(bbox[i][0])
            pt2 = tuple(bbox[(i + 1) % len(bbox)][0])
            cv2.line(frame, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])), (0, 255, 0), 2)

        if data:
            print(f"✅ Detected QR code: {data}")
            cv2.putText(frame, data, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("QR Localization (Press q to exit)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
