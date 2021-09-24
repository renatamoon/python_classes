#faça uma lista de tarefas com as seguintes opções:
'''adicionar tarefa
listar tarefas
opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
opção de refazer (a cada vez que chamarmos, refaz a ultima ação
'''

def show_op(to_do_list):
    print("=*"*5)
    print('Tarefas: ')
    print(todo_list)
    print("=*"*5)

def do_add(todo, todo_list):
    todo_list.append(todo)

def do_undo(todo_list, redo_list):
    if not todo_list:
        print('nada a desfazer')
        return
    last_todo = todo_list.pop() #remove o ultimo elemento da todo list
    redo_list.append(last_todo)

def do_undo(todo_list, redo_list):
    if not redo_list:
        print('nada a refazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(todo)

def do_redo(to_do, todo_list):
    todo_list.append(todo)

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True: #precisa do while true pois o programa precisa executar
        #para incluir os valores nas listas
        todo = input('digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list) #chama a funcao que mostra a todo list
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list) #assim que fizer um undo, tem que adicionar
            #o que eu disfiz na re_do
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list) #assim que fizer um redo tem que remover do
            #tem que remover do redo
            continue

        do_add(todo, todo_list) #funcao que adiciona a to_do na to_do_list

