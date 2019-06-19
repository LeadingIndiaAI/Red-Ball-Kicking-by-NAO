import time
import qi
import config
def moveToRedBall(IP, PORT):
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
    memory = config.loadProxy("ALMemory")
    tracker.setEffector(effector)
    tracker.registerTarget(targetName, diameter)
    tracker.setRelativePosition([-distanceX, distanceY, angleWz, thresholdX, thresholdY, thresholdWz])
    tracker.setMode(mode)
    import time
    t_end = time.time() + 20
    while True:
        if time.time() < t_end:
            tracker.track(targetName)
                
        else:
            tracker.stopTracker()
            tracker.unregisterTarget(targetName)
            break
