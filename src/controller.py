"""! @file controller.py
This program is a proportional controller class that moves a
12V Brushed DC Motor to a desired location. The class initializes a gain constant, Kp,
and a desired motor location; and sets motor speed accordingly.
"""

class Controller:
    """!
    The class initializes a gain constant, Kp,
    and a desired motor location; and sets motor speed accordingly.
    """
    def __init__(self, Kp, setPoint):
        """! 
        This function initializes motor gain constant and desired encoder count
        @param Kp User specified proportional gain constant.
        @param setPoint The encoder count of the desired motor location.
        """

        self.Kp = Kp
        self.setPoint = setPoint
        
    def run(self, actualVal):
        """!
        This function handles proportional control by comparing current motor
        location to the desired location and sets duty cycle accordingly.
        @param actualVal The current encoder count.
        """    
       
        # Compare actual to setpoint to find the error
        # Multiply by Kp
        outputVal = self.Kp * (self.setPoint - actualVal)
        
        
        return outputVal

    def set_setpoint(self, setPt):
        """!
        This function sets the desired motor location.
        """ 
        self.setPoint = setPt
        
    def set_Kp(self, Kp):
        """!
        This function sets the user input gain.
        """ 
        self.Kp = Kp