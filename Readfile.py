def read_from_file(file_name,):
   with open(file_name, 'r') as file:
       content = file.read()
   print(content)

file_name = 'Guvi.txt'
print("Reading content:")
read_from_file(file_name)

