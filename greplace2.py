import os
import sys
import glob

def replace_text_in_files(file_pattern, search_text, replace_text):
    # Iterate through all files matching the pattern
    for file_path in glob.glob(file_pattern):
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
        print("Usage: python script.py <file-pattern> <search-text> <replace-text>")
        sys.exit(1)

    # Get command line arguments
    file_pattern, search_text, replace_text = sys.argv[1:]

    # Call the function to replace text in files
    replace_text_in_files(file_pattern, search_text, replace_text)