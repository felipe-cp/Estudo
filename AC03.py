# Felipe Carvalho Pereira
# E-mail: felipe.cpereira92@gmail.com
# Disciplina: Estrutura de dados
# Professor: Jorge Carlos Valverde Rebaza
# Turma: Banco de dados - Noite - 3° semestre
# Atividade contínua 3 - Ranking de Algoritmos de Ordenação
# Data da entrega: 28/04/2020
import random
import time
from random import randint
###############################################################################################################################################
# Escolhi usar o Google Sheets por curiosidade e foi uma boa experiência para aprender um pouco sobre as APIs do Google.
# O arquivo JSON é a chave gerada para que possam ser realizadas alterações através do Python na planilha. 
# Link da planilha com os resultados: https://docs.google.com/spreadsheets/d/1YqBmA3ibRtJra9YuyGijX8S1DFAWm-KlrUlkrZ9Mmf4/
import gspread   # -> pip install gspread oauth2client
from oauth2client.service_account import ServiceAccountCredentials
#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']
#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\User\Desktop\Felipe - AC03\py-sheets-275514-96fea579be18.json', scope)
gc = gspread.authorize(credentials) #Se autentica com conta de serviço
wks = gc.open_by_key('1YqBmA3ibRtJra9YuyGijX8S1DFAWm-KlrUlkrZ9Mmf4') #Abre a planilha usando o ID do arquivo como referencia
worksheet = wks.get_worksheet(0) #Seleciona a primeira página da planilha
###############################################################################################################################################
# Criando a classe Ordenacao que receberá os algoritmos de ordenação
class Ordenacao:     
    def __init__(self, lista):
        self.lista = lista
    
    def bubble_sort(self, lista):     # Usando o algoritmo bubble sort para ordenar a lista 
        n = len(lista)
        for i in range(n):
            ordenado = True
            for j in range(n - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    ordenado = False
            if ordenado:
                break
        return lista

    def merge_sort(self, lista):       # Usando o algoritmo mergesort para ordenar a lista
        if len(lista) < 2:
            return lista
        centro = len(lista) // 2
        lista_L = self.merge_sort(lista[:centro])       # Foi interessante esse algoritmo para entender melhor o conceito de recursividade
        lista_R = self.merge_sort(lista[centro:]) 
        return self.merge(lista_L, lista_R)
    
    def merge(self, lista_L, lista_R):      # Usando o algoritmo mergesort para ordenar a lista
        if len(lista_L) == 0:
            return lista_R
        if len(lista_R) == 0:
            return lista_L
        result = []
        index_L = index_R = 0
        while len(result) < len(lista_L) + len(lista_R):
            if lista_L[index_L] <= lista_R[index_R]:
                result.append(lista_L[index_L])
                index_L += 1
            else:
                result.append(lista_R[index_R])
                index_R += 1
            if index_R == len(lista_R):
                result += lista_L[index_L:]
                break
            if index_L == len(lista_L):
                result += lista_R[index_R:]
                break
        return result
    
    def InsertionSort(self, nlist):             # Usando o algoritmo Insertion Sort para ordenar a lista
        for index in range(1,len(nlist)):
            currentvalue = nlist[index]
            position = index
            while position>0 and nlist[position-1]>currentvalue:
                nlist[position]=nlist[position-1]
                position = position-1
            nlist[position]=currentvalue
        return nlist
    
    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end
        while True:
            while low <= high and array[high] >= pivot:
                high = high - 1
            while low <= high and array[low] <= pivot:
                low = low + 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break
        array[start], array[high] = array[high], array[start]
        return high

    def quick_sort(self, lista, inicio, fim):           # Usando o algoritmo quick sort para ordenar a lista
        if inicio >= fim:
            return 
        p = self.partition(lista, inicio, fim)
        self.quick_sort(lista, inicio, p-1)
        self.quick_sort(lista, p+1, fim)
    
    def counting_sort(self, lista, max_val):   # Usando o algoritmo counting sort para ordenar a lista
        m = max_val + 1
        count = [0] * m                  
        for a in lista:
            count[a] += 1             
        i = 0
        for a in range(m):            
            for c in range(count[a]):  
                lista[i] = a
                i += 1
        return lista
###############################################################################################################################################
def criarLista(L, H, tam): # Função para gerar listas aleatórias de tamanho N
    lista = []
    for i in range(tam): 
        lista.append(randint(L, H)) # Gerar numero aleatorio entre L e H e adicionar a lista
    return lista
###############################################################################################################################################
def testarBubble_sort(lista1):   # Função que testa o algoritmo bubble sort e marca o tempo gasto na execução em minutos
    teste = Ordenacao(lista1)
    antes = time.time()         # Inicio da cronometragem 
    teste.bubble_sort(lista1)   # Chamando o algoritmo da classe Ordenacao para a lista aleatória gerada 
    depois = time.time()       # Fim da cronometragem
    result = (depois - antes) / 60   # O tempo de execussão é dado em segundos, é preciso dividir por 60 para converção em minutos
    return result

def m10Bubble_sort (n, soma):            # Função que chama o teste bubble sort 10 vezes para 10 listas diferentes
    for i in range (0,10):       # Laço que garante 10x a execussão do teste
        teste = criarLista(0,n,n)    # Cria uma lista aleatória recebendo N como parâmetro  
        m = testarBubble_sort(teste)   # Atribui o valor do tempo do teste em m
        soma = soma + m                # Acumula os tempos na variavél soma
    media = soma / 10                       # calculando a média dos tempos de execução
    return media
###############################################################################################################################################
def testarMerge_sort(lista1):      # Função que testa o algoritmo merge sort e marca o tempo gasto na execução em minutos
    teste = Ordenacao(lista1)
    antes = time.time()
    teste.merge_sort(lista1)
    depois = time.time()
    result = (depois - antes) / 60
    return result
   
def m10Merge_sort(n, soma):       # Função que chama o teste merge sort 10 vezes para 10 listas diferentes
    for i in range (0,10):
        teste = criarLista(0,n,n)
        m = testarMerge_sort(teste)
        soma = soma + m
    media = soma / 10                     # Calculando a média dos tempos de execução
    return media
###############################################################################################################################################
def testarInsertionSort(lista1):   # Função que testa o algoritmo InsertionSort e marca o tempo gasto na execução em minutos
    teste = Ordenacao(lista1)
    antes = time.time()
    teste.InsertionSort(lista1)
    depois = time.time()
    result = (depois - antes) / 60
    return result
   
def m10InsertionSort(n, soma):            # Função que chama o teste InsertionSort 10 vezes para 10 listas diferentes
    for i in range (0,10):
        teste = criarLista(0,n,n)
        m = testarInsertionSort(teste)
        soma = soma + m
    media = soma / 10                       # calculando a média dos tempos de execução
    return media
###############################################################################################################################################
def testarquick_sort(lista1):   # Função que testa o algoritmo quick sort e marca o tempo gasto na execução em minutos
    teste = Ordenacao(lista1)
    antes = time.time()
    teste.quick_sort(lista1,0,n-1)    # Necessita passar N-1 para não ter problemas com a recursividade do quick sort
    depois = time.time()
    result = (depois - antes) / 60
    return result
    
def m10quick_sort(n, soma):            # Função que chama o teste quick sort 10 vezes para 10 listas diferentes
    for i in range (0,10):
        teste = criarLista(0,n,n)
        m = testarquick_sort(teste)
        soma = soma + m
    media = soma / 10                       # calculando a média dos tempos de execução
    return media
###############################################################################################################################################
def testarcounting_sort(lista1, vMax):   # Função que testa o algoritmo counting sort e marca o tempo gasto na execução em minutos
    teste = Ordenacao(lista1)
    antes = time.time()
    teste.counting_sort(lista1,vMax)  # Nescessário passar o valor maximo da lista como parametro para que o counting sort funcione que é igual ao N global
    depois = time.time()
    result = (depois - antes) / 60
    return result

def m10counting_sort(n, soma):            # Função que chama o teste counting sort 10 vezes para 10 listas diferentes
    for i in range (0,10):
        teste = criarLista(0,n,n)
        m = testarcounting_sort(teste, n)
        soma = soma + m
    media = soma / 10                       # calculando a média dos tempos de execução
    return media
###############################################################################################################################################
# Funções que atualizam a planilha com o valor das médias https://docs.google.com/spreadsheets/d/1YqBmA3ibRtJra9YuyGijX8S1DFAWm-KlrUlkrZ9Mmf4/
def n1000(n,soma):
    worksheet.update_acell('B3', m10Bubble_sort(n,soma))
    worksheet.update_acell('B4', m10Merge_sort(n,soma))
    worksheet.update_acell('B5', m10InsertionSort(n,soma))
    worksheet.update_acell('B6', m10quick_sort(n,soma))
    worksheet.update_acell('B7', m10counting_sort(n,soma))

def n10000(n,soma):
    worksheet.update_acell('C3', m10Bubble_sort(n,soma))
    worksheet.update_acell('C4', m10Merge_sort(n,soma))
    worksheet.update_acell('C5', m10InsertionSort(n,soma))
    worksheet.update_acell('C6', m10quick_sort(n,soma))
    worksheet.update_acell('C7', m10counting_sort(n,soma))

def n100000(n,soma):
    worksheet.update_acell('D3', m10Bubble_sort(n,soma))
    worksheet.update_acell('D4', m10Merge_sort(n,soma))
    worksheet.update_acell('D5', m10InsertionSort(n,soma))
    worksheet.update_acell('D6', m10quick_sort(n,soma))
    worksheet.update_acell('D7', m10counting_sort(n,soma))

def n1000000(n,soma):
    worksheet.update_acell('E3', m10Bubble_sort(n,soma))
    worksheet.update_acell('E4', m10Merge_sort(n,soma))
    worksheet.update_acell('E5', m10InsertionSort(n,soma))
    worksheet.update_acell('E6', m10quick_sort(n,soma))
    worksheet.update_acell('E7', m10counting_sort(n,soma))

def n10000000(n,soma):
    worksheet.update_acell('F3', m10Bubble_sort(n,soma))
    worksheet.update_acell('F4', m10Merge_sort(n,soma))
    worksheet.update_acell('F5', m10InsertionSort(n,soma))
    worksheet.update_acell('F6', m10quick_sort(n,soma))
    worksheet.update_acell('F7', m10counting_sort(n,soma))
###############################################################################################################################################
# Chamando as funções para valores difrentes de N
soma = 0
n = 1000         
n1000(n,soma)
n = 10000         
n10000(n,soma)
n = 100000         
n100000(n,soma)
n = 1000000            
n1000000(n,soma)
n = 10000000         
n10000000(n,soma)
