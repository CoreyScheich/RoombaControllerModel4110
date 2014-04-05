__author__ = 'csch'

#Roomba Serial codes from http://www.irobot.com/images/consumer/hacker/Roomba_SCI_Spec_Manual.pdf

RoombaStart = 128
RoombaBaud = 129
RoombaControl = 130
RoombaSafeMode = 131
RoombaFullMode = 132
RoombaPower = 133
RoombaSpotClean = 134
RoombaClean = 135
RoombaMaxClean = 136
#RoombaDrive can be followed by 4 bytes
#Velocity and Radius are represented by 2 bytes a piece calculated from the hex of a decimal
#Velocity = -200 = hex FF38 = [hex FF] [hex 38] = [255] [56
RoombaDrive = 137
RoombaMotors = 138
RoombaLEDs = 139
RoombaSong = 140
RoombaPlaySong = 141
RoombaReadSensors = 142
RoombaForceDock = 143


#Roomba BaudRate Codes
BaudCode300 = 0
BaudCode600 = 1
BaudCode1200 = 2
BaudCode2400 = 3
BaudCode4800 = 4
BaudCode9600 = 5
BaudCode14400 = 6
BaudCode19200 = 7
BaudCode28800 = 8
BaudCode38400 = 9
BaudCode57600 = 10
BaudCode115200 = 11

#Roomba Motor Codes
MotorCodeSideBrush = 1
MotorCodeVacuum = 2
MotorCodeMainBrush = 4

#Roomba Motor OverCurrentCodes
MotorOCCodeSideBrush = 1
MotorOCCodeVacuum = 2
MotorOCCodeMainBrush = 4
MotorOCCodeDriveRight = 8
MotorOCCodeDriveLeft = 16

#BumpDrop Codes
bdBumpRight = 1
bdBumpLeft = 2
bdDropRight = 4
bdDropLeft = 8
bdDropCaster = 16


#Roomba LED Codes
LEDCodeDirtDetect = 1
LEDCodeMAX = 2
LEDCodeClean = 4
LEDCodeSpot = 8
LEDCodeStatus = 16
LEDCodeStatus2 = 32

#Roomba Sensor Read Codes
SensorCodeALL = 0
SensorCodePacket1 = 1
SensorCodePacket2 = 2
SensorCodePacket3 = 3

#Roomba Sensor Bytes
SensorCodeALLBytes = 26
SensorCodePacket1Bytes = 10
SensorCodePacket2Bytes = 6
SensorCodePacket3Bytes = 10


