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
    if(joystick.getLeftYAxis() > 0.2):
        print("Up!")
    else:
        print("Nothing!")

    os.system('clear')
    print("I got here!")

#bot.start()
#bot.safe()



