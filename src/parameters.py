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

	def get_column_name(self, mixture, measurement, gas):
		return mixture + '_' + measurement + '_' + gas

	def get_column_name_short(self, mixture, measurement, gas):
		return gas + '_' + measurement

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
		self.fit_index_end = 730
		# function for column name
		self.column_name_function = self.get_column_name

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
		self.fit_index_end = 730
		# function for column name
		self.column_name_function = self.get_column_name

	def use_third_parameters(self):
		self.filename = 'PCL_HFP_0pt5PdTFPP_Combined_2.xlsx'
		# ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
		self.sheets = ['Initial', '24 hr', '1 week']
		# ['0pt1', '0pt5', '3', '10']
		self.mixtures = ['0pt5PdTFPP']
		# ['N2', 'Air', 'O2']
		self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		self.measurements = ['1', '2', '3']
		# evaluate at 671.2 nm, i.e. sample 921 = index 920
		self.x_index_of_peak = 920
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [1000, 0.99, 500, 1000, 0.99, 500]
		self.fit_index_end = 730
		# function for column name
		self.column_name_function = self.get_column_name_short

	def use_fourth_parameters(self):
		self.filename = '3percentdutycycle combined_2.xlsx'
		# ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
		self.sheets = ['Initial', '1 week', '4 weeks', '1000 hr']
		# ['B', 'G', 'UV', 'R']
		self.mixtures = ['B', 'G', 'UV', 'R']
		# ['N2', 'Air', 'O2']
		self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		self.measurements = ['1', '2', '3']
		# evaluate at 673.93 nm, i.e. sample 929 = index 928
		self.x_index_of_peak = 928
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [1000, 0.99, 500, 1000, 0.99, 500]
		self.fit_index_end = 730
		# function for column name
		self.column_name_function = self.get_column_name

	def use_fifth_parameters(self):
		self.filename = 'Nylon 6 data.xlsx'
		# ['Initial', '1 week']
		self.sheets = ['Initial', '1 week']
		# ['Nylon 6]
		self.mixtures = ['Nylon 6']
		# ['N2', 'Air', 'O2']
		self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		self.measurements = ['1', '2', '3']
		# evaluate at 670.85 nm, i.e. sample 920 = index 919
		self.x_index_of_peak = 919
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [1000, 0.99, 500, 1000, 0.99, 500]
		self.fit_index_end = 730
		# function for column name
		self.column_name_function = self.get_column_name_short

	def use_37C_parameters(self):
		self.filename = '365_days_37C.xlsx'
		# ['Sheet1']
		self.sheets = ['Sheet1']
		# ['Nylon 6]
		self.mixtures = ['37C']
		# ['N2', 'Air', 'O2']
		#self.gases = ['N2', 'Air', 'O2']
		# ['1', '2', '3']
		#self.measurements = ['1', '2', '3']
		# evaluate at 673.93 nm, i.e. sample 929 = index 928
		self.x_index_of_peak = 928
		# Curve fit function and initial parameters
		self.fit_function = self.sum_exp_func
		self.fit_p0 = [400, 0.99, 600, 400, 0.99, 600]
		self.fit_index_end = 810
		# function for column name
		#self.column_name_function = self.get_column_name_short
