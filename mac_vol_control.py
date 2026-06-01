# Step 1: Importing required modules
import cv2
import numpy as np
import mediapipe as mp
import math
import subprocess

# Function to set the system volume using osascript
def set_system_volume(volume):
    script = f"set volume output volume {volume}"
    subprocess.run(["osascript", "-e", script])

mpDraw = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands = mpHands.Hands()

cap = cv2.VideoCapture(0)

vol = 0

while True:
    # Step 2: Capturing hand gestures
    success, img = cap.read()
    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lmList = []
            for Id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([Id, cx, cy])

            if lmList:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]

                # Step 3(a): Measuring distance between 2 fingers
                length = math.hypot(x2-x1, y2-y1)

                cv2.circle(img, (x1,y1), 15, (0,123,12), cv2.FILLED)
                cv2.circle(img, (x2,y2), 15, (0,123,12), cv2.FILLED)
                cv2.line(img, (x1,y1), (x2,y2), (0,12,123), 2)

                z1 = (x1+x2)//2
                z2 = (y1+y2)//2

                if length < 50:
                    cv2.circle(img, (z1,z2), 15, (255, 0, 0), cv2.FILLED)

                # Step 3(b): Mapping distance to volume
                vol = np.interp(length, [50, 300], [0, 100])
                vol = int(min(max(vol, 0), 100))

                # Step 4: Adjusting the system volume
                set_system_volume(vol)

    # Step 5: Drawing volume bar on video
    cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 255), 3)
    filled_height = int(np.interp(vol, [0, 100], [0, 250]))
    cv2.rectangle(img, (52, 400 - filled_height), (83, 400), (0, 255, 0), cv2.FILLED)
    cv2.imshow("Hand Gesture Volume Control", img)

    # Step 6: Check for key press to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()