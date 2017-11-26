import numpy as np
import os

class Graph:

	def loadCsvData(self, csvFilename):
		self.data = np.loadtxt(os.path.join('..', 'input', csvFilename), delimiter=',', skiprows=1)

	def printData(self):
		print('Shape: ' + str(self.data.shape) + '\nData:\n' + str(self.data))
