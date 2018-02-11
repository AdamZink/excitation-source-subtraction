import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from find_extrema import FindExtrema

class Graph:

	def __init__(self):
		self.x_data = None
		self.y_data = None
		self.fit_index_start = None
		self.fit_index_end = None
		self.popt = None

	def load_csv_data(self, filename):
		data_frame = pd.read_csv(os.path.join('..', 'input', filename), sep=',', header=0)
		self.x_data = data_frame['Wavelength']
		self.y_data = data_frame['Intensity']
		self.set_fit_index_start()
		self.set_fit_index_end()
		self.calc_exp_model()

	def exp_func(self, x, a, b, c, d):
		return a * (b ** (x - c)) + d

	def sum_exp_func(self, x, a, b, c, d, e, f):
		return (a * (b ** (x - c))) + (d * (e ** (x - f)))

	def set_fit_index_start(self):
		points = 50
		self.fit_index_start = int(points * 0.75) + FindExtrema.get_index_of_first_drop(
			self.y_data,
			number_of_points=points,
			percent_drop=0.75
		)
		print('Fit Index Start set to: ' + str(self.fit_index_start))

	def set_fit_index_end(self):
		# TODO implementation of minima after fit_index_start
		self.fit_index_end = 730
		print('Fit Index End set to: ' + str(self.fit_index_end))

	def get_data_in_fit_range(self, data):
		return pd.concat([
			data[self.fit_index_start:self.fit_index_end],
			data[1500:2000]],
			ignore_index=True
		)

	def get_x_data_for_fit(self):
		return self.get_data_in_fit_range(self.x_data)

	def get_y_data_for_fit(self):
		return self.get_data_in_fit_range(self.y_data)

	def calc_exp_model(self):
		self.popt, pcov = curve_fit(
			self.sum_exp_func,
			self.get_x_data_for_fit(),
			self.get_y_data_for_fit(),
			p0=[1000, 0.99, 500, 1000, 0.99, 500]
			)
		print('popt: ' + str(self.popt))

	def print_data(self):
		print('X data: ' + str(self.x_data) + '\nY data:\n' + str(self.y_data))

	def show_graph(self):
		plt.title('Frequency Distribution')
		plt.xlabel('Wavelength (nm)')
		plt.xlim(xmin=500, xmax=1000)
		plt.ylabel('Intensity')
		plt.ylim(ymin=0, ymax=10000)

		plt.plot(self.x_data, self.y_data)

		if self.popt is not None:
			x_data_fit = self.x_data[450:]
			y_data_fit = self.sum_exp_func(self.x_data[450:], *self.popt)
			plt.plot(x_data_fit, y_data_fit, '--')

		plt.show()
