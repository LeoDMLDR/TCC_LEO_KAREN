import numpy as np

A3e_raw = []
A3d_raw = []
CA1e_raw = []
CA1d_raw = []

A3e = []
A3d = []
CA1e = []
CA1d = []

def convert_float(dados):
  X0 = []
  X1 = []
  X2 = []
  X3 = []
  X4 = []
  
  for row in dados:
      row = row.split('E')
      X2.append(float(row[0].replace(',','.')))
      X3.append(int(row[1]))
  for row in X3:
      X4.append(10**row)
  X1 = [x * y for x, y in zip(X2, X4)]
  return X1

def tratamento_dados(txt_file_name):
  
  f_header = open(txt_file_name,'r')
  header = next(f_header)
  header = header.split('\t')

  A3e_index = header.index('"A3e"')
  A3d_index = header.index('"A3d"')
  CA1e_index = header.index('"CA1e"')
  CA1d_index = header.index('"CA1d"')

  f = np.loadtxt(txt_file_name, delimiter='\t', skiprows=2, dtype=str)
  for row in f:
      A3e_raw.append(row[A3e_index])
      A3d_raw.append(row[A3d_index])
      CA1e_raw.append(row[CA1e_index])
      CA1d_raw.append(row[CA1d_index])

  A3e = convert_float(A3e_raw)
  A3d = convert_float(A3d_raw)
  CA1e = convert_float(CA1e_raw)
  CA1d = convert_float(CA1d_raw)
  return A3e, A3d, CA1e, CA1e