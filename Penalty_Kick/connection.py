import config
print "Creating motion proxy" 
try:
  motion = config.loadProxy("ALMotion")
  config.StiffnessOn(motion)
  config.PoseInit(motion)
except Exception,e:
  print "Error when creating motion proxy:"
  print str(e)
  exit(1)
print "Creating ALVideoDevice proxy"
try:
  cam = config.loadProxy("ALVideoDevice")
except Exception,e:
  print "Error when creating vision proxy:"
  print str(e)
  exit(1)








