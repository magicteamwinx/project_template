from app.io.input import input_from_console, read_with_builtin
from app.io.output import output_to_console, write_with_builtin

def main():
    # 1. Ввід з консолі
    text = input_from_console()
    output_to_console(f"Ви ввели: {text}")
    write_with_builtin("data/output.txt", text)

if __name__ == "__main__":
    main()