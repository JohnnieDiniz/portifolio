def cadastro_atividade():
    alta = []
    medio = []
    baixo = []
    proximo_id = 1
    
    opcao = None
    
    while opcao != 0:
        print('''
    [1] - Cadastrar nova tarefa
    [2] - Listar as tarefas
    [3] - Sair do Programa
        ''')
        
        try:
            opcao = input('Qual é sua opção? ').strip()
            opcao = int(opcao)
        except ValueError:
            print('Digite uma opção válida!')
            continue
        
        if opcao == 1:
            descricao = input('Qual tarefa deseja adicionar? ').strip()
            prioridade = input('Prioridade (alta/media/baixa): ').strip().lower()
            
            tarefa = {
                'id': proximo_id,
                'descricao': descricao,
                'prioridade': prioridade
            }
            
            proximo_id += 1
            
            if prioridade == 'alta':
                alta.append(tarefa)
            elif prioridade == 'media':
                medio.append(tarefa)
            elif prioridade == 'baixa':
                baixo.append(tarefa)
            else:
                print('Prioridade inválida! Tarefa não cadastrada.')
                
        elif opcao == 2:
            print('\n--- TAREFAS CADASTRADAS ---')
            print(f'ALTA: {alta}')
            print(f'MÉDIA: {medio}')
            print(f'BAIXA: {baixo}')
            
        elif opcao == 3:
            print('Saindo do programa...')
            opcao = 0
        else:
            print('Opção inválida! Digite 1, 2 ou 3.')
    
    print('Programa encerrado.')

# Chamar a função
cadastro_atividade()