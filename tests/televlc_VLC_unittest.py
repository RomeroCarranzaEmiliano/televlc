"""
	televlc_VLC_unittest.py
"""

# IMPORTS #########################################################################################
import unittest
import sys
import importlib

sys.path.insert(1, '../televlc')
import televlc
###################################################################################################


class TestVLC(unittest.TestCase):
	"""  """

	def test_this(self):
		"""
			Check if the imports used and the unittest library is working
		"""
		self.assertEqual(True, True, "Should be True")

	def test__init__(self):
		"""
			Test __init__ with default values:
				PASSWORD="alohomora", HOST="127.0.0.1", PORT="8000"
			Test __init__ given values:
				PASSWORD="anything", HOST="localhost", PORT="8080"
		"""

		# Initialization with default values
		vlc = televlc.VLC()
		self.assertEqual(vlc.PASSWORD, "alohomora", "Should be 'alohomora'")
		self.assertEqual(vlc.HOST, "127.0.0.1", "Should be '127.0.0.1'")
		self.assertEqual(vlc.PORT, "8000", "Should be '8000'")

		# Initialization with given values
		vlc = televlc.VLC("anything", "localhost", "8080")
		self.assertEqual(vlc.PASSWORD, "anything", "Should be 'anything'")
		self.assertEqual(vlc.HOST, "localhost", "Should be 'localhost'")
		self.assertEqual(vlc.PORT, "8080", "Should be '8080'")


	def test_start_telnet_interface(self):
		"""
		"""

		vlc = televlc.VLC()
		self.assertTrue(vlc.start_telnet_interface())
		self.assertFalse(vlc.server == None)
		# Terminate process
		vlc.server.terminate()
		self.assertEqual(vlc.server.poll(), None, "Sould be None")

		#vlc = televlc.VLC("", "an invalid host", "an invalid port")
		#self.assertFalse(vlc.start_telnet_interface())
		#vlc.server.terminate()
		#self.assertEqual(vlc.server.poll(), None, "Should be None")


	def test_connect_to_telnet_interface(self):
		"""
		"""

		vlc = televlc.VLC()
		vlc.start_telnet_interface()
		#vlc.connect_to_telnet_interface()

		self.assertTrue(vlc.connect_to_telnet_interface())
		#self.assertFalse(self.tn == None)

		vlc.server.terminate()
		self.assertEqual(vlc.server.poll(), None, "Should be None")


if __name__ == "__main__":
	unittest.main()