import gitfiles

# Load all .gitignore files
gitfiles.load_gitignore()

# Should return ['app.py'] because all other names exist in .gitignore
files = [
    '.venv',
    '.env',
    'app.py'
]
print(gitfiles.filter(files))
