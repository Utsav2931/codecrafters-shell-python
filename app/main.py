import subprocess
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
        case "pwd":
            res = os.getcwd()
        case _:
            file_path = get_file_path(user_command[0])
            if file_path != "":
                result = subprocess.run(
                    user_command,
                    capture_output = True,
                    text = True,
                )
                return result.stdout.strip("\n")
            res = f"{user_command[0]}: command not found"

    return res

def type (command):
    shell_builtins = {"echo", "type", "exit"}
    if command in shell_builtins:
        return f"{command} is a shell builtin"
    else:
        file_path = get_file_path(command)
        if file_path != "":
            return f"{command} is {file_path}"
        return f"{command}: not found"

def get_file_path (file_name):
        paths = PATH.split(":")
        for path in paths:
            if os.path.isfile(f"{path}/{file_name}"):
                return f"{path}/{file_name}"
        return ""

if __name__ == "__main__":
    main()
