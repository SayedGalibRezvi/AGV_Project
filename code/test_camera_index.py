import cv2

cap = cv2.VideoCapture("http://192.168.x.x:4747/video")
while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No frame!")
        continue

    cv2.imshow("Camera Feed", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
