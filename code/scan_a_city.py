import cv2
from pyzbar.pyzbar import decode
import subprocess
import os

# --- Manim project settings ---
MANIM_PROJECT_DIR = r"G:/AGV_Project"
MANIM_FILE = "multi_algorithm_city_animation.py"
MANIM_SCENE = "MultiRobotPaths"   # must match the class name in the Manim file


def run_animation():
    """Call Manim to render and play the newest city animation."""
    cmd = [
        "manim",
        "-pqh",             # preview, high quality
        "-r", "1920,1080",  # resolution: 1080p
        "--fps", "60",      # 60 frames per second
        MANIM_FILE,
        MANIM_SCENE,
    ]

    # run manim from the project directory so relative paths work
    subprocess.run(cmd, cwd=MANIM_PROJECT_DIR)


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
                print("🚀 Starting city-style animation for A → G using updated graph...")
                found = True
                break

        cv2.imshow("QR Scanner", frame)

        # press 'q' to quit or stop after A is found
        if found or cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if found:
        run_animation()


if __name__ == "__main__":
    read_qr_code()
