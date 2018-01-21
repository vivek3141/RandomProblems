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
    L1 = list(t1)
    L2 = list(t2)
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
def slope(P1, P2):
    try:
        return(P2[1] - P1[1]) / (P2[0] - P1[0])
    except ZeroDivisionError:
        return False
def y_intercept(P1, slope):
    return P1[1] - slope * P1[0]
def turn(m1, b1, m2, b2):
    if m1 == m2:
        return False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    if(b1+b2)/2 > y:
        return "Turn Right"
    return "Turn Left"
def show(img, X):
    im = img[:]
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 300, 400)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 10)
    if lines is None:
        return False
    c11, c12 = iterate(lines[0])
    cv2.line(im, c11, c12, (0, 0, 255), 2)
    c21 = None
    try:
        for k in range(5):
            c21, c22 = iterate(lines[k])
            cv2.line(im, c21, c22, (0, 0, 255), 2)
    except IndexError:
        pass
    cv2.imshow('Line Detection', im)
    if not(c21 is None):
        A1 = c11
        A2 = c12
        B1 = c21
        B2 = c22
        slope_A = slope(A1, A2)
        slope_B = slope(B1, B2)
        if not(slope_A) or not(slope_B):
            return False
        y_int_A = y_intercept(A1, slope_A)
        y_int_B = y_intercept(B1, slope_B)
        X1 = turn(slope_A, y_int_A, slope_B, y_int_B)
        if not(X1 == X):
            return X1
cap = cv2.VideoCapture(0)
X = ""
while True:
    img = cap.read()[1]
    X1 = show(img, X)
    if not((X is False) or (X is None)):
        X = X1
        print(X)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
