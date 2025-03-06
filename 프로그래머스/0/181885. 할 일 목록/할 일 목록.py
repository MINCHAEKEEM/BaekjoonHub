def solution(todo_list, finished):
    answer = []
    new_todo = dict(zip(todo_list, finished))
    
    for todo, boool in new_todo.items():
        if boool == False:
            answer.append(todo)
    return answer