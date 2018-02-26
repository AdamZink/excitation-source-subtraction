import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from find_extrema import FindExtrema
from sheet import Sheet

class Grapher:

	def __init__(self):
		self.x_data = None
		self.y_data = None
		self.x_col_name = None
		self.y_col_name = None
		self.fit_index_start = None
		self.fit_index_end = None
		self.popt = None
		self.sheet = None

	def load_sheet_from_excel(self, filename, sheet_name):
		self.sheet = Sheet()
		self.sheet.load_excel_sheet(filename, sheet_name)

	def sum_exp_func(self, x, a, b, c, d, e, f):
		return (a * (b ** (x - c))) + (d * (e ** (x - f)))

	def original_func(self, x_index):
		return self.y_data[x_index]

	def set_fit_index_start(self):
		points = 50
		self.fit_index_start = int(points * 0.75) + FindExtrema.get_index_of_first_drop(
			self.y_data,
			number_of_points=points,
			percent_drop=0.25
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

	def setup_for_fit(self):
		self.x_data = self.sheet.get_measurements(self.x_col_name)
		self.y_data = self.sheet.get_measurements(self.y_col_name)
		self.set_fit_index_start()
		self.set_fit_index_end()

	def calc_exp_model(self, x_col_name, y_col_name):
		self.x_col_name = x_col_name
		self.y_col_name = y_col_name
		self.setup_for_fit()
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
		plt.xlabel(self.x_col_name)
		plt.xlim(xmin=500, xmax=1000)
		plt.ylabel('Intensity of ' + self.y_col_name)
		plt.ylim(ymin=0, ymax=65000)

		plt.plot(self.x_data, self.y_data)

		if self.popt is not None:
			x_data_fit = self.x_data[525:]
			y_data_fit = self.sum_exp_func(self.x_data[525:], *self.popt)
			plt.plot(x_data_fit, y_data_fit, '--')

			y_data_subtract = np.subtract(
				self.original_func(np.arange(2048)[525:]),
				self.sum_exp_func(x_data_fit, *self.popt)
			)
			plt.plot(x_data_fit, y_data_subtract, '-')

			# evaluate at 673.93 nm, i.e. sample 929 = index 928 (approximate peak wavelength)
			print(y_data_subtract)
			print(str(self.original_func(928)) + ' -> ' + str(y_data_subtract[928]))

		plt.show()
