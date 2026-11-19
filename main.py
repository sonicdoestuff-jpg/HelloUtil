
import subprocess

BANNER = r"""
 _     _____ _     _     ____  _
/ \ /|/  __// \   / \   /  _ \/
| |_|||  \  | |   | |   | / \||
| | |||  /_ | |_/| |_/| \_/||
\_/ \|\____\\____/\____/\____/
"""

def main():
    print(BANNER)
    print("       HelloUtil v1.0")
    print("--------------------------")
    print("[1] Git clone a repository")
    print("[2] Chatbot")
    print("[3] About")
    print("[0] Exit")

    choice = input("\nHelloUtil > ")

    if choice == "1":
        url = input("Repository URL: ")
        subprocess.run(["git", "clone", url], check=False)

    elif choice == "2":
        from chatbot import chatbot
        chatbot()

    elif choice == "3":
        print("HelloUtil - Python utility")

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
