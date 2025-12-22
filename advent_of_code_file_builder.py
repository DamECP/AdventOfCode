import urllib.request
from urllib.error import HTTPError, URLError
import os
from datetime import datetime


# === Check for finished problems ===
def is_finished(year: int, day: int) -> bool:

    year_folder = str(year)

    if not os.path.exists(year_folder):
        return False

    for existing_file in os.listdir(year_folder):
        if f"ex{day}" in existing_file and "^" in existing_file:
            return True
    return False


# === Cookie session ===
if not os.path.exists("session_cookie.txt"):
    print(
        "[!] session_cookie.txt not found. Please create it with your AoC session cookie."
    )
    exit()

with open("session_cookie.txt") as cookiefile:  # store cookie in a variable
    cookie = cookiefile.read().strip()


# === Main script ===
current_year = datetime.now().year
changes = False

for year in range(2025, current_year + 1):
    print(year)
    existing_files = set(os.listdir(str(year))) if os.path.exists(str(year)) else set()

    for day in range(1, 25):

        dataset = f"ex{day}.txt"
        python_file = f"{year} - ex{day}.py"
        half_finished = f"{year} - ex{day}^.py"
        finished_file = f"{year} ^^ ex{day}.py"
        python_tests = [half_finished, finished_file, python_file]

        if dataset in existing_files and any(
            name in existing_files for name in python_tests
        ):

            continue

        url = f"https://adventofcode.com/{year}/day/{day}/input"

        try:
            my_request = urllib.request.Request(url)  # define a request
            my_request.add_header(
                "User-Agent", "github.com/damECP/aoc-script by damECP@example.com"
            )
            my_request.add_header(
                "Cookie", f"session={cookie}"
            )  # add the cookie to the request

            with urllib.request.urlopen(my_request) as data:
                exercise_data = data.read().decode(
                    "utf-8"
                )  # decode the byte format to utf-8
                file_path = os.path.join(str(year), dataset)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                finished = is_finished(year, day)

                if not os.path.exists(file_path):
                    with open(file_path, "w") as new_file:
                        new_file.write(exercise_data)
                        changes = True
                    print(f"[+] File 'ex{day}.txt' created")

                if not finished and not os.path.exists(python_file):
                    intro = f"with open('ex{day}.txt') as exercise:\n    for line in exercise:\n        line = line.replace('\\n', '')"
                    py_path = os.path.join(str(year), python_file)
                    with open(py_path, "w") as py_file:
                        py_file.write(intro)
                        changes = True
                    print(f"[+] File 'ex{day}.py' created")

        except HTTPError as e:
            if e.code == 500:
                print("Cookie error, update your cookie")
                exit(1)

        except URLError as e:
            print(e)
            break

if changes == False:
    print("Everything is up to date, no change has been made")
