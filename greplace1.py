import os
import sys

def replace_text_in_files(directory, search_text, replace_text):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Replace the search_text with replace_text
            modified_content = content.replace(search_text, replace_text)

            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(modified_content)

            print(f"Replaced '{search_text}' with '{replace_text}' in {file_path}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <directory> <search-text> <replace-text>")
        sys.exit(1)

    # Get command line arguments
    directory, search_text, replace_text = sys.argv[1:]

    # Call the function to replace text in files
    replace_text_in_files(directory, search_text, replace_text)