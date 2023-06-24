"""
Programa: Progressão geométrica
Descrição: Este programa calcula o n-ésimo termo e a soma dos termos de uma PG.
Autor: Filipe
Data: 04/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
n = int(input("Qual a quantidade de termos? "))
a1 = int(input("Qual o primeiro termo? "))
q = int(input("Qual a razão da progressão? "))

#Processamento de dados
an = (a1*(q**(n-1)))
sn = ((a1*((q**n)-1))/(q-1))

#Saida de dados
print(f"O n-ésimo termo é {an}.")
print(f"A soma dos n-ésimos termos é {sn}.")
