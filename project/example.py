from fuzzy import *
import matplotlib.pyplot as plt


def brakeTrain(distanceFromStop, speedOfTrain, cA, cB, cC, cD):
    #fuzzification
    moving = piecewiseLinear(speedOfTrain, cA, cB)
    closeToStop = piecewiseLinear(distanceFromStop, cC, cD)

    #rule matching
    done = fuzzyEquivalence(closeToStop, fuzzyNot(moving))

    #defuzzification
    return fuzzyNot(done)

def calculateNewSpeed(oldSpeed, deltaTime, frictionCoefficient):
    # Vt = V0 - (F*t) / m
    # F  = u * m * g
    # => Vt = V0 - u * g * t
    g = 9.82
    if oldSpeed >= 0:
        return oldSpeed - frictionCoefficient * g * deltaTime
    else:
        return oldSpeed + frictionCoefficient * g * deltaTime

def calculateNewDistance(oldDistance, deltaTime, speed):
    return oldDistance - speed * deltaTime


distance = 8000.0
speed = 100

vD = []
vS = []
vT = []

dt = 0.5
t = 0.0
closestspeed = [distance, speed]
while distance > -1 and t < 2000:
    if abs(distance) < closestspeed[0]:
        closestspeed[1] = speed
        closestspeed[0] = distance
    vD.append(distance)
    vS.append(speed)
    t += dt
    vT.append(t)

    breakLevel = brakeTrain(distance, speed, 0., 790.4,1.,0. )
    speed = calculateNewSpeed(speed, dt, breakLevel)
    distance = calculateNewDistance(distance, dt, speed)

print closestspeed
plt.plot(vT, vD, "r", vT, vS, "b")
plt.show()


