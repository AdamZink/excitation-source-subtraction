import numpy as np
from scipy.signal import argrelextrema

class FindExtrema(object):

	# Find the index of vector where the signal drops by a specified amount
	# vector: the 1D signal to analyze
	# number_of_points: the number of values to skip ahead for drop check
	# 		(higher value will miss local minima)
	# percent_drop: the percentage difference between first point
	# 		and last point to indicate large enough drop
	# Returns index of point where the drop starts,
	# 		or None if no such drop is found
	@classmethod
	def get_index_of_first_drop(cls, vector, number_of_points=3, percent_drop=0.05):
		if (len(vector) < number_of_points + 1) or number_of_points < 1 :
			return None

		test_indices = np.arange(0, len(vector) - number_of_points)
		for index in test_indices:
			if ((vector[index] - vector[index + number_of_points]) * 1.0) / vector[index] >= percent_drop:
				return index
		return None
