import networkx as nx



########## TODO

# PROJETO CENTRAL
#
# 1) FUNÇÕES BÁSICAS
# 2) WINDOW
# 3) RECEITAS E COMPLEXIDADE DE PRODUÇÃO
# ) AGENTES ECONÔMICOS E TERRENO, NECESSIDADES E DISPONIBILIDADES
# ) TEMPO E EVOLUÇÃO DA COMPLEXIDADE
# ) EFEITOS DOS PRODUTOS E ESTADOS
# ) VIOLÊNCIA E CONTROLE
# ) IA E MENTE (FUTURO) E COMPLEXIDADE DE
# ) INOVAÇÃO E ALEATORIEDADE
# ) IMPLEMENTAÇÃO DAS CIÊNCIAS NATURAIS
# )
# )
# )
# )
# )
# )
# )
# )
# )


# 1)a) posse, transferir, mudar, checagens\
# b) receita, realizar, checagens

# 2) a) desenhar e mover o grafo
# b) add funcionalidades de 1) na janela
# c) queue de eventos e pass turn
# d) fixar um queue de receitas
#

###



# Caracteristicas_dos_Pontos = ["produção", "Consumo", "posse"]

class Material_Rotulo:
    def __init__(self, Nome, Graph):
        self.Nome = Nome
        self.Graph = Graph
        self.rotulo = {}
        self.iniciar_rotulo()

    def iniciar_rotulo(self):
        for ponto in self.Graph.nodes:
            self.rotulo[ponto] = {"posse":0}
        for seta in self.Graph.edges:
            self.rotulo[seta] = {'transf':0}

    def Rotulo_Pontos(self):
        retu  = {}
        for node in self.Graph.nodes:
            retu[node] = self.rotulo[node]["posse"]
        return retu

    def Rotulo_Setas(self):
        retu = {}
        for seta in self.Graph.edges:
            retu[seta]=self.rotulo[seta]["transf"]
        return retu

    def Checar_Transferabilidade(self, seta):
        if self.rotulo[seta[0]]["posse"] >= self.rotulo[seta]["transf"]:
            return True
        return False

    def mudar_posse_ponto(self, ponto, quantidade):
        if ponto in self.Graph.nodes:
            self.rotulo[ponto]["posse"]+=quantidade

    def mudar_posse_pontos(self, quantidade):
        for ponto in self.Graph.nodes:
            self.rotulo[ponto]["posse"]+=quantidade

    def mudar_transferencia_seta(self, seta, x):
        if seta in self.Graph.edges:
            if self.rotulo[seta]["transf"]+x <= self.rotulo[seta[0]]["posse"]:
                self.rotulo[seta]["transf"] += x

    def transferir_seta(self, seta):
        self.mudar_posse_ponto(seta[0], -self.rotulo[seta]["transf"])
        self.mudar_posse_ponto(seta[1], self.rotulo[seta]["transf"])
        self.rotulo[seta]["transf"]=0

    def transferencia_global(self):
        viagem = {}
        for seta in self.Graph.edges:
            viagem[seta] = min(self.rotulo[seta[0]]["posse"], self.rotulo[seta])
            quantidade = min(self.rotulo[seta[0]]["posse"], self.rotulo[seta])
            self.rotulo[seta[0]]["posse"]-=quantidade
            self.rotulo[seta]-=quantidade
        for seta in self.Graph.edges:
            self.rotulo[seta[1]]["posse"]+=viagem[seta]

        #     quantidade_para_transferir = min(self.rotulo[seta[0]], self.rotulo[seta])
        #     if self.rotulo[seta]>self.rotulo[seta[0]][1]:
        #         self.rotulo[seta[0]][1]=0
        #     else:    self.rotulo.seta[0][1]-=self.rotulo[seta]
        # self.rotulo[seta[1]][1]+=quantidade_para_transferir

    def Maximizar_Transferencia(self, seta):
        if seta in self.Graph.edges:
            self.mudar_transferencia_seta(seta, self.rotulo[seta[0]]["posse"])

    def Maximizar_Todas_Transferencias(self):
        for seta in self.Graph.edges:
            self.Maximizar_Transferencia(seta)

    # def Adicionar_Ponto(self, ponto):
    #     self.rotulo[ponto]["posse"]=0
    # def Adicionar_seta(self, seta):
    #     self.rotulo[seta]["transf"]=0

    def Crescer_Agentes(self, ponto):
        X.add_node(ponto)
        self.rotulo[ponto] = {"posse": 0}

    def Construir_diVia(self, seta):
        X.add_seta(seta)
        self.rotulo[seta] = {"transf": 0}

