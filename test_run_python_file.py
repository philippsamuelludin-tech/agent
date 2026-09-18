from functions.run_python_file import run_python_file

print('run_python_file("calculator", "main.py")')
print(run_python_file("calculator", "main.py"))
print("Should run the calculator's usage instructions")
print()

print('run_python_file("calculator", "main.py", ["3 + 5"])')
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print("Should run the calculator")
print()

print('run_python_file("calculator", "tests.py")')
print(run_python_file("calculator", "tests.py"))
print("Should run the calculator tests")
print()

print('run_python_file("calculator", "../main.py")')
print(run_python_file("calculator", "../main.py"))
print("Should give Error")
print()

print('run_python_file("calculator", "nonexistent.py")')
print(run_python_file("calculator", "nonexistent.py"))
print("Should give Error")
print()

print('run_python_file("calculator", "lorem.txt")')
print(run_python_file("calculator", "lorem.txt"))
print("Should give Error")
print()