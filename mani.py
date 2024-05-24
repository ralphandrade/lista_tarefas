# lista de tarefas
tarefas = []

# laço de repetição
while True:
# usuario informa intem da tarefa
    nova_tarefa = input('Informe a nova tarefa ou deixe vazio para encerrar e exibir a lista: ')

# verificase o usuario inseriu nova tarefa
    if nova_tarefa !='':
        tarefas.append(nova_tarefa)
        continue
    else:
        break

print(f'{'-'*25}LISTA DE TAREFAS{'-'*25}\n')

# exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)

