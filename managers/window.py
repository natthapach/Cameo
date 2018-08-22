import cv2
import numpy as np
import time

class WindowManager(object) :
  def __init__(self, 
              shouldMirrorPreview=False,
              keypressCallback=None) :
    self.shouldMirrorPreview = shouldMirrorPreview
    self.keypressCallback = keypressCallback
    self._isWindowsCreated = False
  
  @property
  def isWindowsCreated(self) :
    return self._isWindowsCreated

  def createWindow(self, windowName) :
    cv2.namedWindow(windowName)
    self._isWindowsCreated = True
  
  def show(self, windowName, frame) :
    if self.shouldMirrorPreview:
        mirroredFrame = np.fliplr(frame).copy()
        cv2.imshow(windowName, mirroredFrame)
    else :
      cv2.imshow(windowName, frame)
  
  def destroyWindows(self) :
    cv2.destroyAllWindows()
    self._isWindowsCreated = False

  def processEvents(self) :
    keycode = cv2.waitKey(1)
    if self.keypressCallback is not None and keycode != -1 :
      keycode &= 0xFF
      self.keypressCallback(keycode)
      