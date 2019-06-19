import config
import math
import find_goal
def take_position():
    motionProxy = config.loadProxy("ALMotion")
    config.StiffnessOn(motionProxy)
    D = find_goal.findgoal()
    theta = math.atan(D/120.0)
    x     = 0.30*(1 - math.cos(theta))
    y     = -0.30*(math.sin(theta))
    print x,y,theta 
    if D > 30.0 or D < -(30.0) :
        motionProxy.walkTo(x, y, theta )