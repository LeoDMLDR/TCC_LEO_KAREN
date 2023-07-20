import csv

# Initialize arrays to store data
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []

# Open the text file and read the data using csv.reader
with open("REP0101.TXT", "r") as file:
    reader = csv.reader(file)
        
    # Read the header row to determine the indices of each column
    header = reader
    col1_index = reader.index("Tempo")
    col2_index = header.index('"A3e"')
    col3_index = header.index('"A3d"')
    col4_index = header.index('"CA1e"')
    col5_index = header.index('"CA1d"')
    
    next(reader)
    
    # Read each row of data starting from the second row and store the values in the corresponding arrays
    for row in reader:
        col1.append(row[col1_index])
        col2.append(row[col2_index])
        col3.append(row[col3_index])
        col4.append(row[col4_index])
        col5.append(row[col5_index])
