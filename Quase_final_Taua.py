#PROJETO FILA DE CHEGADAS E Partidas DE UM AEROPORTO

# NOTAS

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
        while noh_ref and noh_ref.mod_horario > noh_comparador.mod_horario:
            #atualização dos valores
            noh_comparador.horario, noh_ref.horario = noh_ref.horario, noh_comparador.horario
            noh_comparador.codigo, noh_ref.codigo = noh_ref.codigo, noh_comparador.codigo
            noh_comparador.destino_origem, noh_ref.destino_origem = noh_ref.destino_origem,  noh_comparador.destino_origem
            noh_comparador.portao, noh_ref.portao = noh_ref.portao, noh_comparador.portao
            noh_comparador.status, noh_ref.status = noh_ref.status, noh_comparador.status
            noh_comparador.mod_horario, noh_ref.mod_horario = noh_ref.mod_horario, noh_comparador.mod_horario
            # atualização da refetencia
            noh_ref, noh_comparador = noh_ref.anterior, noh_ref

# Remoção
    def remocao(self): # Remover um nó da fila 
        codigo = self.cabeca.codigo
        if self.tamanho == 0:
            print("Fila vazia! Não há voos para remover!") # Se tiver fila vazia
            return 
        # O voo que estiver na cabeça da fila será removido
        elif self.cabeca.prox:
            self.cabeca.prox.anterior = None
        else:
            self.cauda = None
        self.cabeca = self.cabeca.prox
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
        # Ordenação
        self.insertion_sort()



    #Busca
    # Como dois voos podem compartilhar o mesmo horario e essa variavel é a forma que eles são ordenados se faz necessario um
    # segundo parametro para a busca
    def busca_binaria(self, codigo, horario, alt_status = False, frente=True, atual= -1, passos=-1):
        if atual == -1 and passos == -1:
            atual = self.cabeca
            passos = self.tamanho // 2
        elif atual == None:
            print('Voo não encontrado, verifique se não houve nenhum erro de digitação')
            return
        for _ in range(passos):
            if frente:
                if not atual.prox:
                    break
                atual = atual.prox
            else:
                if not atual.anterior:
                    break
                atual = atual.anterior
        aux_horas, aux_minutos = horario.split(':')
        aux_horas = int(aux_horas)
        aux_minutos = int(aux_minutos)
        h_aux = (aux_horas*60) + aux_minutos
        if atual.mod_horario == h_aux:
            if atual.codigo == codigo: #Verifica se o voo encontrado não é outro com o mesmo horario
                print(f'Voo {codigo} encontrado.')
                print(f'Status: {atual.status}')
                print(f'Horario: {atual.horario}')
                print(f'Portão: {atual.portao}')
                print(f'destino/origem: {atual.destino_origem}')
                if alt_status:
                    atual.status = input('Alterar para: ')
                return
            else: # Caso seja verifica os proximos voos, pois pela forma de ordenação é onde estarão
                self.busca_binaria(codigo, horario, True,  atual, 1)
        elif atual.mod_horario >  h_aux:
            self.busca_binaria(codigo, horario, alt_status , False, atual.anterior, passos//2)
        else:
            self.busca_binaria(codigo, horario, alt_status, True, atual.prox, passos//2)

# Travessia

    def travessia(self, partidas_chegadas):
        if self.tamanho == 0:
            print('Fila vazia! Não há voos para serem percorridos!')
            return
        # Imprima o cabeçalho da tabela das PARTIDAS
        if partidas_chegadas == 2:
            print("Tabela de PARTIDAS")
            print(f'{"Horário":<10} {"Código":<10} {"Portão":<10} {"Destino":<15} {"Status":<10}')
            print("=" * 60)
            atual = self.cabeca
        # Imprimir informações de cada voo por linha da tabela das PARTIDAS
            while atual:
                print(f'{atual.horario:<10} {atual.codigo:<10} {atual.portao:<10} {atual.destino_origem:<15} {atual.status:<10}')
                atual = atual.prox
            print("=" * 60)
        # Imprimir o cabeçalho da tabela das CHEGADAS
        elif partidas_chegadas == 1:
            print("Tabela de CHEGADAS:")
            print(f'{"Horário":<10} {"Código":<10} {"Portão":<10} {"Origem":<15} {"Status":<10}')
            print("=" * 60)
            atual = self.cabeca
            while atual:
                # Imprimir informações de cada voo por linha da tabela das CHEGADAS   
                print(f'{atual.horario:<10} {atual.codigo:<10} {atual.portao:<10} {atual.destino_origem:<15} {atual.status:<10}')
                atual = atual.prox
            print("=" * 60)
# Imprimir uma tabela que satisfaça as informações do voo nessa ordem:
# Horário
# Código do voo
# Portão de embarque
# Destino 
# Status do voo

def deseja_continuar():
    global rodando
    print('Tecle o correspondente número para executar as seguintes ações:')
    print('1. Continuar')
    print('2. Sair')
    x = input()
    if x == 2:
        rodando = False

def interface():
    global rodando
    print('Bem vindo ao gerenciador de voos!')
    print('Tecle o correspondente número para executar as seguintes ações:')
    print('1. Adicionar voo')
    print('2. Remover voo')
    print('3. Buscar voo')
    print('4. Emitir tabela de voos')
    print('5. Editar Status de voo')
    print('6. Sair')
    comando = int(input())
    if comando == 1:
        print('Tecle o correspondente número para executar as seguintes ações:')
        print('1. Adicionar voo na tabela das chegadas')
        print('2. Adicionar voo na tabela das Partidas')
        comando2 = int(input())
        if comando2 == 1:
            print('Por favor informe:')
            hor = input('Horario previsto de chegada: ')
            cod = input('Codigo do voo: ')
            port = input('Portão: ')
            ori = input('Origem:')
            fila_chegada.insercao(hor, cod, port, ori)
        elif  comando2 == 2:
            print('Por favor informe:')
            hor = input('Horario previsto de saida: ')
            cod = input('Codigo do voo: ')
            port = input('Portão: ')
            ori = input('Destino: ')
            fila_saida.insercao(hor, cod, port, ori)
        else:
            print('Codigo invalido')
        deseja_continuar()
    elif comando == 2:
        print('Tecle o correspondente número para executar as seguintes ações:')
        print('1. remover voo na tabela das chegadas')
        print('2. remover voo na tabela das Partidas')
        comando2 = int(input())
        if comando2 == 1:
            fila_chegada.remocao()
        elif comando2 == 2:
            fila_saida.remocao()
        else:
            print('Codigo invalido')
        deseja_continuar()
    elif comando == 3:
        print('Tecle o correspondente número para executar as seguintes ações:')
        print('1. Buscar voo na tabela das chegadas')
        print('2. Buscar voo na tabela das Partidas')
        comando2 = int(input())
        print('Por favor informe:')
        cod = input('Codigo do voo: ')
        hor = input('Horario do voo:')
        if comando2 == 1:
            fila_chegada.busca_binaria(cod, hor)
        elif comando2 == 2:
            fila_saida.busca_binaria(cod, hor)
        else:
            print('Codigo invalido')
        deseja_continuar()
    elif comando == 4:
        print('Tecle o correspondente número para executar as seguintes ações:')
        print('1. Emitir tabela de chegadas')
        print('2. Emitir tabela de Partidas')
        comando2 = int(input())
        if comando2 == 1:
            fila_chegada.travessia(1)
        elif comando2 == 2:
            fila_saida.travessia(2)
        else:
            print('Codigo invalido')
        deseja_continuar()
    elif comando == 5:
        print('Tecle o correspondente número para executar as seguintes ações:')
        print('1. Editar voo na tabela das chegadas')
        print('2. Editar voo na tabela das Partidas')
        comando2 = int(input())
        print('Por favor informe:')
        cod = input('Codigo do voo: ')
        hor = input('Horario do voo:')
        if comando2 == 1:
            fila_chegada.busca_binaria(cod, hor, True)
        elif comando2 == 2:
            fila_saida.busca_binaria(cod, hor, True)
        else:
            print('Codigo invalido')
        deseja_continuar()
    elif comando == 6:
        rodando = False
        return
    else:
        print('Codigo invalido')
        deseja_continuar()
    return





fila_saida = fila_de_voos()
fila_chegada = fila_de_voos()


rodando = True
while rodando:
    interface()



    

        



