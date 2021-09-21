from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for x in range(4):
    for y in range(x + 1):
        robotArm.grab()
        for z in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()