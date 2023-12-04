def read_file_to_list(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    filtered_lines = [line.strip() for line in lines if line.strip()]
    return filtered_lines
