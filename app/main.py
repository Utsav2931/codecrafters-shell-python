from os.path import isfile
import sys
import os

PATH = os.environ.get("PATH")

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
    shell_builtins = {"echo", "type", "exit"}
    if command in shell_builtins:
        return f"{command} is a shell builtin"
    else:
        paths = PATH.split(":")
        for path in paths:
            if os.path.isfile(f"{path}/{command}"):
                return f"{command} is {path}/{command}"
        return f"{command} not found"

if __name__ == "__main__":
    main()
