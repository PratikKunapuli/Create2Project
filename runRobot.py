#import create2api
import os
import sys
import controller


if __name__ == "__main__":
    """
        Initialization
    """
    if(len(sys.argv) > 1):
        DEBUG = sys.argv[1] == "DEBUG"


    #bot = create2api.Create2()
    #bot.start()
    #bot.safe()
    joystick = controller.PS4Controller()
    joystick.init()
    if DEBUG:
        joystick.listen()

    exitButton = False #X on the PS4 controller.

    """
        Looping Code
    """
    while(not exitButton):
        joystick.pollEvents()
        exitButton = joystick.getXButton()
        leftX = joystick.getLeftXAxis()
        leftY = joystick.getLeftYAxis()
        rightX = joystick.getRightXAxis()
        rightY = joystick.getRightYAxis()

        if DEBUG:
            print('LeftX= {:f}'.format(leftX))
            print('LeftY= {:f}'.format(leftY))
            print('RightX= {:f}'.format(rightX))
            print('RightY= {:f}'.format(rightY))
            os.system('clear')
        

