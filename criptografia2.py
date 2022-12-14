#Vamos escrever um program que decriptografa mensagens registradas com o programa criptografia.py  

#*********************************************************************************************
#
#
#
#
#0: Lendo os arquivos com a mensagem criptografada e com chave

try:
 with open('mensagem_criptograda.txt') as arquivo: #O nome do arquivo pode ser alterado ao usar este script
  conteudo=' '.join(arquivo.readlines())
except IOError:
 print('Erro ao ler o arquivo contendo a mensagem a ser cifrada.')

print('A mensagem cifrada.')
print(conteudo)

try:
 with open('chave.txt') as arquivo2: #O nome do arquivo pode ser alterado ao usar este script
  chave=' '.join(arquivo2.readlines())
  chave_temp=list(chave)
  chave_lista=[x for x in chave_temp if x!=' ']
except IOError:
 print('Erro ao ler o arquivo contendo a mensagem a ser cifrada.')

'''Módulo de teste da chave, use um # após o teste'''
#print('chave_lista')
#print(len(chave_lista))
#print(chave_lista)


#*********************************************************************************************
#
#
#
#
#2: Decifrando a mensagem secreta 

#Lista de caractéres usados na criptografia
caracteres='qwertyuiopasdfghjklçzxcvbnm,.;+-*/0123456789QWERTYUIOPASDFGHJKLÇZXCVBNM´`^~{}()!@#$%*()_:><|?ºª¹²³£¢"áéíóúàâêîôû'
lista_de_caracteres1=list(caracteres)


print('Use a seguinte lista de correlações para decriptografar a mensagem secreta.')
for i in range(len(chave_lista)):
 print('%s --> %s'%(chave_lista[i], lista_de_caracteres1[i]))




