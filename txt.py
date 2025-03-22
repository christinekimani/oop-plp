def read_and_modify_file():
    try:
        input_filename = input("Enter filename: ")  

        with open(input_filename, "r") as file:  
            content = file.read()

        modified_content = content.upper()

        output_filename = "modified_" + input_filename

        with open(output_filename, "w") as file:
            file.write(modified_content)

        print(f"Success! Modified file saved as: {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

