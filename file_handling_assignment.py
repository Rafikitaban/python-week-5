# contents of file_handling_assignment.py

try:
    # Open 'my_file.txt' in write mode
    with open('my_file.txt', 'w') as file:
        file.write("This is my first text.\n")
        file.write("Here is my second text, with  numbers: 12345\n")
        file.write("Finally, my third line with some more text.\n")

    # Open 'my_file.txt' in read mode and display the content
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File contents before appending:")
        print(content)

    # Open 'my_file.txt' in append mode
    with open('my_file.txt', 'a') as file:
        file.write("Appending my new fourth line.\n")
        file.write("And here is another fifth line with some extra words.\n")
        file.write("Finally, my sixth line, the final one to end this example.\n")

    # Open 'my_file.txt' in read mode and display the updated content
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("File contents after appending:")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
