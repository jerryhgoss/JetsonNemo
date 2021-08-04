import time
import Jetson.GPIO as GPIO
import busio
#import digitalio
#import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


#def SPI_initialize():
#	
#	# create the spi bus
#	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
#	jspi = board.spi()

#	# create the cs (chip select)
#	cs = digitalio.DigitalInOut(board.D5)

#	# create the mcp object
#	mcp = MCP.MCP3008(spi, cs)

#	# create an analog input channel on pin 0
#	chan = AnalogIn(mcp, MCP.P0)

#print('Raw ADC Value: ', chan.value)
#print('ADC Voltage: ' + str(chan.voltage) + 'V'

input_pin = 12

def main():
	GPIO.setwarnings(False)
	prev_value = None
	# Pin Setup:
	GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
	GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin

	#	print("Starting conductivity sensor tests!")

	print("Starting demo now! Press CTRL+C to exit")
	print("The mode is set to {}".format(GPIO.getmode()))	
	try:
		while True:
		    value = GPIO.input(input_pin)
		    if value != prev_value:
		        if value == GPIO.HIGH:
		            value_str = "HIGH"
		        else:
		            value_str = "LOW"
		        print("Value read from pin {} : {}".format(input_pin,
		                                                   value_str))
		        prev_value = value
		    time.sleep(1)
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
    main()
