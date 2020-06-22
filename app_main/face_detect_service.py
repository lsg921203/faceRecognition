import copy
import os
import cv2
import numpy as np

class FaceDetectService:
    def __init__(self, src):
        self.classifiers = []
        self.src = src
        self.img = None
        self.gray = None
        self.res = None
        self.dataset_path = "dataset/"
        self.trainer = "trainer.yml"

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
    def eye_detect(self):
        flag = self.face_detect()
        if not flag:
            print("no face")
            return False

        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_eye.xml'))

        img = copy.deepcopy(self.img)
        roi_gray = []
        roi_color = []
        for (x, y, w, h) in self.face:
            roi_gray = self.gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        eyes = self.classifiers[1].detectMultiScale(roi_gray,
                                                    scaleFactor=1.3,
                                                    minNeighbors=5,
                                                    minSize=(5,5))
        for (x1, y1, w1, h1) in eyes:
            cv2.rectangle(roi_color, (x1,y1), (x1+w1,y1+h1),(0,255,0),2)
            #img[y:y+h, x:x+w] = roi_color
        self.res = img

        return True

    def smile_detect(self):
        flag = self.face_detect()
        if not flag:
            print("no face")
            return False

        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_smile.xml'))

        img = copy.deepcopy(self.img)
        roi_gray = []
        roi_color = []
        for (x, y, w, h) in self.face:
            roi_gray = self.gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        smile = self.classifiers[1].detectMultiScale(roi_gray,
                                                    scaleFactor=1.7,
                                                    minNeighbors=5,
                                                    minSize=(5, 5))
        for (x1, y1, w1, h1) in smile:
            cv2.rectangle(roi_color, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

        self.res = img

        return True

    def face_recog_train(self):
        dirs = os.listdir(self.dataset_path)# dataset 하위 디렉토리이름을 리스트에 저장
        persons = []
        for dir in dirs:#각 디렉토리에 저장된 파일명들을 persons에 담음음
            if os.path.isdir(self.dataset_path+dir):
                persons.append(os.listdir(self.dataset_path+dir))
        print(len(self.classifiers))
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))
        print(len(self.classifiers))

        #

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        samples = []
        ids = []

        for id, row in enumerate(persons):
            #print("row: ",row)
            for p in row:
                #print("p:",p)
                img = cv2.imread(self.dataset_path+dirs[id]+'/'+p)


                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #cv2.imshow("img", gray)
                #cv2.waitKey(0)
                face = self.classifiers[0].detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(20, 20)
                )
                print(len(face))
                #cv2.waitKey(0)
                for (x, y, w, h) in face:
                    #print("1")
                    samples.append(gray[y:y+h,x:x+w])
                    ids.append(id)

        recognizer.train(samples, np.array(ids))
        recognizer.write(self.dataset_path+self.trainer)
        print("얼굴 학습 완료")

    def face_recog(self):
        self.classifiers.clear()
        self.classifiers.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.dataset_path+self.trainer)

        names = ["하연수","수지"]
        self.img = cv2.imread(self.src)
        #cv2.imshow("image",self.img)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        face = self.classifiers[0].detectMultiScale(
                    self.gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(20, 20)
                )
        res = False
        name = 'no face'
        for (x, y, w, h) in face:
            id, confi = recognizer.predict(self.gray[y:y+h,x:x+w])
            if confi < 100:
                name = names[id]
                print( name, "/ confidence:",confi)
                res = True
            else:
                name = 'unknown'
                res = False

        return  res, name

