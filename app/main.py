import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input().split(" ")
        print(execute_command(command))


def execute_command(command):
    res = ""
    match command[0]:
        case "exit":
            exit(int(command[1]))
        case "echo":
            res = " ".join(command[1:])
        case _:
            res = f"{command[0]}: command not found"

    return res

if __name__ == "__main__":
    main()
