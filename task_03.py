import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path, indent=""):
    try:
        if not os.path.isdir(path):
            print(Fore.RED + f"Помилка: {path} не є директорією.")
            return

        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(Fore.GREEN + indent + "📂 " + entry.name)
                    print_directory_structure(entry.path, indent + "    ")
                else:
                    print(Fore.BLUE + indent + "📜 " + entry.name)
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: Будь ласка, вкажіть шлях до директорії.")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + f"Помилка: Директорія {directory_path} не існує.")
        sys.exit(1)

    print(Fore.YELLOW + f"Структура директорії {directory_path}:\n")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()