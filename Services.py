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
        self.ulti = None
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

    def remocao(self, codigo): # Remover um nó da fila 
        if self.tamanho == 0:
            print("Fila vazia! Não há voos para remover!") # Se tiver fila vazia
            return 
        
        atual = self.cabeca

        while atual:
            if atual.codigo == codigo:
                if atual.prox:
                    atual.prox.ulti = atual.ulti 
                else:
                    self.cauda = atual.ulti
                    self.cauda.prox = None

                if atual.ulti:
                    atual.ulti.prox = atual.prox
                else:
                    self.cabeca = atual.prox
                    self.cauda.prox = None

                self.tamanho -= 1
                print(f'Voo com código {codigo} removido!') # Encontrado o código na fila
                return
            atual = atual.prox
        print(f'Voo com código {codigo} não encontrado na fila.') # Se não estiver encontrado na fila 




# Ordenação
    def insertion_sort(self, fila):
        noh_ref = self.cauda.ulti
        noh_comparador = self.cauda
        while self.noh_ref.ulti and noh_ref.horario > noh_comparador.horario:
            if noh_comparador.codigo == self.cauda.codigo:
                self.cauda = noh_ref
            #atualização dos ponteiros
            noh_comparador.ulti = noh_ref.ulti
            noh_ref.ulti = noh_comparador
            noh_ref.prox = noh_comparador.prox
            noh_comparador.prox = noh_ref
            # atualização da refetencia
            noh_ref = noh_comparador.ulti
