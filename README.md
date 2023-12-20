# HTML to PHP File Extension Change Script

This Python script allows you to batch change file extensions in a specified directory from `.html` to `.php`.

## Description

The script streamlines the process of converting HTML files to PHP. It iterates through files in the specified directory, changes their extensions from `.html` to `.php`, and provides an efficient way to update multiple files at once.

## How to Use

1. **Clone or Download**: Clone or download this repository to your local machine.

2. **Install Python**: Ensure Python is installed on your system.

3. **Navigate to Script Directory**: Open a command prompt or terminal and navigate to the directory where the Python script (`html-to-php.py`) is located.

   ```bash
   cd path/to/script/directory
   
4. Execute the script with the following command, replacing [directory_path] with the directory containing your files.

   `python html-to-php.py [directory_path]`

    For example, if your files is located at 'c:\main', you would run:

   `python html-to-php.py "c:\main"`

5. The script will process the files in the specified directory and rename the file extention.
6. After the script completes, you'll receive a message confirming that all files have been successfully renamed. eg: `Changed: index.html -> index.php`.
