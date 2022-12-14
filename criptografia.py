#Vamos escrver um pequeno script para criptografia em Python.

#*********************************************************************************************
#
#
#
#
#0:Importando bibliotecas
import random





#*********************************************************************************************
#
#
#
#
#1:Lendo conteúdo de um arquivo
try:
 with open('mensagem_secreta.txt') as arquivo: #O nome do arquivo pode ser alterado ao usar este script
  conteudo=' '.join(arquivo.readlines())
except IOError:
 print('Erro ao ler o arquivo contendo a mensagem a ser cifrada.')

'''Módulo de teste da leitura do arquivo, use um # após o teste.'''
#print(conteudo)

#*********************************************************************************************
#
#
#
#
#2: Criando uma lista de caracteres, um arquivo para estocar a mensagem de ser criptografada, outro para estocar a chave da criptografia e uma chave que irá ser usado na criptografia

caracteres='qwertyuiopasdfghjklçzxcvbnm,.;+-*/0123456789QWERTYUIOPASDFGHJKLÇZXCVBNM´`^~{}()!@#$%*()_:><|?ºª¹²³£¢"áéíóúàâêîôû'
lista_de_caracteres1=list(caracteres)

'''Módulo teste de lista de caractéres, use um # após o teste'''
#print('lista de caracteres1')
#print(lista_de_caracteres1)
#print(len(lista_de_caracteres1))


#Arquivo para guardar a chave de criptografia
chave_arquivo=open('chave.txt', 'w')
criptografia_arquivo=open('mensagem_criptograda.txt', 'w')




#*********************************************************************************************
#
#
#
#
#3: Criação da chave de criptografia e registro da mesma em um arquivo:

numero_chave=random.randint(100, len(lista_de_caracteres1)) #Parâmetro ajustável

#Reordenando os elementos da lista e criando uma chave de criptografia
chave_lista:list=[]
for i in range(numero_chave+1):
 numero=random.randint(0, len(lista_de_caracteres1)-1)
 if(lista_de_caracteres1[numero] not in chave_lista):
  chave_lista.append(lista_de_caracteres1[numero])

chave_lista=chave_lista #Atualizando a chave da criptografia

chave_secreta:str=' '.join(chave_lista)
chave_arquivo.write(chave_secreta)
chave_arquivo.close()

'''Módulo de teste de criação de uma chave secreta, use um # após o teste'''
#print('chave lista')
#print(chave_lista)
#print(len(chave_lista))
#print('chave secreta')
#print(chave_secreta)
#print(len(chave_secreta))


#*********************************************************************************************
#
#
#
#
#4: Criptografando a mensagem e registrando em um arquivo
j:int=0 #Contador

x:str=str(conteudo)
while(j<len(chave_lista)-1):
 x=x.replace(str(lista_de_caracteres1[j]), str(chave_lista[j]))
 conteudo=x
 j=j+1
conteudo_criptografado:str=str(x)
criptografia_arquivo.write(conteudo_criptografado)
criptografia_arquivo.close()

'''Módulo de teste da criptografia'''
#print(conteudo_criptografado)






