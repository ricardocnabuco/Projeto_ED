#PROJETO FILA DE CHEGADAS E SAIDAS DE UM AEROPORTO

# NOTAS
# 0.1: INPLEMENTAÇÃO BASICA DE NO E LISTA DUPLAMENTE ENCADEADA

class voo:
    def __init__(self, horario, destino, chegando, codigo):
        #Informações do voo
        self.horario = horario
        self.status = 'Previto'
        self.destino = destino
        self.chegando = chegando
        self.codigo = codigo
        #Ponteiros
        self.prox = None
        self.ulti = None

class fila_de_voos:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def remover_voo_por_codigo(self, codigo):
        if self.tamanho == 0:
            print("Fila vazia! Não há voos para remover!")
            return 
        
        atual = self.cabeca

        while atual:
            if atual.codigo == codigo:
                if atual.prox:
                    atual.prox.ulti = atual.ulti 
                else:
                    self.cauda = atual.ulti

                if atual.ulti:
                    atual.ulti.prox = atual.prox
                else:
                    self.cabeca = atual.prox
                
                self.tamanho -= 1
                print(f'Voo com código {codigo} removido!')
                return
            atual = atual.prox
        print(f'Voo com código {codigo} não encontrado na fila.')




# Ordenação
    def insertion_sort(self, fila):
        for _ in range(self.tamanho):
            noh_ref = self.cabeca
            noh_comparador = self.cabeca.prox
            ancora = noh_comparador.prox
            while self.noh_ref.ulti and noh_ref.horario > noh_comparador.horario
                #atualização dos ponteiros
                noh_comparador.ulti = noh_ref.ulti
                noh_ref.ulti = noh_comparador
                noh_ref.prox = noh_comparador.prox
                noh_comparador.prox = noh_ref
                # atualização da refetencia
                noh_ref = nof_comparador.ulti
            # atualização do elemento a ser ordenado
            noh_comparador = ancora 
