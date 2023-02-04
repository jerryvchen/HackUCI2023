# planner.py

from pathlib import Path
def create_planner(start_day: int, end_day: int, tasks: list[str]) -> dict[int, list[str]]:
    """Divides up the tasks into a certain number of days, and prints it out to an external file. """
    planner = dict()
    total_days = end_day - start_day + 1 # including today
    for day in range(start_day, total_days + 1):
        planner[day] = list()
    tasks_per_day = len(tasks) // total_days
    extra_tasks = len(tasks) % total_days

    list_index = 0
    for day in range(start_day, total_days + 1):
        for _ in range(tasks_per_day):
            planner[day].append(tasks[list_index])
            list_index += 1
        if extra_tasks > 0:
            planner[day].append(tasks[list_index])
            list_index += 1
            extra_tasks -= 1
    return planner


def create_planner_from_path(path: Path) -> dict[int, list[str]]:
    """Parses through a file and returns a planner dict."""
    tasks = list()
    try:
        with open(path, 'r') as file:
            start_day = int(file.readline())
            end_day = int(file.readline())
            tasks = list()
            for line in file:
                tasks.append(line.strip())
            planner = create_planner(start_day, end_day, tasks)
            print('SUCCESS')
            return planner
    except FileNotFoundError:
        print('FILE NOT FOUND')
    

def read_input_file_path() -> Path:
    """Reads the input file path from standard input"""
    return Path(input())


def print_planner(planner: dict[int, list[str]]):
    """Prints the planner into the console."""
    for day in planner.keys():
        event_str = ', '.join(planner[day])
        print('Day ' + str(day) + ': ' + event_str)

