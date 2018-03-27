from grapher import Grapher
from writer import Writer

# ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']
sheets = ['Initial', '24 hours', '1 week', '2 weeks', '4 weeks', '1000 hr']

# ['90_10', '75_25', '50_50']
mixtures = ['90_10', '75_25', '50_50']

# ['N2', 'Air', 'O2']
gases = ['N2', 'Air', 'O2']

# ['1', '2', '3']
measurements = ['1', '2', '3']


excel_writer = Writer()
excel_writer.save_row('Time,Mix,Measurement,' + ','.join(gases))

for sheet in sheets:
	print('\n======== ' + sheet + ' ========')
	grapher = Grapher()
	grapher.load_sheet_from_excel('Solvent_variation_condensed_data.xlsx', sheet)

	for mixture in mixtures:
		for measurement in measurements:
			resultMap = {}
			for gas in gases:

				column_name = mixture + '_' + measurement + '_' + gas
				print('\n' + column_name)

				grapher.calc_exp_model('Wavelength', column_name)
				grapher.save_graph(gas + '_' + sheet + '_' + mixture + '_' + measurement)

				resultMap[gas] = grapher.get_subtracted_peak_intensity()

			excel_writer.save_row(sheet + ',' + mixture + ',' + measurement + ',' + ','.join([str(resultMap[gas]) for gas in gases]))

excel_writer.export_to_excel('subtraction_results.csv')

print('\nDone writing file')
