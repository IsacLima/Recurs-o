from moduloTabela import *

def busca_recursiva(tabela, chave):
    aux = tabela
    i = 1
    if(not aux.vazia()):
        if(aux.chave[i] != chave):
            aux.excluir(aux.chave[i])
            return i + busca_recursiva(aux, chave)
        return i - 1
    

tabela = Tabela(5)
tabela.inserir('aaa', 1)
tabela.inserir('aab', 2)
tabela.inserir('abb', 3)
tabela.inserir('bbb', 4)
tabela.inserir('bab', 5)
print(busca_recursiva(tabela, 'bbb'))