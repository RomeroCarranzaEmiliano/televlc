"""
	televlc.py

	Control VLC with python via a telenet interface
"""

# IMPORTS #########################################################################################
import subprocess
import telnetlib
###################################################################################################

class VLC():
	def __init__(self, PASSWORD="alohomora", HOST="127.0.0.1", PORT="8000"):
		""" Initialization of the VLC object instance """
		self.PASSWORD = PASSWORD
		self.HOST = HOST
		self.PORT = PORT
		self.server = None
		self.tn = None


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
			Commands given to telnet have to be encoded to ascii

			* Should verify if there is a started telnet interface
		"""

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
			print(e)
			return False

		return True

	
	def do(self, command):
		"""
			Executes the given command in the already connected telnet interface
		
			The command recived must be writteng as a list, ej: [command, parameter1, parameter2]

			* Should verify there is a connection to the telnet interface
		"""

		# Command validation
		if type(command) != list:
			raise Exception("[ERROR] The command provided is not a list\n", str(command)) 

		# Wait until the console prompt appears(>)
		message = ">"
		message = message.encode("ascii")
		self.tn.read_until(message)

		# Write command to telnet
		message = f"{command}\n"
		message = message.encode("ascii")
		self.tn.write(message)


	def disconnect_from_telnet(self):
		"""
			Disconnects from the telnet interface

			* Should verify that there is a telnet interface connection to disconnect from
		"""	

		# Sends an exit message to exit the telnet connection
		self.do("exit")


	def exit(self):
		"""
			Stops the started interface

			* Should verify that there is a started interface to stop
		"""
		
		# Sends a shutdown message to stop the interface
		self.do("shutdown")
