from time import sleep
import RPi.GPIO as GPIO

class Motor(object):
	def __init__(self, stepPin, dirPin, enablePin):
		self.stepPin = stepPin
		self.dirPin = dirPin
		self.enablePin = enablePin

		self.direction = 0

		self.stepsPerSecond = 200
	
		GPIO.setup(self.stepPin, GPIO.OUT)
        	GPIO.output(self.stepPin, 0)
		GPIO.setup(self.dirPin, GPIO.OUT)
        	GPIO.output(self.dirPin, self.direction)
		GPIO.setup(self.enablePin, GPIO.OUT)
        	GPIO.output(self.enablePin, 1)

	def setStepsPerSecond(self,stepsPerSecond):
		self.stepsPerSecond = stepsPerSecond

	def setDirection(self,direction):
		print(direction)
		if (direction != 0) and (direction != 1):
			raise ValueError('Direction must be a boolean')
		self.direction = direction
		GPIO.output(self.dirPin,direction)

	def toggleDirection(self):
		self.drection = not self.direction
		GPIO.output(self.dirPin,self.direction)
    
	def enable(self):
		GPIO.output(self.enablePin,0)

	def disable(self):
		GPIO.output(self.enablePin,1)

	def getSleepTime(self):
		time = 0.16 / self.stepsPerSecond
		return time
	
	def stepMove(self,steps):
		for i in range(0,steps):
			GPIO.output(self.stepPin,1)
			sleep(self.getSleepTime()/2)
			GPIO.output(self.stepPin,0)
			sleep(self.getSleepTime()/2)

GPIO.setmode(GPIO.BCM)
motor = Motor(16,12,21)

motor.enable()
motor.stepMove(600)
motor.setDirection(1)
sleep(2)
motor.stepMove(600)
motor.disable()
sleep(1)
GPIO.cleanup()	
