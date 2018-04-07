class Parameters:

	def __init__():
		self.filename = None
		self.sheets = None
		self.mixtures = None
		self.gases = None
		self.measurements = None
		self.x_index_of_peak = None

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
