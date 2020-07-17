#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:16:52 2020

@author: bruno
"""

import pandas as pd

df = pd.read_csv("/home/bruno/Downloads/owid-covid-data.csv")

df = df.sort_values(by=["iso_code", "date"])
df = df.drop_duplicates(subset=['iso_code'], keep='last')
df = df.set_index("location",drop='false')

#criar uma função que pegue a tabela e
# o nome do país em inglês com a 1ªletra maiúscula e
#retorna uma tabela com todos os países tendo 
#o número de mortes, testes e casos
#seguindo as taxas do país alvo.

def converte_df (df_base,pais_alvo):
    casos_m = df_base.at[pais_alvo,'total_cases_per_million']
    mortes_m = df_base.at[pais_alvo,'total_deaths_per_million']
    ls = []
    header = ['país','casos','mortes','populacao']
    for name in [x for x in df_base.index]:
        pop = df_base.at[name,'population']
        pop_n = pop/1000000
        ls.append([name,pop_n*casos_m,pop_n*mortes_m,pop])
    df_out = pd.DataFrame(ls[1:],columns=header)
    return df_out
    
    