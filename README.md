# Lab3
 ME 405 Bin 9 Lab 3 - Closed Loop Proportional Motor Control

 The code in this repository allows for a step response to be applied to closed loop control of a Pololu 12V 37D70L DC motor.

 gui.py runs on a PC, and connects to the STM32 microcontroller over serial. When the user presses the "Run" button on the gui, they are prompted to input the proportional gain in the console. This gain is then sent to the microntroller to initiate the step response.

 main.py runs on the STM32 micrcontroller and sets up the DC motor driver, encoder, and closed loop controller. It awaits a Kp value to be sent over serial, and the performs a closed loop step response on the motor. When steady state is obtained, data fromt he step response is sent back over serial to the PC.

 The PC recieves the data over serial and then plots it on the GUI. THis gives the user a visual representation of the the performance of the control loop.

 The handshaking between the two programs is set up to allow for repeated tests with varied values of Kp to determine the optimal control gain.

 
