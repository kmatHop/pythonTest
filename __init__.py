from check50 import *

class test(Checks):

	@check()
	def exists(self):
		"""test.py exists"""
		self.require("test.py")

	
