import networkx as nx
import pygame as pyg
import math

###notation
#math.sin and math.cos in radians


####TODO
#blitar um grafo dado
#moverponto


print(math.pi)
tamanho_ponto = (10, 10)
centro=(300,300)
raio=250
cor_branca = (255, 255, 255)
cor_azul = (108, 194, 236)
cor_verde = (152, 231, 114)
cor_preta=(0,0,0)



def soma_posicoes(pos1, pos2):
    return (pos1[0]+pos2[0], pos1[1]+pos2[1])
def Posicoes_Pontos(n):
    posicoes=[]
    m=0
    while m<n:
        posicoes.append(soma_posicoes(centro, (math.floor(raio*math.cos(m*2*math.pi/n)),
                                      math.floor(raio*math.sin(m*2*math.pi/n)))))
        m+=1
    return posicoes




def main():
    #Definições dos objetos(variaveis)
    pyg.init()
    tela = pyg.display.set_mode([600, 600])
    tela1= pyg.Surface((600,600))
    tela1.fill(cor_preta)
    tela.blit(tela1, (0,0))
    pyg.display.set_caption("iniciando com pygame")
    sup = pyg.Surface(tamanho_ponto)
    sup.fill(cor_preta)
    relogio = pyg.time.Clock()
    # numero_pontos=int(input("digite um número de pontos "))
    numero_pontos=16
    posicoes=Posicoes_Pontos(numero_pontos)



    sair = False
    while sair != True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                sair = True
            # if event.type == pyg.MOUSEBUTTONDOWN:
            #     ret = ret.move((10, 10))
        relogio.tick(27)
        tela.fill(cor_branca)
        # tela.blit(sup, soma_posicoes(centro, (raio, 0)))
        m = 0
        while m < len(posicoes):
            sup = pyg.Surface(tamanho_ponto)
            sup.fill(cor_preta)
            tela.blit(sup, posicoes[m])
            m+=1
        # pyg.draw.lines(tela, cor_preta, True, [(200,200), (300, 300), (400,400)], 3)
        pyg.draw.lines(tela, cor_preta, True, Posicoes_Pontos(16), 3)
        # tela.blit(linha)
        # tela.blit(sup2, (200, 200))
        # tela.blit(sup, ret)
        pyg.display.update()
    pyg.quit()




    # pyg.init()
    # tela = pyg.display.set_mode([300, 300])
    # pyg.display.set_caption("iniciando com pygame")
    # relogio = pyg.time.Clock()
    #
    # sair = False
    # while sair != True:
    #     for event in pyg.event.get():
    #         if event.type == pyg.QUIT:
    #             sair = True
    #     relogio.tick(27)
    #
    #     pyg.display.update()
    # pyg.quit()





main()























############LIXO

# class Hypergraph:
#
#     def __init__(self, Nodes, Hyperedges, Raw, Product):
#         self.Nodes = Nodes
#         self.Hyperedges = Hyperedges
#         self.Raw = Raw
#         self.Product = Product
#
#     def Get_Outdegree(self, node):
#         i = 0
#         for hyperedge in self.Hyperedges:
#             if node in self.Raw[hyperedge]:
#                 i += 1
#         return i
#
#     def Get_InDegree(self, node):
#         i = 0
#         for hyperedge in self.Hyperedges:
#             if node in self.Product[hyperedge]:
#                 i += 1
#         return i

