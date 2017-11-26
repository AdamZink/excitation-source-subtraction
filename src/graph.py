import numpy as np
import os
import matplotlib.pyplot as plt

class Graph:

	def __init__(self):
		self.data = np.zeros(shape=(0,2))

	def loadCsvData(self, csvFilename):
		self.data = np.loadtxt(os.path.join('..', 'input', csvFilename), delimiter=',', skiprows=1)

	def printData(self):
		print('Shape: ' + str(self.data.shape) + '\nData:\n' + str(self.data))

	def showGraph(self):

		frequencyList, intensityList = self.data.T
		plt.scatter(frequencyList, intensityList)
		plt.title('Frequency Distribution')
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Intensity')
		plt.show()
