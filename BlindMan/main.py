import cv2
import numpy as np
def iterate(lines):
    for r, theta in lines:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * r
        y0 = b * r
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
    return (x1, y1), (x2, y2)
def turn(t1, t2):
    pass
def slope(t1,t2):
    return (t1[1] - t2[1])/(t1[0] - t2[0])
def show(img):
    im = img[:]
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 300, 400)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 10)
    if lines is None:
        lines = [[]]
    x1, y1 = iterate(lines[0])
    cv2.line(im, x1, y1, (0, 0, 255), 2)
    try:
        for i in range(2):
            x2,y2 = iterate(lines[i])
            cv2.line(im, x2, y2, (0, 0, 255), 2)
    except IndexError:
        pass
    cv2.imshow('Line Detection', im)
    turn((x1,y1),(x2,y2))
cap = cv2.VideoCapture(0)
while True:
    img = cap.read()[1]
    show(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
