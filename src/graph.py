import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class Graph:

	def __init__(self):
		self.x_data = None
		self.y_data = None
		self.popt = None

	def load_csv_data(self, filename):
		data_frame = pd.read_csv(os.path.join('..', 'input', filename), sep=',', header=0)
		self.x_data = data_frame['Frequency']
		self.y_data = data_frame['Intensity']
		self.calc_exp_model()

	def exp_func(self, x, a, b, c, d):
		return a * (b ** (x - c)) + d

	def get_data_in_fit_range(self, data):
		return data[500:730]

	def get_x_data_for_fit(self):
		return self.get_data_in_fit_range(self.x_data)

	def get_y_data_for_fit(self):
		return self.get_data_in_fit_range(self.y_data)

	def calc_exp_model(self):
		self.popt, pcov = curve_fit(
			self.exp_func,
			self.get_x_data_for_fit(),
			self.get_y_data_for_fit(),
			p0=[1000, 0.99, 560, 0.1],
			bounds=(0, [10000, 10000, 10000, 500]))
		print('popt: ' + str(self.popt))

	def print_data(self):
		print('X data: ' + str(self.x_data) + '\nY data:\n' + str(self.y_data))

	def show_graph(self):
		plt.title('Frequency Distribution')
		plt.xlabel('Frequency (Hz)')
		plt.xlim(xmin=500, xmax=800)
		plt.ylabel('Intensity')
		plt.ylim(ymin=0, ymax=10000)

		plt.plot(self.x_data, self.y_data)

		if self.popt is not None:
			x_data_fit = self.x_data[450:]
			y_data_fit = self.exp_func(self.x_data[450:], *self.popt)
			plt.plot(x_data_fit, y_data_fit, '--')

		plt.show()
