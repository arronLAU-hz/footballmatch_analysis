import cv2
import mss
import numpy as np

with mss.mss() as sct:

    monitor = {"top": 100, "left": 100, "width": 800, "height": 600}

    # "top": 100
    # "left": 100
    # "width": 80
    # "height": 600

    while "Screen capturing":
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)


        cv2.imshow("PES 2013 Capture", img)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

