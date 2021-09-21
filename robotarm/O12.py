from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

robotArm.speed = 3

for x in range(9, 0, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        for y in range(x):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(x):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()

robotArm.wait()