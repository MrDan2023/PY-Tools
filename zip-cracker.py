import zipfile
import os
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "Zip Cracker - Mr Dan"

set_console_title(custom_title)

def extract_zip(zip_file, password, extract_path):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(path=extract_path, pwd=password.encode())
        return True
    except Exception as e:
        return False

def list_zip_files(directory):
    zip_files = [f for f in os.listdir(directory) if f.endswith('.zip')]
    return zip_files

def main():
    directory = "."
    wordlist_file = "rockyou.txt"

    zip_files = list_zip_files(directory)

    if not zip_files:
        print("No ZIP files found.")
        return

    print("Available ZIP files:")
    for i, zip_file in enumerate(zip_files):
        print(f"{i + 1}: {zip_file}")

    try:
        choice = int(input("Please select the zip file:" + "\n ~~> "))
        if 1 <= choice <= len(zip_files):
            selected_zip_file = zip_files[choice - 1]
            print(f"Selected ZIP file: {selected_zip_file}")

            extract_folder = os.path.splitext(selected_zip_file)[0]
            os.makedirs(extract_folder, exist_ok=True)

            with open(wordlist_file, 'r', errors='ignore') as wordlist:
                for line in wordlist:
                    password = line.strip()
                    if extract_zip(
                        os.path.join(directory, selected_zip_file),
                        password,
                        extract_folder
                    ):
                        print(f"Password found!: {password}")
                        break
                else:
                    print("Password was not found :(")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    print("Make sure to check out MrDan2023 on Github!")
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
