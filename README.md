# Lab3
 ME 405 Bin 9 Lab 3 - Closed Loop Proportional Motor Control

 The code in this repository allows for a step response to be applied to closed loop control of a Pololu 12V 37D70L DC motor.

 gui.py runs on a PC, and connects to the STM32 microcontroller over serial. When the user presses the "Run" button on the gui, they are prompted to input the proportional gain in the console. This gain is then sent to the microntroller to initiate the step response.

 main.py runs on the STM32 micrcontroller and sets up the DC motor driver, encoder, and closed loop controller. It awaits a Kp value to be sent over serial, and the performs a closed loop step response on the motor. When steady state is obtained, data fromt he step response is sent back over serial to the PC.

 The PC recieves the data over serial and then plots it on the GUI. THis gives the user a visual representation of the the performance of the control loop.

 The handshaking between the two programs is set up to allow for repeated tests with varied values of Kp to determine the optimal control gain.

 ![Step](https://github.com/logdotzipp/Lab3/assets/156237159/b62b3f7e-5456-4a53-9112-9190b8967856)
 Figure 1: Step response of the motor to varied values of Kp

![Zoomed](https://github.com/logdotzipp/Lab3/assets/156237159/dc6ca88c-0c72-4d75-a4e7-840578007e54)
 Figure 2: Zoomed view of Figure 1 to analyze transient behavior. Low values of Kp (0.05, 0.1) result in undershoot and high steady state error. Relatively high values of Kp (1.0, 3.0) result in overshoot and oscillation.

![KP0_16](https://github.com/logdotzipp/Lab3/assets/156237159/583a4e1f-c114-4b3a-9e5a-1605131d18d7)
 Figure 3: Optimized proportional gain of 0.16 results in no overshoot and low steady state error.
