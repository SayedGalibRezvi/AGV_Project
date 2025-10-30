import cv2
from pyzbar.pyzbar import decode

# ✅ Your DroidCam WiFi IP (confirmed)
url = "http://192.168.178.24:4747/video"

cap = cv2.VideoCapture(url)
print("🎥 Connected to DroidCam stream — scanning for QR codes. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No frame received, check WiFi connection.")
        continue

    # Convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect QR codes
    codes = decode(gray)

    for code in codes:
        data = code.data.decode('utf-8')
        (x, y, w, h) = code.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        print(f"✅ Detected: {data}")

    cv2.imshow("QR Code Scanner", frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