class Receita_Materiais:

    def __init__(self, Nome, Insumos, Produtos, Agente):
        self.Nome = Nome
        self.Insumos=Insumos
        self.Produtos=Produtos
        # self.Agente=Agente
        #Insumos = dicio{material:quantidade}
        #Produtos tambem
        #funciona tambem como dicio{nome:quantidade}

    def Checar_Disponibilidade(self, Ponto):
        for Material in self.Insumos:
            if Material.rotulo[Ponto]["posse"]<self.Insumos[Material]:
                print("nop")
                return False
        return True

    def Checar_Disponibilidade_Pontos(self, Pontos):
        pass

    def Realizar_Receita(self, Ponto):
        if self.Checar_Disponibilidade(Ponto)==True:
            for Material in self.Insumos:
                Material.rotulo[Ponto]["posse"]-=self.Insumos[Material]
            for Material in self.Produtos:
                Material.rotulo[Ponto]["posse"]+=self.Produtos[Material]
        else: pass

    def Realizar_Receita_Pontos(self, Pontos):o,
        pass


class Uso:
    def __init__(self, Materiais, Efeitos, Condicoes):
        self.Materiais=Materiais
        self.Efeitos=Efeitos
        self.Condicoes=Condicoes








#INICIALIZAÇÃO

#inicializar grafo
X = nx.DiGraph()
edg = [(i,i+1) for i in range(0, 4)]
X.add_edges_from(edg)
# print(X.nodes)
# print(X.edges)


#INICIALIZAR MATERIAIS
Materiais = []
Comida = Material_Rotulo("Comida", X)
Materiais.append(Comida)
Expandir=Uso([Comida], "criar agente economico", "nenhuma")
Expandir.Crescer = Expandir.Materiais[0].Crescer_Agentes
Expandir.Construir = Expandir.Materiais[0].Construir_diVia
# for Ponto in X.nodes:
#     print([Ponto, Comida.rotulo[Ponto]])
# Ponto = Material_Rotulo("População", X)


#INICIALIZAR RECEITAS
Receitas=[]
Lavoura = Receita_Materiais("Lavoura", {Comida:1}, {Comida:2}, [])
Receitas.append(Lavoura)
# Sequencia_Receitas=[]



#EVENTOS
Comida.mudar_posse_pontos(1)



#TESTES
# print(X.nodes)
# print(Comida.rotulo[1]["posse"])
# Comida.Crescer_Agentes(5)
# print(X.nodes)
# print(Comida.Rotulo_Pontos())
# print(Comida.Rotulo_Setas())

# JOGO
# Expandir.Crescer(5)
# Comida.Crescer_Agentes(5)
tempo = 0
while tempo < 50:
    print(Comida.Rotulo_Pontos())
    print(Comida.Rotulo_Setas())
    c1 = input("digite coisa pra fazer ")
    c2 = input("digite coisa pra fazer ")
    c3 = input("digite coisa pra fazer ")
    lista=[c1, c2, c3]
    for i in range(0, 3):
        if len(lista[i])==1:
            if lista[i] in X.nodes:
                Lavoura.Realizar_Receita(int(lista[i]))
            else: Expandir.Crescer(int(lista[i]))
        elif len(lista[i])==3:
            Comida.mudar_transferencia_seta((int(lista[i][0]), int(lista[i][2])) ,1)
            Comida.transferir_seta((int(lista[i][0]), int(lista[i][2])))
            # Comida.transferencia_global()
    tempo+=1


















###

    #LIXO DA CLASSE MATERIAL_ROTULO
    # def mudar_quantidade_ponto(self, ponto, quantidade):
    #     if ponto in self.Graph.nodes:
    #         self.rotulo[ponto]["posse"]+=quantidade

    # def produzir_ponto(self, ponto):
    #     self.rotulo[ponto]["posse"] += self.rotulo[ponto][0]
    #     self.rotulo[ponto][0]=0

    # def mudar_producao_ponto(self, ponto, quantidade):
    #     if ponto in self.Graph.nodes:
    #         self.rotulo[ponto]["Produção"]+=quantidade
    #
    # def mudar_consumo_ponto(self, ponto, quantidade):
    #     if ponto in self.Graph.nodes:
    #         self.rotulo[ponto]["posse"]+=quantidade
    #
    # def Mudar_Todos_Consumos(self, quantidade):
    #     for ponto in self.Graph.nodes:
    #         self.rotulo[ponto]["posse"]+=quantidade

    # def consumir_ponto(self, ponto):
    #     self.rotulo[ponto]["posse"]-=self.rotulo[ponto]["posse"]
    #     self.rotulo[ponto]["posse"]=0
    #     if self.rotulo[ponto]["posse"]<0:
    #         self.rotulo[ponto]["posse"]=0

    # def iterar_tempo(self):
    #     self.transferencia_global()
    #     for ponto in self.Graph.nodes:
    #         self.consumir_ponto(ponto)
    #     for ponto in self.Graph.nodes:
    #         self.produzir_ponto(ponto)

    # def transferir_seta(self, seta):
    #     if self.check_transferabilidade(seta) == True:
    #         self.mudar_rotuloponto(seta[0][""], [0, -self.rotulo[seta]])
    #         self.mudar_rotuloponto(seta[1], [0, self.rotulo[seta]])
    #         self.rotulo[seta] = 0
    #     else:
    #         self.mudar_rotuloponto(seta[0], [0, -self.rotulo[seta[0]]["posse"]])
    #         self.mudar_rotuloponto(seta[1], [0, self.rotulo[seta[0]]["posse"]])
    #         self.rotulo[seta] -= self.rotulo[seta[0]]["posse"]

###







