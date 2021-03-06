import RPi.GPIO as GPIO

class roboCar(object):
	def __init__(self):
		self.currentAction = "STOPPED"
		self.currentForwardBackwardAction = "STOPPED"

		GPIO.setmode(GPIO.BOARD)
	 
		self.Motor1A = 18
		self.Motor1B = 16
		self.Motor1E = 22

		self.Motor2A = 19
		self.Motor2B = 21
		self.Motor2E = 23
		 
		GPIO.setup(self.Motor1A,GPIO.OUT)
		GPIO.setup(self.Motor1B,GPIO.OUT)
		GPIO.setup(self.Motor1E,GPIO.OUT)

		GPIO.setup(self.Motor2A,GPIO.OUT)
		GPIO.setup(self.Motor2B,GPIO.OUT)
		GPIO.setup(self.Motor2E,GPIO.OUT)

	def moveForward(self):
		self.currentAction = "FORWARD"
		self.currentForwardBackwardAction = "FORWARD"

		GPIO.output(self.Motor1A,GPIO.HIGH)
		GPIO.output(self.Motor1B,GPIO.LOW)
		GPIO.output(self.Motor1E,GPIO.HIGH)

		GPIO.output(self.Motor2A,GPIO.HIGH)
		GPIO.output(self.Motor2B,GPIO.LOW)
		GPIO.output(self.Motor2E,GPIO.HIGH)


	def moveBackward(self):
		self.currentAction = "BACKWARD"
		self.currentForwardBackwardAction = "BACKWARD"

		GPIO.output(self.Motor1A,GPIO.LOW)
		GPIO.output(self.Motor1B,GPIO.HIGH)
		GPIO.output(self.Motor1E,GPIO.HIGH)

		GPIO.output(self.Motor2A,GPIO.LOW)
		GPIO.output(self.Motor2B,GPIO.HIGH)
		GPIO.output(self.Motor2E,GPIO.HIGH)

	def moveLeft(self):
		self.currentAction = "LEFT"

		# if going wrong way, change here.
		GPIO.output(self.Motor1A,GPIO.LOW)
		GPIO.output(self.Motor1B,GPIO.HIGH)
		GPIO.output(self.Motor1E,GPIO.HIGH)

		GPIO.output(self.Motor2A,GPIO.HIGH)
		GPIO.output(self.Motor2B,GPIO.LOW)
		GPIO.output(self.Motor2E,GPIO.HIGH)

	def moveRight(self):
		self.currentAction = "RIGHT"

		# if going wrong way, change here.
		GPIO.output(self.Motor1A,GPIO.HIGH)
		GPIO.output(self.Motor1B,GPIO.LOW)
		GPIO.output(self.Motor1E,GPIO.HIGH)

		GPIO.output(self.Motor2A,GPIO.LOW)
		GPIO.output(self.Motor2B,GPIO.HIGH)
		GPIO.output(self.Motor2E,GPIO.HIGH)

	def stopMoving(self):
		self.currentAction = "STOPPED"
		self.currentForwardBackwardAction = "STOPPED"
		GPIO.output(self.Motor1E,GPIO.LOW)
		GPIO.output(self.Motor2E,GPIO.LOW)

	def stopMoveForward(self):
		if self.currentAction == "FORWARD":
			self.stopMoving()
		elif((self.currentAction == "LEFT" or self.currentAction == "RIGHT") and self.currentForwardBackwardAction == "FORWARD"):
			self.currentForwardBackwardAction = "STOPPED"

	def stopMoveBackward(self):
		if self.currentAction == "BACKWARD":
			self.stopMoving()
		elif((self.currentAction == "LEFT" or self.currentAction == "RIGHT") and self.currentForwardBackwardAction == "BACKWARD"):
			self.currentForwardBackwardAction = "STOPPED"

	def stopTurnLeft(self):
		if(self.currentAction == "LEFT"):
			if(self.currentForwardBackwardAction == "STOPPED"):
				self.stopMoving()
			elif(self.currentForwardBackwardAction == "FORWARD"):
				self.moveForward()
			elif(self.currentForwardBackwardAction == "BACKWARD"):
				self.moveBackward()


	def stopTurnRight(self):
		if(self.currentAction == "RIGHT"):
			if(self.currentForwardBackwardAction == "STOPPED"):
				self.stopMoving()
			elif(self.currentForwardBackwardAction == "FORWARD"):
				self.moveForward()
			elif(self.currentForwardBackwardAction == "BACKWARD"):
				self.moveBackward()

	def cleanupBeforeQuit(self):
		self.stopMoving()
		GPIO.cleanup()
