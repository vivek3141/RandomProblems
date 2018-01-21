import cv2
import run
cap = cv2.VideoCapture(0)
while True:
    screen = cap.read()[1]
    screen = cv2.resize(screen, (800, 600))
    x,data1,data2 = run.run(screen)
    cv2.imshow("Test", x)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

