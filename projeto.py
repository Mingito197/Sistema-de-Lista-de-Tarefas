class Tarefas:
    def __init__(self, nome, descricao, prazo):
        self.nome = nome
        self.descricao = descricao
        self.prazo = prazo
        self.concluida = False

    def detalhes(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"[{status}] Nome: {self.nome}, Descrição: {self.descricao}, Prazo: {self.prazo}"
    
class GerenciadorTarefas:
    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.lista_tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.nome}' adicionada.")
        
    
    def listar_tarefas(self):
        if not self.lista_tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(self.lista_tarefas, start=1):
                print(f"{i}: {tarefa.detalhes()}")
        
    def marcar_concluida(self, nome_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.nome == nome_tarefa:
                tarefa.concluida = True
                print(f"Tarefa '{tarefa.nome}' concluida.")
                return
        print(f"Tarefa '{nome_tarefa}' não encontrada.") 


    def listar_tarefas_concluidas(self):
        concluidas = [tarefa for tarefa in self.lista_tarefas if tarefa.concluida]
        if not concluidas:
            print("Nenhuma tarefa concluida.")
        else:
            for i, tarefa in enumerate(concluidas, start=1):
                print(f"{i}: {tarefa.detalhes()}")
    
    def listar_pendentes(self):
        pendentes = [tarefa for tarefa in self.lista_tarefas if not tarefa.concluida]
        if not pendentes:
            print("Nenhuma tarefa pendente.")
        else:
            for i, tarefa in enumerate(pendentes, start=1):
                print(f"{i}: {tarefa.detalhes()}")
     
tarefas = GerenciadorTarefas()

def criar_tarefa():
    nome = input("Introduza o nome da tarefa: ")
    descricao = input("Introduza a descrição da tarefa: ")   
    prazo = input("Introduza o prazo da tarefa: ")
    tarefa = Tarefas(nome, descricao, prazo)
    return tarefa

while True:
    escolha = input("O que deseja fazer? \n1 - Criar tarefa \n2 - Listar tarefas \n3 - Marcar tarefa como concluida \n4 - Listar tarefas concluídas \n5 - Listar tarefas pendentes \n6 - Adicionar tarefa \n7 - Visualizar uma tarefa específica \n8 - Sair \n " )
    if escolha == "1":
        tarefa = criar_tarefa()
        tarefas.adicionar_tarefa(tarefa)
        print(tarefa.detalhes())
    elif escolha == "2":
        tarefas.listar_tarefas()
    elif escolha == "3":
        tarefa_concluida = input("Introduza o nome da tarefa a marcar como concluida: ")
        tarefas.marcar_concluida(tarefa_concluida)
    elif escolha == "4":
        tarefas.listar_tarefas_concluidas()
    elif escolha == "5":
        tarefas.listar_pendentes()
    elif escolha == "6":
        tarefa = criar_tarefa()
        tarefas.adicionar_tarefa(tarefa)
    elif escolha == "7":
        tarefa_especifica = input("Introduza o nome da tarefa a visualizar: ")
        for tarefa in tarefas.lista_tarefas:
            if tarefa.nome == tarefa_especifica:
                print(tarefa.detalhes())
                break
        else:
            print(f"Tarefa '{tarefa_especifica}' não encontrada.")
    elif escolha == "8":
        print("A sair do programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")