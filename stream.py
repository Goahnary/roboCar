import picamera

camera = picamera.PiCamera()

while 1:
	camera.capture('stream/pythonCam.jpg')
