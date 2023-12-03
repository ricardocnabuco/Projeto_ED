#PROJETO FILA DE CHEGADAS E SAIDAS DE UM AEROPORTO

# NOTAS
# 0.1: INPLEMENTAÇÃO BASICA DE NO E LISTA DUPLAMENTE ENCADEADA

class voo:
    def __init__(self, horario,  codigo, portao, destino_origem):
        #Informações do voo
        self.horario = horario
        self.status = 'Previsto'
        self.destino_origem = destino_origem
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
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

# Ordenação
    def insertion_sort(self):
        noh_ref = self.cauda.anterior
        noh_comparador = self.cauda
        while noh_ref.anterior and noh_ref.horario > noh_comparador.horario:
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
    def remocao(self): # Remover um nó da fila 
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
    def insercao(self, horario,  codigo, portao, destino_origem): # adicionar um no
        self.tamanho += 1
        novo_voo = voo(horario,  codigo, portao, destino_origem)
        if not self.cabeca:
            self.cabeca = novo_voo
            self.cauda = novo_voo
            return
        self.cauda.prox = novo_voo
        novo_voo.anterior = self.cauda
        self.cauda = novo_voo


    #Busca
    # Como dois voos podem compartilhar o mesmo horario e essa variavel é a forma que eles são ordenados se faz necessario um
    # segundo parametro para a busca
    def busca_binaria(self, codigo, horario, atual= -1, passos=-1):
        aux_horas, aux_minutos = horario.split(':')
        aux_horas = int(aux_horas)
        aux_minutos = int(aux_minutos)
        h_aux = (aux_horas*60) + aux_minutos
        if atual == -1 and passos == -1:
            atual = self.cabeca
            passos = self.tamanho // 2
        elif atual == None:
            print('Voo não encontrado, verifique se não houve nenhum erro de digitação')
            return
        elif passos == 0:
            passos += 1
        for _ in range(passos):
            atual = atual.prox
        if atual.mod_horario == h_aux:
            if atual.codigo == codigo: #Verifica se o voo encontrado não é outro com o mesmo horario
                print(f'Voo {codigo} encontrado.')
                print(f'Status: {atual.status}')
                print(f'Horario: {atual.horario}')
                print(f'Portão: {atual.portao}')
                print(f'destino/origem: {atual.destino_origem}')
                return
            else: # Caso seja verifica os proximos voos, pois pela forma de ordenação é onde estarão
                self.busca_binaria(codigo, horario, atual, 1)
        elif atual.mod_horario >  h_aux:
            self.busca_binaria(codigo, horario, self.cabeca, passos//2)
        else:
            self.busca_binaria(codigo, horario, atual, passos//2)

# Travessia

    def travessia(self):
        if self.tamanho == 0:
            print('Fila vazia! Não há voos para serem percorridos!')
            return
        # Imprima o cabeçalho da tabela das PARTIDAS 
        print("Tabela de PARTIDAS")
        print(f'{"Horário":<10} {"Código":<10} {"Portão":<10} {"Destino":<15} {"Status":<10}')
        print("=" * 60)
        atual = self.cabeca
        # Imprimir informações de cada voo por linha da tabela das PARTIDAS
        while atual:
            if not atual.chegando: 
                print(f'{atual.horario:<10} {atual.codigo:<10} {atual.portao:<10} {atual.destino:<15} {atual.status:<10}')
            atual = atual.prox
        print("\n" + "=" * 60)
        # Imprimir o cabeçalho da tabela das CHEGADAS 
        print("\nTabela de Chegadas:")
        print(f'{"Horário":<10} {"Código":<10} {"Portão":<10} {"Origem":<15} {"Status":<10}')
        print("=" * 60)
        atual = self.cabeca
        while atual:
            # Imprimir informações de cada voo por linha da tabela das CHEGADAS
            if atual.chegando:
                print(f'{atual.horario:<10} {atual.codigo:<10} {atual.portao:<10} {atual.destino:<15} {atual.status:<10}')
            atual = atual.prox
# Imprimir uma tabela que satisfaça as informações do voo nessa ordem:
# Horário
# Código do voo
# Portão de embarque
# Destino 
# Status do voo