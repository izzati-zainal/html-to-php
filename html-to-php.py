import os
import sys

def change_file_extension(directory_path):
    # Check if the provided path is a directory
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has the .html extension
        if filename.endswith(".html"):
            # Generate the new filename with .php extension
            new_filename = os.path.join(directory_path, os.path.splitext(filename)[0] + ".php")

            # Rename the file
            os.rename(os.path.join(directory_path, filename), new_filename)
            print(f"Changed: {filename} -> {os.path.basename(new_filename)}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python html-to-php.py [directory_path]")
        sys.exit(1)

    # Get the directory path from the command-line argument
    directory_path = sys.argv[1]

    # Call the function to change file extensions
    change_file_extension(directory_path)
