

class Controller:
    
    def __init__(self, Kp, setPoint):
        
        self.Kp = Kp
        self.setPoint = setPoint
        
    def run(self, actualVal):
        
        
       
        # Compare actual to setpoint to find the error
        # Multiply by Kp
        outputVal = self.Kp * (self.setPoint - actualVal)
        
        
        return outputVal

    def set_setpoint(self, setPt):
        self.setPoint = setPt
        
    def set_Kp(self, Kp):
        self.Kp = Kp