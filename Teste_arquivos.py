import openpyxl

start_crise = []
end_crise = []
start_naocrise = []
end_naocrise = []

workbook = openpyxl.load_workbook('dados.xlsx')
data = workbook['REP0102']

column1 = []
column2 = []
column3 = []
column1_f = []
column2_f = []
column3_f = []
interval_crise = []

for cell in data['A']:
    
    if cell.value is None:
        break
    else:    
        time_str = cell.value
      
        time_parts = time_str.split(':')

        hh, mm, ss_s = time_parts
                   
        hh = float(hh)
        mm = float(mm)
        ss_s = float(ss_s)

        time_in_seconds = hh * 3600 + mm * 60 + ss_s
        column1.append(time_in_seconds)
        ponto=round(time_in_seconds*256)
        column1_f.append(ponto)   

for cell in data['B']:
    
    if cell.value is None:
        break
    else:    
        time_str = cell.value
      
        time_parts = time_str.split(':')

        hh, mm, ss_s = time_parts
                   
        hh = float(hh)
        mm = float(mm)
        ss_s = float(ss_s)

        time_in_seconds = hh * 3600 + mm * 60 + ss_s
        column2.append(time_in_seconds)
        ponto=round(time_in_seconds*256)
        column2_f.append(ponto)   

print(column1_f[0])
print(column2_f[0])
#print(column3)
