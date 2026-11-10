import os
tarefas = []

    
def menu_opcoes():
    os.system('cls')
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')
    

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
 
def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Erro: Digite um número!')
        voltar_ao_menu_principal()
        return
    if opcao < 1 or opcao > 4:
        opcao_invalida()
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        visualizar_tarefas()
    elif opcao == 3:
        remover_tarefas()
    elif opcao == 4:
        sair_do_programa()


        
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção Inválida! Escolha uma opção entre 1 e 4')
    voltar_ao_menu_principal()
    return

        
def adicionar_tarefa():
    exibir_subtitulo('Adicionando uma taréfa: ')
    tarefa = input('Digite a terefa: ')
    if not tarefa.strip():
        print('Erro: A tarefa não pode ficar vazia!')
    else:
        tarefas.append(tarefa)
        print('Tarefa adicionada!')
    voltar_ao_menu_principal()
        
       
def visualizar_tarefas():
    exibir_subtitulo('Lista de tarefas')      
    if not tarefas:
        print('Nenhuma tarefa para visualizar!')
    else:    
        print('Tarefas:') 
        for indice, tarefa in enumerate(tarefas, start=1):
            print (f'{indice}. {tarefa}')
    voltar_ao_menu_principal()
  
def remover_tarefas():
    exibir_subtitulo('Removendo uma tarefa: ') 
    if not tarefas:
        print('Erro: Nenhuma tarefa para remover.')
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f'Tarefas: {indice}. {tarefa}')
        try:
            tarefa_numero = int(input(f'Digite a número da terefa a ser removida: '))
        except ValueError:
            print('Erro: Digite um número!')
            voltar_ao_menu_principal()
            return
        if 1 <= tarefa_numero <= len(tarefas):
            remover_tarefa = tarefas.pop(tarefa_numero -1) 
            print(f'Tarefa: {remover_tarefa} removida!')
            voltar_ao_menu_principal()
        else:
            print('Número da tarefa inválido!')
            voltar_ao_menu_principal()
        
def sair_do_programa():
    print('Saindo do gerenciador de tarefas. Até mais!')
    
def main():
    os.system('cls')
    menu_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()
    
