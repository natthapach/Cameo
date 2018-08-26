import cv2
import numpy as np

CASCADES_PATH = "./cascades"

class FaceDetector(object) :
  def __init__(self, detectEye=True) :
    self._detectEye = detectEye

  def detect(self, frame) :
    # prepare
    img = np.copy(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detect
    face_cascade = cv2.CascadeClassifier(CASCADES_PATH + "/haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces :
      img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # eye detect
    if self._detectEye :
      eye_cascade = cv2.CascadeClassifier(CASCADES_PATH + "/haarcascade_eye.xml")
      eyes = eye_cascade.detectMultiScale(gray, 1.3, 5, 0, (40, 40))

      for (x, y, w, h) in eyes :
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return img
