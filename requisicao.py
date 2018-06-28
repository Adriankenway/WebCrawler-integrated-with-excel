import requests
import re
import xlwt

endereco = str(input("Digite a url: "))

site = requests.get(endereco)
string_de_teste = site.text
padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w+\.-]+',string_de_teste)

x = 0
if padrao_email:
	workbook = xlwt.Workbook()
	worksheet = workbook.add_sheet('Simple')
	x = 1
	y = 0
	i = 0
	worksheet.write(0,0,'E-mail:')
	while True:
		worksheet.write(x,y,padrao_email[i])
		x += 1
		i += 1
		print(x)
		if (i == len(padrao_email)):
			workbook.save('simple.xls')
			exit()
else:
	print("Padrao nao encontrado")