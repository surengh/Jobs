# Author: Surender Kumar
# Contact: kumarsu44@gmail.com
# 	   (+91 - 9604433613)
#
# Underlying Algorithm
# ====================
# 1. Read a small chunk (of chunksize) from the given input file (stock_data.csv)
#    (assuming file is large enough)
# 2. Compute max stock value for each company within the chunk, and track the value
#    and date (index) into max_stock_value and date_max_stock respectively.
# 3. Print date_max_stock which will print the respective date of max stock value
#    as the index, of respective companies.
#
# Unit Test Inputs
# ================
# 1. Wrong URL to file
# 2. Empty file
# 3. Bad files with missing entries
# 4. File with extra terminals (e.g ")
# 5. File with invalid data types (, as its not clear from the requirements, that,
#    whether we are supposed to ignore those rows, or, we should exit gracefully
#    flagging appropriate message to the user. The following code has been written
#    keeping former assumption in mind).


import pandas as pd;

input_file = './'+'stock_data.csv' # Path to input file
chunk_size = 2 			   # Change as per memory availability

try:
	if os.stat(input_file) <= 0:
		print "Empty file."
		sys.exit()
	else:
		dia = cvs.excel()
		dia.quoting = cvs.QOUTE_NONE
		read = pd.read_csv(input_file, dialect=dia, index_col=['Year', 'Month'], sep = ', ', error_bad_lines=False, chunksize=chunk_size)

		N = len(read.columns) - 2

		max_stock_value = [0*i for i in range(N)]
		date_max_stock = [0*i for i in range(N)]

		for chunk in read:
			for num in range (1, N):
				if max_stock_value[num] < (read['Company' + `num`]).max():
					max_stock_value[num] = (read['Company' + `num`]).max()
					date_max_stock[num] = read.ix[max_stock_value[num]]

		print date_max_stock
except OSError:
	print "File not found."
	sys.exit()
