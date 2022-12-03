import os

print(os.getcwd())
os.removedirs("New_directory")
print(os.listdir())
os.mkdir('New_directory')
print(os.listdir())

os.rename('New_directory', 'Renamed_directory')
print(os.listdir())