#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#initiate list with pin gpio pin numbers
#PI PIN PORT & Numbers
#---------------------------------------------------------
#            pin 					pin
#===========+==========================+==================
#Power 		|1		+3.3V  +5v		  2|Power
#{I2C} SDA1 |3	 	GPIO2  +5v		  4|Power
#{I2C} SCL1 |5	 	GPIO3  GND		  6|
#GPCLK0		|7	 	GPIO4  GPIO14	  8|{UART} TXD0
#			|9	   	  GND  GPIO15	 10|{UART} RXD0
#			|11    GPIO17  GPIO18	 12|PCM_CLK
#			|13    GPIO27  GND		 14|
#			|15    GPIO22  GPIO23	 16|
#Power		|17     +3.3v  GPIO24	 18|
#SPI0_MOSI	|19    GPIO10  GND		 20|
#SPI0_MISO	|21     GPIO9  GPIO25	 22|
#SPI0_SCLK	|23    GPIO11  GPIO8	 24|SPI0_CE0_N
#			|25		  GND  GPIO7     26|SPI0_CE1_N
#{ID EEPROM}|27     ID_SD  ID_SC	 28|{ID EEPROM}
#GPCLK1		|29	    GPIO5  GND		 30|
#GPCLK2		|31     GPIO6  GPIO12    32|PWM0
#PWM1		|33    GPIO13  GND		 34|
#PCM_FS		|35    GPIO19  GPIO16	 36|
#			|37    GPIO26  GPIO20	 38|PCM_DIN
#			|39	      GND  GPIO21    40|PCM_DOUT

#Step1 delete the number with "," for the you have not pluged in. Example gpoiList [26, 19, 21]
#GPIO LIST form PIN1-40 == you can delete what pin you don't need to use
gpioList [2, 3, 4, 14, 15, 17, 18, 27, 22, 23, 24, 10, 9, 11, 25, 11, 8, 7, 5, 6, 12, 13, 19, 16, 26, 20, 21]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

#Sleep Time varables
sleepTimeShort = 0.2
sleepTimeLong = 0.1

try:
	while True:
		for i in gpioList:
			GPIO.output(i, GPIO.LOW)
			time.sleep(sleepTimeShort);
			GPIO.output(i, GPIO.HIGH)
			time.sleep(sleepTimeLong);

#End Program cleanly with keyboard
except KeyboardInterrupt:
	print "Exit Right Now..."
#Reset GPIO settings
	GPIO.cleanup()
