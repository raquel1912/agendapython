#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:42:33 2021

@author: raquel
""" 
import os
import time
import json


#cadastrando 1 aluno
def cadastrar():
    nome = input('Digite seu nome: ') 
    telefone = input('Digite seu numero: ')
    sexo = input('Digite seu sexo: ') 
    idade = input('Digite sua idade: ')
    agenda = open("agenda","r+")
    dados = json.load(agenda)
    dados.append({
    'Nome': nome,
    'Telefone': telefone,
    'Sexo': sexo,
    'Idade': idade
    })
    agenda.seek(0)
    json.dump(dados, agenda)
def pesquisar():
    print('pesquisar')
def excluir():
    print('excluir')
def listar():
   agenda = open("agenda", "r")
   dados = json.load(agenda)
   for aluno in dados:
       print(aluno['Nome'])
       print(aluno['Telefone'])
       print(aluno['Sexo'])
       print(aluno['Idade'])
       print('')
       
             
       
#menu de opcoes
os.system('clear')
while (0==0):
    print ("""
    1.Cadastrar um aluno
    2.Pesquisar um aluno
    3.Excluir
    4.Listar
    0.Sair
    """)
    opcao = input('opcao: ')
    if(opcao=='0'):
        break
    elif(opcao=='1'):
       cadastrar()
    elif(opcao=='2'):
       pesquisar()
    elif(opcao=='3'):
        excluir()
    elif(opcao=='4'):
        listar()
    
    else:
        print('opcao invalida')
    time.sleep(6.4)
    os.system('clear')
       
       
       
       
