import config
import time
def locate_ball():
	headMov = config.loadProxy("ALMotion")
	i = 0
	a = [-1.5,0,1.5]
	b = [2.0,4.0,6.0]
	isAbsolute = True
	headMov.stiffnessInterpolation("HeadYaw", 1.0, 1.0)
	targetName = "RedBall"
	diameter = 0.08
	distanceX = 0.08
	distanceY = 0.0
	angleWz = 0.0
	thresholdX = 0.1
	thresholdY = 0.1
	thresholdWz = 1.0
	effector = "None"
	mode = "Move"
	tracker = config.loadProxy( "ALTracker" )
	tracker.setEffector(effector)
	tracker.registerTarget(targetName, diameter)
	tracker.setRelativePosition([-distanceX, distanceY, angleWz, thresholdX, thresholdY, thresholdWz])
	tracker.setMode(mode)
	t_end = time.time() + 30
	tracker.track(targetName) 
	for i in range(3):
		headMov.angleInterpolation("HeadYaw", a[i], b[i], isAbsolute)
		i+=1
		if tracker.isTargetLost():
			continue
		else:
			break
	headMov.angleInterpolation("HeadYaw", 0, 8.0, isAbsolute)
		
	if time.time() == t_end:
		tracker.stopTracker()
	tracker.unregisterTarget(targetName)
	headMov.stiffnessInterpolation("HeadYaw", 0.0, 1.0)
