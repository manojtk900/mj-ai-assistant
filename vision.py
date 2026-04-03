import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect_objects():

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        if not ret:
            break

        bbox, label, conf = cv.detect_common_objects(frame)

        output = draw_bbox(frame, bbox, label, conf)

        cv2.imshow("MJ Vision", output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    return label
    