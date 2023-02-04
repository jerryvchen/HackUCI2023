import planner

def main() -> None:
    input = planner.read_input_file_path()
    planner_dict = planner.create_planner_from_path(input)
    planner.print_planner(planner_dict)

if __name__ == '__main__':
    main()