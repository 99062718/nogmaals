from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for x in range(5):
    robotArm.moveRight()
    for y in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()