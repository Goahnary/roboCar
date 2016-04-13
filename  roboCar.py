import RPi.GPIO as GPIO

class roboCar(object):
	currentAction = "STOPPED"
	currentForwardBackwardAction = "STOPPED"

	GPIO.setmode(GPIO.BOARD)
 
	Motor1A = 16
	Motor1B = 18
	Motor1E = 22  # Enable

	Motor2A = 23
	Motor2B = 21
	Motor2E = 19  # Enable
	 
	GPIO.setup(Motor1A,GPIO.OUT)
	GPIO.setup(Motor1B,GPIO.OUT)
	GPIO.setup(Motor1E,GPIO.OUT)

	GPIO.setup(Motor2A,GPIO.OUT)
	GPIO.setup(Motor2B,GPIO.OUT)
	GPIO.setup(Motor2E,GPIO.OUT)

	def moveForward():
		currentAction = "FORWARD"
		currentForwardBackwardAction = "FORWARD"

		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.HIGH)


	def moveBackward():
		currentAction = "BACKWARD"
		currentForwardBackwardAction = "BACKWARD"

		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

	def moveLeft():
		currentAction = "LEFT"

		# if going wrong way, change here.
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.HIGH)

	def moveRight():
		currentAction = "RIGHT"

		# if going wrong way, change here.
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

	def stopMoving():
		currentAction = "STOPPED"
		currentForwardBackwardAction = "STOPPED"
		GPIO.output(Motor1E,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.LOW)

	def stopMoveForward():
		if currentAction == "FORWARD":
			stopMoving()
		elif((currentAction == "LEFT" or currentAction == "RIGHT") and currentForwardBackwardAction == "FORWARD"):
			currentForwardBackwardAction = "STOPPED"

	def stopMoveBackward():
		if currentAction == "BACKWARD":
			stopMoving()
		elif((currentAction == "LEFT" or currentAction == "RIGHT") and currentForwardBackwardAction == "BACKWARD"):
			currentForwardBackwardAction = "STOPPED"

	def stopTurnLeft():
		if(currentAction == "LEFT"):
			if(currentForwardBackwardAction == "STOPPED"):
				stopMoving()
			elif(currentForwardBackwardAction == "FORWARD"):
				moveForward()
			elif(currentForwardBackwardAction == "BACKWARD"):
				moveBackward()


	def stopTurnRight():
		if(currentAction == "RIGHT"):
			if(currentForwardBackwardAction == "STOPPED"):
				stopMoving()
			elif(currentForwardBackwardAction == "FORWARD"):
				moveForward()
			elif(currentForwardBackwardAction == "BACKWARD"):
				moveBackward()

	def cleanupBeforeQuit():
		stopMoving()
		GPIO.cleanup()
