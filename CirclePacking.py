import numpy as np
import cv2
from Circle import Circle


def updateCircle(circle, circles, max_size=-1):
    if circle.radius > max_size > 0:
        circle.grow = False

    else:
        for other in circles:
            if circle != other:
                if circle.intersectingOther(other):
                    circle.grow = False
                    other.grow = False
                    break

        circle.growCircle(1)

def updateCircles(circles, max_size=-1):
    for circle in circles:
        if circle.grow:
            updateCircle(circle, circles, max_size)


def getRndNewCircle(height, width, circles, min_size=2):
    while True:
        circle_found = True
        pos = np.array([np.random.randint(0, width), np.random.randint(0, height)])

        newCircle = Circle(pos, min_size)

        for circle in circles:
            if newCircle.intersectingOther(circle):
                circle_found = False
                break

        if circle_found:
            break

    return newCircle


def circlePacking(height, width, max_iter=1000, min_size=2, max_size=-1, growthUpdatePerLoop=1, newCirclePerLoop=1):

    circles = []

    for i in range(max_iter):
        for j in range(newCirclePerLoop):
            circles.append(getRndNewCircle(height, width, circles, min_size))

        for j in range(growthUpdatePerLoop):
            updateCircles(circles, max_size)

    return circles

def showCircles(height, width, circles):
    img = np.zeros((height, width, 3))
    for circle in circles:
        cv2.circle(img, (circle.pos[0], circle.pos[1]), circle.radius, (255, 255, 255), 1)

    return img


def showCirclePacking(height, width, max_iter=1000, min_size=2, max_size=-1, growthUpdatePerLoop=1, newCirclePerLoop=1):
    circles = []

    for i in range(max_iter):
        for j in range(newCirclePerLoop):
            circles.append(getRndNewCircle(height, width, circles, min_size))

        for j in range(growthUpdatePerLoop):
            updateCircles(circles, max_size)

        img = showCircles(height, width, circles)
        cv2.imshow("", img)
        cv2.waitKey(1)

    cv2.waitKey(0)


def findAvgColorinCircle(img, pos, radius):
    color = np.zeros(3)
    if np.all(pos - radius > 0) and np.all(pos + radius < np.asarray(img.shape[:2])):
        for i in range(3):
            color[i] = np.average(img[pos[1] - radius: pos[1] + radius, pos[0] - radius: pos[0] + radius, i])
    else:
        color = img[pos[1], pos[0]]

    return color.astype(int)


def circlePackingFromImg(img_arr, max_iter=1000, min_size=2, max_size=-1, growthUpdatePerLoop=1, newCirclePerLoop=1):
    circles = []

    for i in range(max_iter):

        for j in range(newCirclePerLoop):
            circles.append(getRndNewCircle(img_arr.shape[0], img_arr.shape[1], circles, min_size))

        for j in range(growthUpdatePerLoop):
            updateCircles(circles, max_size)

        img = np.zeros((img_arr.shape[0], img_arr.shape[1], 3))
        for circle in circles:
            color = findAvgColorinCircle(img_arr, circle.pos, circle.radius)
            cv2.circle(img, (circle.pos[0], circle.pos[1]), int(circle.radius), [int(color[0]), int(color[1]), int(color[2])], -1)
            cv2.circle(img, (circle.pos[0], circle.pos[1]), int(circle.radius), (255, 255, 255), 1)

        cv2.imshow("", img.astype(np.uint8))
        cv2.waitKey(1)
    cv2.waitKey(0)

