#PROJETO FILA DE CHEGADAS E SAIDAS DE UM AEROPORTO

# NOTAS
# 0.1: INPLEMENTAÇÃO BASICA DE NO E LISTA DUPLAMENTE ENCADEADA

class voo:
    def __init__(self, horario,  codigo, portao, destino=None):
        #Informações do voo
        self.horario = horario
        self.status = 'Previto'
        self.destino = destino
        self.codigo = codigo
        self.portao = portao
        #Ponteiros
        self.prox = None
        self.anterior = None
        #modulo do horario
        horas, minutos = self.horario.split(':')
        horas = int(horas)
        minutos = int(minutos)
        self.mod_horario = (horas*60) + minutos

class fila_de_voos:
    def __init__(self, tipo):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        self.tipo = tipo

# Ordenação
    def insertion_sort(self, fila):
        noh_ref = self.cauda.anterior
        noh_comparador = self.cauda
        while self.noh_ref.anterior and noh_ref.horario > noh_comparador.horario:
            if noh_comparador.codigo == self.cauda.codigo:
                self.cauda = noh_ref
            #atualização dos ponteiros
            noh_comparador.anterior = noh_ref.anterior
            noh_ref.anterior = noh_comparador
            noh_ref.prox = noh_comparador.prox
            noh_comparador.prox = noh_ref
            # atualização da refetencia
            noh_ref = noh_comparador.anterior

# Remoção
    def remocao(self, codigo): # Remover um nó da fila 
        if self.tamanho == 0:
            print("Fila vazia! Não há voos para remover!") # Se tiver fila vazia
            return 
        atual = self.cabeca
        # O voo que estiver na cabeça da fila será removido
        if atual.codigo == codigo: 
            self.cabeca = atual.prox
            if self.cabeca:
                self.cabeca.anterior = None
            else:
                self.cauda = None
            self.tamanho -= 1
            print(f'Voo com código {codigo} removido!')

# Insercao
    def insercao(self, horario,  codigo, portao, destino=None): # adicionar um no
        self.tamanho += 1
        novo_voo = voo(horario,  codigo, portao, destino=None)
        if not self.cabeca:
            self.cabeca = novo_voo
            self.cauda = novo_voo
            return
        self.cauda.prox = novo_voo
        novo_voo.anterior = self.cauda
        self.cauda = novo_voo