import os
import pprint
import pygame

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}
            for i in range(0,6):
                self.axis_data[i] = 0.0

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                
                os.system('clear')
                pprint.pprint(self.button_data)
                pprint.pprint(self.axis_data)
                pprint.pprint(self.hat_data)

    def pollEvents(self):
        if not self.axis_data:
            self.axis_data = {}
            for i in range(0,6):
                self.axis_data[i] = 0.0

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

    def getLeftYAxis(self):
        self.pollEvents()
        return self.axis_data[1]

    def getLeftXAxis(self):
        return self.axis_data[0]

    def getRightYAxis(self):
        return self.axis_data[5]

    def getRightXAxis(self):
        return self.axis_data[2]

    def getXButton(self):
        self.pollEvents()
        return self.button_data[1]

    def getSquareButton(self):
        return self.button_data[0]

    def getTriangleButton(self):
        return self.button_data[3]

    def getCircleButton(self):
        return self.button_data[2]

    def getLeftTrigger(self):
        return self.axis_data[3]

    def getRightTrigger(self):
        return self.axis_data[4]



if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()