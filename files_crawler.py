import os
import chardet
import re

def is_text_file(file_path, sample_size=8192):
    text_extensions = {
        '.txt', '.log', '.csv', '.yml', '.yaml', '.json', '.xml', '.html', '.htm', '.css', '.js', '.ts', '.py', '.java', '.c', '.cpp', '.h', '.hpp', '.cs', '.php', '.rb', '.pl', '.sh', '.bash', '.ps1', '.sql', '.ini', '.cfg', '.conf', '.properties', '.gradle', '.pro', '.kt', '.kts', '.swift', '.m', '.mm', '.go', '.rs', '.r', '.scala', 'properties', '.jar','.gradle'
    }
    
    if os.path.splitext(file_path)[1].lower() in text_extensions:
        return True
    
    try:
        with open(file_path, 'rb') as f:
            raw = f.read(sample_size)
            if raw:
                result = chardet.detect(raw)
                if result['encoding'] is not None:
                    return True
    except Exception:
        pass
    return False

def create_file_structure(start_path):
    file_structure = []
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        current_dir = []
        for file in files:
            file_path = os.path.join(root, file)
            if is_text_file(file_path):
                current_dir.append(file_path)
        if current_dir:
            file_structure.append(current_dir)
    return file_structure

def write_combined_text_file(start_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, _, files in os.walk(start_path):
            for file in files:
                file_path = os.path.join(root, file)
                if is_text_file(file_path):
                    try:
                        with open(file_path, 'rb') as text_file:
                            raw = text_file.read(8192)
                            if raw:
                                result = chardet.detect(raw)
                                encoding = result['encoding'] or 'utf-8'
                        with open(file_path, 'r', encoding=encoding) as text_file:
                            f.write(f"File: {file_path}\n")
                            f.write("="*50 + "\n")
                            f.write(text_file.read())
                            f.write("\n\n")
                    except Exception as e:
                        f.write(f"Error reading {file_path}: {str(e)}\n\n")

def write_file_structure_to_py(file_structure, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("file_structure = [\n")
        for directory in file_structure:
            f.write("    [\n")
            for file_path in directory:
                f.write(f"        '{file_path}',\n")
            f.write("    ],\n")
        f.write("]\n")

def sanitize_variable_name(name):
    # Remove non-alphanumeric characters and replace with underscores
    name = re.sub(r'\W+', '_', name)
    # Ensure the variable name starts with a letter or underscore
    if name[0].isdigit():
        name = '_' + name
    return name

def write_files_content_to_py(start_path, output_file):
    variable_names = []
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, _, files in os.walk(start_path):
            for file in files:
                file_path = os.path.join(root, file)
                if is_text_file(file_path):
                    try:
                        with open(file_path, 'rb') as text_file:
                            raw = text_file.read(8192)
                            if raw:
                                result = chardet.detect(raw)
                                encoding = result['encoding'] or 'utf-8'
                        with open(file_path, 'r', encoding=encoding) as text_file:
                            file_name = os.path.splitext(file)[0]
                            variable_name = sanitize_variable_name(file_name)
                            content = text_file.read()
                            f.write(f"{variable_name} = '''\n{content}\n'''\n\n")
                            variable_names.append(variable_name)
                    except Exception as e:
                        f.write(f"# Error reading {file_path}: {str(e)}\n\n")
        
        # Add the whole_code dictionary
        f.write("whole_code = {\n")
        for var_name in variable_names:
            f.write(f"    '{var_name}': {var_name},\n")
        f.write("}\n")

import os

def files_crawler():
    folder_path = input("Enter the folder path to crawl: ")
    temp_dir = os.path.join('Temp')
    combined_file = os.path.join(temp_dir, "combined_text_files.txt")
    structure_file = os.path.join(temp_dir, "code_files_list.txt")
    content_file = os.path.join(temp_dir, "files_content.py")
    
    # Create Temp directory if it doesn't exist
    os.makedirs(temp_dir, exist_ok=True)
    
    file_structure = create_file_structure(folder_path)
    write_combined_text_file(folder_path, combined_file)
    write_file_structure_to_py(file_structure, structure_file)
    write_files_content_to_py(folder_path, content_file)
    
    print(f"Combined text files written to {combined_file}")
    print(f"File structure written to {structure_file}")
    print(f"File contents and whole_code dictionary written to {content_file}")