# let we have an array of tasks and persons e.g.
# tasks = [t1,t2,t3,t4,t5,t6,t7,t8, t9] OR [t1,t2,t3,t4, t5] OR [t1,t2, t3] OR [t1, t2]
# persons = ["p1", "p2", "p3"]
# Now, the problem is to divide equal tasks among each person
# first notice the no. of tasks. That are 9 tasks, 5 tasks, 3 tasks and 2 tasks
# Notice that, no. of persons are 3.
from functions import define_person_task, define_flooring_task
import array

# case 1:
# no. of tasks greater than no. of persons
# case 2:
# no. of tasks equal to no. of persons
# case 3:
# no. of tasks less than no. of persons
task_array = [
    "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11", "t12",
    "t13", "t14", "t15", "t16", "t17", "t18", "t19", "t20", "t21", "t22",
    "t23", "t24", "t25", "t26", "t27", "t28", "t29", "t30", "t31", "t32",
    "t33", "t34", "t35", "t36", "t37", "t38", "t39", "t40", "t41"
]
# task_array = [
#     "t1", "t2", "t3", "t4", "t5", "t6", "t7", "t8", "t9", "t10", "t11"
# ]
# task_array = ["t1", "t2", "t3", "t4", "t5", "t6", "t7"]
# task_array = ["t1", "t2"]
persons = ["p1", "p2", "p3", "p4", "p5", "p6"]
# persons = ["p1", "p2", "p3"]

remaining = no_of_tasks = len(task_array)
no_of_persons = len(persons)

# print(f"task: {no_of_tasks}")
# print(f"person: {no_of_persons}")

person_tasks = []
assigned = 0

# if case 1 or case 2 - we can handle both cases at once
if no_of_tasks >= no_of_persons:
    assigning = round(no_of_tasks / no_of_persons)
    # print("Rounded: ", assigning, "Exact ", (no_of_tasks / no_of_persons))
    while assigning <= remaining:
        person_tasks.append(
            define_person_task(no_of_tasks=assigning,
                               put_at=assigned,
                               array=task_array))
        assigned += assigning
        remaining -= assigning

    if remaining:
        #if division of tasks less than no. of tasks
        if round(no_of_tasks / no_of_persons) < (no_of_tasks / no_of_persons):
            # print(
            #     f"Assigning: {assigning}\nNo of persons: {no_of_persons}\nNo of Tasks: {no_of_tasks}\nAssigned to persons: {assigning * no_of_persons}\nReamining: {remaining}"
            # )
            last_index = len(person_tasks) - 1
            # print(last_index)
            # print(person_tasks[last_index])
            person_tasks[last_index] = define_flooring_task(
                no_of_tasks=remaining,
                put_at=assigned,
                append_in=person_tasks[last_index],
                from_array=task_array)
            assigned += assigning
        # if division of tasks greater than no. of tasks
        else:
            person_tasks.append(
                define_person_task(no_of_tasks=remaining,
                                   put_at=assigned,
                                   array=task_array))
            assigned += assigning
else:
    i = 1
    while i <= no_of_persons:
        if i <= no_of_tasks:
            person_tasks.append(define_person_task(1, assigned, task_array))
        else:
            person_tasks.append(define_person_task(0, assigned, task_array))

        assigned += 1
        i += 1

print(f"Tasks per person: {person_tasks}")
