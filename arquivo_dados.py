import csv

start_crise = []
end_crise = []
start_naocrise = []
end_naocrise = []
len4 = 4
len7 = 7

def tratamento_4(dados):
  dados=dados.split(':')
  return dados


with open('/content/drive/MyDrive/TCC/dados.csv', 'r') as csvfile:
   
    csvreader = csv.reader(csvfile)

  
    column1 = []
    column2 = []
    column3 = []
    column1_f = []
    column2_f = []
    column3_f = []


    #TEM QUE DAR O SPLIT EM : NOS TEMPOS EM QUE DA MAIS DE UM MINUTO E MULTIPLICAR PELOS MINUTOS/HORAS
    #VER METODO PARA QUANTIFICAR O NUMERO DE : PARA USAR COMO CRITERIO DE SELECAO DE TRATAMENTO DE DADOS
    #PELO LEN DA PRA SABER, OS SEGNDOS TEM LEN 4, MINUTOS LEN 7 E HORAS LEN 10
    #DAR UM SPLIT EM : NOS QUE TEM LEN 7 E MULTIPICAR O [0] POR 60 E SOMAR COM O RESTO
    #DAR UM SPLIT EM : NOS QUE TEM LEN 10 E MULTIPLICAR [0]*60*60+[1]*60+[2]
    #OBS NESTE CASO ESPECIFICO TODOS OS INICIOS E TERMINOS DE CRISE SAO DO MESMO "LEN" ENTAO NAO TRATEI A VERIFICACAO DOS DOIS CASOS, MAS BASTARIA CRESCER A LOGICA PRA MAIS UM ESTAGIO
    for row in csvreader:
        column1.append(row[0])
        column2.append(row[1])
        column3.append(row[2])

for row in column1:
  row=row.split(':')

print(column1)
print(column2)
print(column3)