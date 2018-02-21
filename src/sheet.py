import pandas as pd
import os

class Sheet:

	def __init__(self):
		self.excel_path = None
		self.sheet_name = None
		self.dataframe = None
		self.measurements = {}

	def load_excel_sheet(self, filename, sheet_name):
		self.excel_path = os.path.join('..', 'input', filename)
		self.sheet_name = sheet_name
		self.dataframe = pd.read_excel(self.excel_path, sheet_name=self.sheet_name, header=0)
		for col_name in list(self.dataframe):
			self.measurements[col_name] = self.dataframe[col_name]

	def get_measurements(self, col_name):
		return self.measurements[col_name]
