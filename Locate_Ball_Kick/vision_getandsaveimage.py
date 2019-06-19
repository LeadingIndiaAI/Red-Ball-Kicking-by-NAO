import time
from PIL import Image
import config
from naoqi import ALProxy
def showNaoImage(IP, PORT,camera_id):
  camProxy = config.loadProxy("ALVideoDevice")
  camProxy.kCameraSelectID=18
  print camProxy.getParam(camProxy.kCameraSelectID)
  camProxy.setParam(camProxy.kCameraSelectID,camera_id)
  resolution =  1   # VGA
  colorSpace = 11   # RGB
  videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)
  naoImage = []
  naoImage = camProxy.getImageRemote(videoClient)
  camProxy.unsubscribe(videoClient)
  print (naoImage)
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  array = naoImage[6]
  im = Image.frombytes("RGB", (imageWidth, imageHeight), array)
  im.save("camImage.png", "PNG")
  im.show()
if __name__ == '__main__':
  IP = "192.168.43.11"  # Replace here with your NaoQi's IP address.
  PORT = 9559
  showNaoImage(IP, PORT)


