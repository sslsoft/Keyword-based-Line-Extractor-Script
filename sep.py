#Script By Tamim Shikder 

import os
folder_path = r'tamim\febdb\Shared Server'  # ei khane db er location ta diven mane db je file a rakha ase tar location diven
keywords = ['keyword name here']  # ei khane ei je tar account lagbe tar link ba tar nam diven
output_files = {keyword: os.path.join(folder_path, f'{keyword}.txt') for keyword in keywords}
#nicher kno kiso change kora jave nah jodi kiso change koren tahole script thik mote kaj korve nah
def extract_lines_with_keywords(folder, keywords, output_files):
    try:
        found_lines = set()  
        
        found_lines = {keyword: set() for keyword in keywords}
 
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    print(f"Processing: {file_path}")  

                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                           
                            for keyword in keywords:
                                if keyword.lower() in line.lower():  
                                    found_lines[keyword].add(line.strip())

        for keyword, lines in found_lines.items():
            if lines:
                with open(output_files[keyword], 'w', encoding='utf-8') as out_f:
                    out_f.write('\n'.join(lines))
                print(f"Task completed for '{keyword}'. {len(lines)} unique lines written to {output_files[keyword]}")
            else:
                print(f"No lines containing '{keyword}' found.")

    except Exception as e:
        print(f"An error occurred: {e}")

extract_lines_with_keywords(folder_path, keywords, output_files)
