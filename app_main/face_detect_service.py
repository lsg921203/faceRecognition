import copy

import cv2

class FaceDetectService:
    def __init__(self, src):
        self.classifiers = []
        self.src = src
        self.img = None
        self.gray = None
        self.res = None

    def face_detect(self):
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        self.img = cv2.imread(self.src)
        # 이미지를 흑백처리
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        self.face = self.classifiers[0].detectMultiScale(
            self.gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        img = copy.deepcopy(self.img)

        for (x, y, w, h) in self.face:

            cv2.rectangle(img, (x,y), (x+w,y+h),(0, 0, 255), 4)

        self.res = img

        if len(self.face) == 0:
            print('no face')
            return False
        return True
