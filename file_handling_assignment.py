def main():
    filename = "my_file.txt"

    # File Creation: Create a new text file and write to it
    try:
        with open(filename, 'w') as file:
            file.write("Hello, this is my first line.\n")
            file.write("The answer to life, the universe, and everything is 42.\n")
            file.write("Python is great for file handling!\n")
        print(f"'{filename}' has been created and written to successfully.")
    
    except (PermissionError, IOError) as e:
        print(f"Error creating or writing to the file: {e}")
    
    finally:
        print("File creation process complete.")

    # File Reading and Display: Read the contents of the file
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)
    
    except FileNotFoundError as e:
        print(f"Error: The file '{filename}' was not found: {e}")
    
    except (PermissionError, IOError) as e:
        print(f"Error reading the file: {e}")
    
    finally:
        print("File reading process complete.")

    # File Appending: Open the file in append mode and add more content
    try:
        with open(filename, 'a') as file:
            file.write("Appending a new line to the file.\n")
            file.write("Another interesting fact: The sun is 93 million miles away.\n")
            file.write("Finally, let's add one more line.\n")
        print(f"Additional lines have been appended to '{filename}' successfully.")
    
    except (PermissionError, IOError) as e:
        print(f"Error appending to the file: {e}")
    
    finally:
        print("File appending process complete.")

    # Read and display the updated contents of the file
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nUpdated contents of the file:")
            print(content)
    
    except FileNotFoundError as e:
        print(f"Error: The file '{filename}' was not found: {e}")
    
    except (PermissionError, IOError) as e:
        print(f"Error reading the file: {e}")
    
    finally:
        print("Final file reading process complete.")


if __name__ == "__main__":
    main()
