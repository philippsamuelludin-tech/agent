from functions.get_files_info import get_files_info

print('get_files_info("calculator", "."):')
result = get_files_info("calculator", ".")
print("Result for current directory:")
print(result)
print()

print("get_files_info('calculator', 'pkg'):")
result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(result)
print()

print("get_files_info('calculator', '/bin'):")
result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(result)
print()

print("get_files_info('calculator', '../'):")
result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(result)
print()
