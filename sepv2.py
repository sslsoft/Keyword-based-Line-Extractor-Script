import os
import chardet

# Specify folder path and keywords
folder_path = r'tamim\febdb\Shared Server'  # Replace with the path to your database folder
keywords = ['keyword name here']  # Replace with your keywords
output_files = {keyword: os.path.join(folder_path, f'{keyword}.txt') for keyword in keywords}


def detect_encoding(file_path):
    """Detect the encoding of a file."""
    with open(file_path, 'rb') as f:
        raw_data = f.read(1024)  
        result = chardet.detect(raw_data)
    return result['encoding']

def extract_lines_with_keywords(folder, keywords, output_files):
    try:
        found_lines = {keyword: set() for keyword in keywords}

        
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")

                    
                    encoding = detect_encoding(file_path)
                    print(f"Detected encoding: {encoding}")

                    try:
                        
                        with open(file_path, 'r', encoding=encoding) as f:
                            for line in f:
                                for keyword in keywords:
                                    if keyword.lower() in line.lower():
                                        found_lines[keyword].add(line.strip())
                    except Exception as read_error:
                        print(f"Error reading file {file_path}: {read_error}")

        
        for keyword, lines in found_lines.items():
            if lines:
                output_file = output_files[keyword]
                with open(output_file, 'w', encoding='utf-8') as out_f:
                    out_f.write('\n'.join(lines))
                print(f"Task completed for '{keyword}'. {len(lines)} unique lines written to {output_file}")
            else:
                print(f"No lines containing '{keyword}' found.")

    except Exception as e:
        print(f"An error occurred: {e}")


extract_lines_with_keywords(folder_path, keywords, output_files)
