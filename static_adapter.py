import cv2
import numpy as np

class ImageStaticAdapter(object) :
  def __init__(self, filename) :
    self._filename = filename
    self._image = cv2.imread(filename, cv2.IMREAD_COLOR)

  def grab(self) :
    return True

  def retrieve(self) :
    return (True, self._image)