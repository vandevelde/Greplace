import os
import sys
import glob

def replace_text_in_files(file_pattern, search_text, replace_text, include_subdirectories=False):
    # Determine whether to include subdirectories
    if include_subdirectories:
        files = [file for file in glob.glob(file_pattern)]
        for root, _, subfiles in os.walk(os.path.dirname(file_pattern)):
            for subfile in subfiles:
                if glob.fnmatch.fnmatch(os.path.join(root, subfile), file_pattern):
                    files.append(os.path.join(root, subfile))
    else:
        files = glob.glob(file_pattern)

    # Iterate through all files
    for file_path in files:
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
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print("Usage: python script.py [-s] <file-pattern> <search-text> <replace-text>")
        sys.exit(1)

    # Check for the optional -s flag
    include_subdirectories = False
    if len(sys.argv) == 5 and sys.argv[1] == "-s":
        include_subdirectories = True
        sys.argv.pop(1)  # Remove the -s flag from sys.argv

    # Get command line arguments
    _, file_pattern, search_text, replace_text = sys.argv

    # Call the function to replace text in files
    replace_text_in_files(file_pattern, search_text, replace_text, include_subdirectories)