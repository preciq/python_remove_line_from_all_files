import os
import fnmatch

def remove_line_from_files(directory, pattern, text):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
            with open(filepath, 'w') as file:
                for line in lines:
                    if text not in line:
                        file.write(line)

# Example usage
directory = 'p_s'
pattern = 'pain.txt'  # Example: '*.txt'
text = 'desired_text_here'

remove_line_from_files(directory, pattern, text)
