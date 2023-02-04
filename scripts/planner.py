# planner.py

from pathlib import Path
def planner(start_day: int, end_day: int, tasks: list[str]) -> dict[int, list[str]]:
    """Divides up the tasks into a certain number of days, and prints it out to an external file. """
    total_days = end_day - start_day + 1 # including today
    





def input_tasks(path: Path) -> list[str]:
    """Parses through a file and returns a compiled list of tasks."""
    tasks = list()
    try:
        with open(path, 'r') as file:
            start_day = int(file.readline())
            
            print('SUCCESS')
    except FileNotFoundError:
        print('FILE NOT FOUND')

def _read_input_file_path() -> Path:
    """Reads the input file path from standard input"""
    return Path(input())


def _print_planner(planner: dict[int, list[str]]):
    """Prints the planner into the console."""
    for day, events in planner:
        event_str = ', '.join(events)
        print('Day ' + str(day) + ': ' + event_str)


