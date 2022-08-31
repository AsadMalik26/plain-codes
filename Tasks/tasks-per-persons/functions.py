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


def define_flooring_task(no_of_tasks, put_at, append_in, from_array):
    i = 0
    # tasks = None
    # print("no_of_tasks: ", no_of_tasks)
    while i < no_of_tasks:
        append_in.append(from_array[put_at])
        put_at += 1
        i += 1
    return append_in


# =================================================End functions==========================================
