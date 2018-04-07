import numpy as np

class Parameters:

	def __init__(self):
		self.filename = None
		self.sheets = None
		self.mixtures = None
		self.gases = None
		self.measurements = None
		self.x_index_of_peak = None
		self.fit_p0 = None

	def sum_exp_func(self, x, a, b, c, d, e, f):
		return (a * (b ** (x - c))) + (d * (e ** (x - f)))

	def double_exp_func(self, x, a, b, c, d):
		return (a * (np.e ** (-b * x))) + (c * (np.e ** (-d * x)))

	def use_first_parameters(self):
		self.filename = 'Solvent_variation_condensed_data.xlsx'
		# ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
		self.sheets = ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
		# ['90_10', '75_25', '50_50']
		self.mixtures = ['90_10', '75_25', '50_50']
		# ['N2', 'Air', 'O2']
		self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		self.measurements = ['1', '2', '3']
		# evaluate at 673.93 nm, i.e. sample 929 = index 928
		self.x_index_of_peak = 928
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [1000, 0.99, 500, 1000, 0.99, 500]

	def use_second_parameters(self):
		self.filename = 'Green_PtTFPP_combined_data.xlsx'
		# ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
		self.sheets = ['Initial']
		# ['0pt1', '0pt5', '3', '10']
		self.mixtures = ['0pt1', '0pt5', '3', '10']
		# ['N2', 'Air', 'O2']
		self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		self.measurements = ['1', '2', '3']
		# evaluate at 652.35 nm, i.e. sample 866 = index 865
		self.x_index_of_peak = 865
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [1000, 0.99, 500, 1000, 0.99, 500]
