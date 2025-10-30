import cv2
from pyzbar.pyzbar import decode
import subprocess
import time

def read_qr_code():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    print("📸 Scanning for QR code... Show QR A to start animation")
    found = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        decoded_objs = decode(frame)
        for obj in decoded_objs:
            qr_data = obj.data.decode("utf-8")
            print(f"✅ QR Code: {qr_data}")

            if qr_data.strip().upper() == "A":
                print("🚀 Starting shortest path animation for A → G...")
                found = True
                break

        cv2.imshow("QR Scanner", frame)
        if found or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if found:
        # Run the Manim animation for A -> G path
        subprocess.run([
            "manim",
            "-pql",  # quick low-quality preview (use -pqh for higher quality)
            "multi_robot_path.py",
            "MultipleRobotPaths"
        ])

if __name__ == "__main__":
    read_qr_code()
