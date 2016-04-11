import time
import socket
import sys

port = 1337

# create our socket, or quit trying
try:
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ip = socket.gethostbyname( "wkuacm.org" );
except socket.error:
	print "failed to create socket :("
	sys.exit(1)
except socket.gaierror:
	print "failed to resolve wkuacm.org"
	sys.exit(1)
	
# connects to our server and asks for input
clientSocket.connect((ip, port)) # accepts a tuple of the ip and port

print "Enter text to be uppercased"

if(handleConnect(clientSocket)):
	receiveCommands(clientSocket)



def processCommand(rawCommand):
	if(rawCommand.indexOf(" ") == -1):
		# All commands have a space in them
		return

	command = rawCommand.split(" ")[0]
	subCommand = rawCommand.split(" ")[1]

	if(command == "MOVE"):
		if(subCommand == "FORWARD"):
			pass
		elif(subCommand == "LEFT"):
			pass
		elif(subCommand == "RIGHT"):
			pass
		elif(subCommand == "BACKWARD"):
			pass
		else:
			print "Uknown MOVE subCommand " + subcommand
	elif (command == "ACTION"):
		if(subCommand == "STOP"):
			pass
		elif(subCommand == "DISCONNECT"):
			pass
		else:
			pass
	else:
		print "Unknown command " + command

receiveCommands(clientSocket):
	running = True
	while(running):
		#clientSocket.send(message + "\r\n") # sends to server, without the \r\n it doesn't work
		response = clientSocket.recv(1024)  # get response
		print response.replace("\r\n","")   # remove extra new line characters
		processCommand(response)            # send the command for processing
		
	
	clientSocket.close()

def handleConnect(clientSocket):
	clientSocket.send("CONNECT CAR\r\n")    # Tell the server a car is here
	while(True):
		
		response = clientSocket.recv(1024)
		if(response == "CONTROL DISCONNECTED"):
			time.sleep(30)
			clientSocket.send("CONTROL STATUS\r\n")    # Tell the server a car is here
			continue
		else:
			return True