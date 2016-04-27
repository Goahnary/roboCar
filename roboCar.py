import RPi.GPIO as GPIO

class roboCar(object):
	def __init(self):
		self.currentAction = "STOPPED"
		self.currentForwardBackwardAction = "STOPPED"

		GPIO.setmode(GPIO.BOARD)
	 
		self.Motor1A = 16
		self.Motor1B = 18
		self.Motor1E = 22

		self.Motor2A = 21
		self.Motor2B = 19
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
			stopMoving()
		elif((self.currentAction == "LEFT" or self.currentAction == "RIGHT") and self.currentForwardBackwardAction == "FORWARD"):
			self.currentForwardBackwardAction = "STOPPED"

	def stopMoveBackward(self):
		if self.currentAction == "BACKWARD":
			stopMoving()
		elif((self.currentAction == "LEFT" or self.currentAction == "RIGHT") and self.currentForwardBackwardAction == "BACKWARD"):
			self.currentForwardBackwardAction = "STOPPED"

	def stopTurnLeft(self):
		if(self.currentAction == "LEFT"):
			if(self.currentForwardBackwardAction == "STOPPED"):
				stopMoving()
			elif(self.currentForwardBackwardAction == "FORWARD"):
				moveForward()
			elif(self.currentForwardBackwardAction == "BACKWARD"):
				moveBackward()


	def stopTurnRight(self):
		if(self.currentAction == "RIGHT"):
			if(self.currentForwardBackwardAction == "STOPPED"):
				stopMoving()
			elif(self.currentForwardBackwardAction == "FORWARD"):
				moveForward()
			elif(self.currentForwardBackwardAction == "BACKWARD"):
				moveBackward()

	def cleanupBeforeQuit(self):
		stopMoving()
		GPIO.cleanup()
