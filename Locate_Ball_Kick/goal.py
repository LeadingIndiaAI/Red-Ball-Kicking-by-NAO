import config
import time
def locate_goal():
	headMov = config.loadProxy("ALMotion")
	i = 0
	a = [-1.5,0,1.5]
	b = [2.0,4.0,6.0]
	isAbsolute = True
	headMov.stiffnessInterpolation("HeadYaw", 1.0, 1.0)
        targetName = "LandMark"
	distanceX = 0.08
	distanceY = 0.0
	angleWz = 0.0
	thresholdX = 0.1
	thresholdY = 0.1
	thresholdWz = 1.0
        subscribeDone = False
        sizeMark = 0.1
        markIds = [68, 85, 84, 204, 145, 76, 115, 153, 112, 11, 135, 127, 170, 123, 114, 121]
        effector = "None"
	mode = "WholeBody"
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
