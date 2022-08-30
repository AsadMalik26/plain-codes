# =================================================functions==========================================
def define_person_task(no_of_tasks, put_at, array):
    i = 0
    # print("no_of_tasks: ", no_of_tasks)
    task_list = []
    while i < no_of_tasks:
        task_list.append(array[put_at])
        put_at += 1
        i += 1

    return task_list


# =================================================End functions==========================================
