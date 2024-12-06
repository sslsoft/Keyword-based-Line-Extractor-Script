# Keyword-based-Line-Extractor-Script
Keyword-based Line Extractor Script . This script scans `.txt` files within a specified folder (and its subfolders) to find lines containing specific keywords. Matching lines are extracted and saved into separate output files for each keyword, ensuring efficient and organized data retrieval.  
# Keyword-based Line Extractor Script  

## Overview  
This Python script is designed to search for specific keywords within text files located in a specified folder (and its subfolders). When matches are found, the script extracts the lines containing those keywords and saves them to separate output files, one for each keyword.

## Features  
- **Recursive Search**: The script processes all `.txt` files in the specified folder and its subfolders.  
- **Case-Insensitive Matching**: Keywords are matched irrespective of case sensitivity.  
- **Keyword-specific Output**: Each keyword gets its own output file with all unique lines containing that keyword.  
- **Handles Large Files**: Efficiently reads files line by line to process large datasets.  
- **Error Handling**: Catches exceptions and provides meaningful error messages.  

## Requirements  
- Python 3.6 or higher  

## How to Use  

### Step 1: Define Input Parameters  
Open the script and configure the following variables:  

1. **`folder_path`**: Set this to the folder path where your `.txt` files are located. Example:  
   ```python
   folder_path = r'tamim\febdb\Shared Server'
### keywords: Define the list of keywords you want to search for. Example:

**`keywords`** = ['keyword1', 'keyword2']

**Author: Tamim Shikder**   
