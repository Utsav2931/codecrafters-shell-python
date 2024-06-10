import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        user_command = input().split(" ")
        print(execute_command(user_command))


def execute_command(user_command):
    res = ""
    match user_command[0]:
        case "exit":
            exit(int(user_command[1]))
        case "echo":
            res = " ".join(user_command[1:])
        case "type":
            res = type(user_command[1])
        case _:
            res = f"{user_command[0]}: command not found"

    return res

def type (command):
    commands = {"echo", "type", "exit"}
    if command in commands:
        return f"{command} is a shell builtin"
    else:
        return f"{command} not found"

if __name__ == "__main__":
    main()
