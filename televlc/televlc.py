"""
	televlc.py

	Control VLC with python via a telenet interface
"""

# IMPORTS #########################################################################################
import subprocess
import telnetlib
from time import sleep
###################################################################################################

class VLC():
	def __init__(self, PASSWORD="alohomora", HOST="127.0.0.1", PORT="8000"):
		""" Initialization of the VLC object instance """
		self.PASSWORD = PASSWORD
		self.HOST = HOST
		self.PORT = PORT
		self.server = None
		self.tn = None
		self.time_rate = 0.01
		self.intent_limit = 10


	def start_telnet_interface(self):
		""" 
			Start VLC graphic interface(normal vlc reproducer) 
			and telnet interface(for the app to control it) 

			* Some validation should be added
		"""

		try:
			self.server = subprocess.Popen(["vlc", "--extraintf", "telnet", "--telnet-password", self.PASSWORD, 
				"--telnet-host", self.HOST, "--telnet-port", self.PORT], shell=False, stdout=subprocess.PIPE, 
				stderr=subprocess.PIPE)
		except:
			return False

		return True


	def connect_to_telnet_interface(self):
		""" 
			Connects to the already started telnet interface.
			Commands given to telnet have to be encoded to ascii.
			Due to the normal lag when starting up the interface, it is needed to do a re-try
			when connecting to the interface in case both functions are called without waiting,
			like:
			`
				vlc.start_telnet_interface()
				vlc.connect_to_telnet_interface()
			`
			instead of:
			`
				vlc.start_telnet_interface()
				time.sleep(1)
				vlc.connect_to_telnet_interface()
			`
			To solve the case in which we want to connect to another telnet interface already
			created outside the script or when the waiting time shouldn't be that big, the 
			sleep before every intent goes from 0.1s and increases 50% for every intent.

			* Should verify if there is a started telnet interface
		"""

		# Get the initial time rate
		time_rate = self.time_rate

		# Try until the intent limit or success
		for intent in range(0, self.intent_limit):
			error = None

			try:
				# Telnet connection
				self.tn = telnetlib.Telnet(self.HOST, self.PORT)

				# Wait until the password is asked
				message = "Password:"
				message = message.encode("ascii")
				self.tn.read_until(message)

				# Write message to telnet
				message = f"{self.PASSWORD}\n"
				message = message.encode("ascii")
				self.tn.write(message)
			except Exception as e:
				error = e

			if error:
				# Wait some time until next intent
				sleep(time_rate)
				# Grow the next waiting time
				time_rate *= 1.5
			else:
				# Succesfull intent, then continue
				break


		if self.tn == None:
			return False
		else:
			return True

	
	def do(self, command):
		"""
			Executes the given command in the already connected telnet interface
		
			The command recived must be writteng as a list, ej: [command, parameter1, parameter2]

			* Should verify there is a connection to the telnet interface
		"""

		# Command validation
		if type(command) != list:
			return "[ERROR] The command provided is not a list" + str(command)


		# Create the command from the list
		glued_command = ""
		for i in range(len(command)):
			if type(command[i]) == str:
				glued_command += command[i]
			else:
				return False

		try:
			# Wait until the console prompt appears(>)
			message = ">"
			message = message.encode("ascii")
			self.tn.read_until(message)

			# Write command to telnet
			message = f"{command}\n"
			message = message.encode("ascii")
			self.tn.write(message)
		except:
			return False

		return True



	def disconnect_from_telnet_interface(self):
		"""
			Disconnects from the telnet interface

			* Should verify that there is a telnet interface connection to disconnect from
		"""	

		# Sends an exit message to exit the telnet connection
		return self.do("exit")

