import requests
import re
import xlwt
from bs4 import BeautifulSoup
#pega a url a ser pesquisada e salva em uma variavel: "endereco"
endereco = str(input("Digite a url: "))
#esse bloco:
#faz a requisicao e salva na variavel:"site"
#coloca o codigo fonte  do site na variavel:"strng_de_teste"
#faz a varredura dos padroes tipo e-mail e os salva como lista na variavel:"padrao_email"
try:
	#Tenta fazer a requisicao
	site = requests.get(endereco)
except:
	#se nao conseguir sai do programa e printa uma mensagem de erro
	print("falha na requisicao")
	exit()
print("Oque deseja procurar:")
print("1.Emails\n2.Imagens/Videos")
opcoes = str(input())
if (opcoes == "1"):
	string_de_teste = site.text
	padrao_email = re.findall(r'[\w\.-]+@[\w-]+\.[\w+\.-]+',string_de_teste)
	x = 0
	#se algum padrao de e-mail for encontrado ele retorna "True"
	#se e o retorno for "True"  cria uma planilha
	#nessa planilha com nome: "simple.xls" salva os e-mails
	if padrao_email:
		#cria a planilha
		workbook = xlwt.Workbook()
		#cria uma folha da planilha 
		worksheet = workbook.add_sheet('Simple')
		# "x" e o numero da linha
		x = 1
		# "y" e o numero da coluna
		y = 0
		# "i" e o indice da lista "Padrao_email"
		i = 0
		worksheet.write(0,0,'E-mail:')
		while True:
			worksheet.write(x,y,padrao_email[i])
			x += 1
			i += 1
			print(i)
			if (i == len(padrao_email)):
				workbook.save('simple.xls')
				exit()
	#se o retorno for "False" e printado a mensagem:"Padrao nao encontrado"
	else:
		print("Padrao nao encontrado")
else:
	soup = BeautifulSoup(site.text, 'html.parser')
	for link in soup.find_all('img'):
		print(link.get('src'))