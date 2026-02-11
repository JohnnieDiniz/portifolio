def to_do():
    # 1. Criar as 3 listas (prateleiras do Kanban)
    alta = []
    media = []
    baixa = []
    
    # 2. Contador de IDs (começa em 1)
    proximo_id = 1
    
    print("=== SISTEMA DE TAREFAS ===")
    print("Cadastre uma nova tarefa:")
    print("-" * 30)
    
    # 3. Perguntar prioridade ao usuário
    # (USE .lower() para padronizar!)
    prioridade = input("Prioridade (alta/média/baixa): ").strip().lower()