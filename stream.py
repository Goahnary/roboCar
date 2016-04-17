import picamera

camera = picamera.PiCamera()

while 1:
	camera.capture('/tmp/stream/pythonCam.jpg')
