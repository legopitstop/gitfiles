import gitfiles

# Load all .gitignore files
gitfiles.load_gitignore()

# Returns True because .gitignore contains `*.so`
print(gitfiles.match("test.so"))
