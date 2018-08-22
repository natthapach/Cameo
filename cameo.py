import cv2
from managers.capture import CaptureManager
from managers.window import WindowManager
import filters

class Cameo(object) :
  def __init__(self) :
    cap0 = cv2.VideoCapture(0)
    self._windowManager = WindowManager(True, self.onKeypress)
    self._captureManager = CaptureManager(cap0)
    self._isRun = False

  def run(self) :
    self._isRun = True
    sharpenFilter = filters.SharpenFilter()
    findEdgesFilter = filters.FindEdgesFilter()

    while self._isRun :
      self._captureManager.enterFrame()
      # filter
      frame = self._captureManager.frame
      sharpen = sharpenFilter.apply(frame)
      findEdges = findEdgesFilter.apply(frame)

      # display
      self._windowManager.show("origin", frame)
      self._windowManager.show("sharpen", sharpen)
      self._windowManager.show("find edges", findEdges)

      self._captureManager.exitFrame()
      
      self._windowManager.processEvents()

  def onKeypress(self, keycode) :
    if keycode == 32 :  # space
      self._captureManager.writeImage('screenshot.png')
    elif keycode ==9 : # tab
      if not self._captureManager.isWritingVideo :
        self._captureManager.startWritingVideo('screencast.avi')
      else :
        self._captureManager.stopWritingVideo()
    elif keycode == 27 : # esc
      self._windowManager.destroyWindows()
      self._isRun = False
  
  # def _windowProcess(self) :
    
if __name__ == '__main__' :
  Cameo().run()