# LEER LAS ENTRADAS

def read_input():
    # Primer renglón: número de tareas y duración de cada tarea
    first_line = input().split()
    number_of_tasks = int(first_line[0])
    task_duration = int(first_line[1])

    # Siguientes renglones: un par (earliest_start, deadline) por tarea
    tasks = []
    for task_number in range(number_of_tasks):
        line = input().split()
        earliest_start = int(line[0])
        deadline = int(line[1])
        tasks.append((earliest_start, deadline))

    return task_duration, tasks

# LAS REGIONES PROHIBIDAS

def find_forbidden_regions(task_duration, tasks):
    # Valores distintos de earliest_start, del más tardío al más temprano
    distinct_starts = set()
    for task in tasks:
        distinct_starts.add(task[0])
    distinct_starts = sorted(distinct_starts, reverse=True)

    # Pares (deadline, earliest_start) ordenados de mayor a menor deadline, para acomodar hacia atrás
    tasks_by_deadline = []
    for earliest_start, deadline in tasks:
        tasks_by_deadline.append((deadline, earliest_start))
    tasks_by_deadline.sort(reverse=True)

    forbidden_regions = []
    for window_start in distinct_starts:
        latest_first_start = pack_backwards(window_start, task_duration,
                                            tasks_by_deadline, forbidden_regions)

        # Las tareas no caben después de window_start: la respuesta es "no"
        if latest_first_start < window_start:
            return None

        # Empezar una tarea en este intervalo bloquearía a este grupo
        if latest_first_start < window_start + task_duration:
            forbidden_regions.append((latest_first_start - task_duration, window_start))

    return forbidden_regions

def pack_backwards(window_start, task_duration, tasks_by_deadline, forbidden_regions):
     # Acomoda hacia atrás, lo más tarde posible, las tareas con earliest_start >= window_start
    current_time = float("inf")
    for deadline, earliest_start in tasks_by_deadline:
        if earliest_start < window_start:
            continue
        end_time = min(deadline, current_time)
        start_time = end_time - task_duration
        start_time = move_out_of_forbidden_regions(start_time, forbidden_regions)
        current_time = start_time

    # Inicio de la primera tarea del grupo
    return current_time

def move_out_of_forbidden_regions(start_time, forbidden_regions):
    # Si el inicio cae dentro de una región prohibida, se mueve a su borde izquierdo
    moved = True
    while moved:
        moved = False
        for region_start, region_end in forbidden_regions:
            if region_start < start_time < region_end:
                start_time = region_start
                moved = True
    return start_time

# EDF

import heapq

def schedule_with_edf(task_duration, tasks, forbidden_regions):
    # Tareas ordenadas por earliest_start, para irlas liberando en orden
    tasks_by_start = sorted(tasks)
    available_deadlines = []  # montículo con los deadline de las tareas disponibles
    next_task_index = 0
    current_time = 0
    tasks_done = 0

    while tasks_done < len(tasks):
        # Si no hay tareas disponibles, saltar al earliest_start de la siguiente
        if len(available_deadlines) == 0:
            next_start = tasks_by_start[next_task_index][0]
            if current_time < next_start:
                current_time = next_start

        # No empezar dentro de una región prohibida
        current_time = move_past_forbidden_regions(current_time, forbidden_regions)

        # Agregar al montículo las tareas que ya se pueden empezar
        while next_task_index < len(tasks_by_start) and tasks_by_start[next_task_index][0] <= current_time:
            heapq.heappush(available_deadlines, tasks_by_start[next_task_index][1])
            next_task_index += 1

        # Hacer la tarea con el deadline más próximo
        deadline = heapq.heappop(available_deadlines)
        end_time = current_time + task_duration
        if end_time > deadline:
            return False
        current_time = end_time
        tasks_done += 1

    return True

def move_past_forbidden_regions(current_time, forbidden_regions):
    # Si current_time cae dentro de una región prohibida, se mueve a su borde derecho
    moved = True
    while moved:
        moved = False
        for region_start, region_end in forbidden_regions:
            if region_start < current_time < region_end:
                current_time = region_end
                moved = True
    return current_time

# OUTPUT

def main():
    task_duration, tasks = read_input()
    forbidden_regions = find_forbidden_regions(task_duration, tasks)

    # Si algún grupo no cabe, la respuesta ya es "no"
    if forbidden_regions is None:
        print("no")
    elif schedule_with_edf(task_duration, tasks, forbidden_regions):
        print("yes")
    else:
        print("no")

main()

# Get-Content hsample1.txt | python h.py > yes
# Get-Content hsample2.txt | python h.py > no
# Get-Content hsample3.txt | python h.py > yes