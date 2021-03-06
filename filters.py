import cv2
import numpy as np

class ConvolutionFilter(object) :
  def __init__(self, kernel) :
    self._kernel = kernel

  def apply(self, src) :
    return cv2.filter2D(src, -1, self._kernel)

class SharpenFilter(ConvolutionFilter) :
  def __init__(self) :
    kernel = np.array([
                        [-1, -1, -1],
                        [-1,  9, -1],
                        [-1, -1, -1]
                      ])
    ConvolutionFilter.__init__(self, kernel)

class FindEdgesFilter(ConvolutionFilter) :
  def __init__(self) :
    kernel = np.array([
                        [-1, -1, -1],
                        [-1,  8, -1],
                        [-1, -1, -1],
                      ])
    ConvolutionFilter.__init__(self, kernel)

class EmbossFilter(ConvolutionFilter) :
  def __init__(self) :
    kernel = np.array([
      [-2, -1, 0],
      [-1,  1, 1],
      [ 0,  1, 2]
    ])
    ConvolutionFilter.__init__(self, kernel)
    
class CannyFilter(object) :
  def __init__(self,
              min_threshold=100,
              max_threshold=200):
    self.min_threshold = min_threshold
    self.max_threshold = max_threshold

  def apply(self, src) :
    return cv2.Canny(src, self.min_threshold, self.max_threshold)