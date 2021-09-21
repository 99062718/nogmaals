from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1,7)

color = 0
x = 1

while color != "":
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        break
    for y in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for y in range(x):
        robotArm.moveLeft()
    x += 1

robotArm.wait()