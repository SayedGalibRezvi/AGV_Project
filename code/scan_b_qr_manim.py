import cv2
from pyzbar.pyzbar import decode
import subprocess
import os
import time

def read_qr_code():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    print("📸 Scanning for QR code... Show QR B to play B → F animation")
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

            if qr_data.strip().upper() == "B":
                print("🎬 Playing path animation for B → F...")
                found = True
                break

        cv2.imshow("QR Scanner (B)", frame)
        if found or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if found:
        video_path = r"G:\AGV_Project\assets\media\videos\robot_path_B_to_F\2160p60\BtoFPath.mp4"
        # Method 1: Use VLC or default media player
        subprocess.run(["start", "", video_path], shell=True)  # for Windows
        # If VLC is installed, you can use this instead:
        # subprocess.run(["C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", video_path])

if __name__ == "__main__":
    read_qr_code()
