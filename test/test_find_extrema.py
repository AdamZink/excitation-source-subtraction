import unittest
from context import FindExtrema

import numpy as np

class TestFindExtrema(unittest.TestCase):

	# Tests for get_index_of_first_drop
	def test_get_index_of_first_drop_index_1(self):
		vector = np.array([100, 100, 100, 100, 95])
		self.assertEqual(1, FindExtrema.get_index_of_first_drop(vector, number_of_points=3, percent_drop=0.05))

	def test_get_index_of_first_drop_None_too_short(self):
		vector = np.array([100])
		self.assertEqual(None, FindExtrema.get_index_of_first_drop(vector, number_of_points=1, percent_drop=0.05))

	def test_get_index_of_first_drop_None_no_drop(self):
		vector = np.array([100, 100, 100, 150])
		self.assertEqual(None, FindExtrema.get_index_of_first_drop(vector, number_of_points=3, percent_drop=0.05))

	def test_get_index_of_first_drop_None_invalid_parameter(self):
		vector = np.array([100, 100, 100, 100, 95])
		self.assertEqual(None, FindExtrema.get_index_of_first_drop(vector, number_of_points=0, percent_drop=0.05))
