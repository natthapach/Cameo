import cv2
from managers.capture import CaptureManager
from managers.window import WindowManager

class Cameo(object) :
  def __init__(self) :
    cap0 = cv2.VideoCapture(0)
    self._windowManager = WindowManager('Cameo',
                                        self.onKeypress)
    self._captureManager = CaptureManager(cap0,
                                          self._windowManager,
                                          True)

  def run(self) :
    self._windowManager.createWindow()
    while self._windowManager.isWindowCreated :
      self._captureManager.enterFrame()
      # filter
      frame = self._captureManager.frame

      # display
      self._windowManager.show(frame)

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
      self._windowManager.destroyWindow()
  
if __name__ == '__main__' :
  Cameo().run()