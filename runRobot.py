#import create2api
import os
import controller


#bot = create2api.Create2()
joystick = controller.PS4Controller()
joystick.init()
#joystick.listen()

exitButton = False #X on the PS4 controller.
while(not exitButton):
    joystick.pollEvents()
    exitButton = joystick.getXButton()
    leftX = joystick.getLeftX()
    leftY = joystick.getLeftY()
    rightX = joystick.getRightY()
    rightY = joystick.getRightX()

    print 'LeftX: %d' % (leftX)
    print 'LeftY: %d' % (leftY)
    print 'RightX: %d' % (rightX)
    print 'RightY: %d' % (rightY)


    os.system('clear')
    #print("I got here!")

#bot.start()
#bot.safe()



