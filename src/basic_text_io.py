file_path = 'data/sample_resumes/resume_1.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        count = len(words)
        print(f'Word Count: {count}')
except FileNotFoundError:
    print("Error: The file was not found. Check your folder path!")