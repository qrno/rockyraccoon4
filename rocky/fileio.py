from os import listdir
from os.path import isfile, join, splitext

# Returns a list of all paths to files in a directory
# get_files('posts') -> 'posts/index.rocky'
def get_filepaths(dir):
    files = []
    for file in listdir(dir):
        if isfile(join(dir, file)):
            files.append(join(dir, file))
    return files

# Returns a list of all paths to files with extension ext
def get_filepaths_with_ext(dir, ext):
    files = get_filepaths(dir)

    files_with_ext = []
    for file in files:
        if splitext(file)[-1] == ext:
            files_with_ext.append(file)

    return files_with_ext

# Returns a list of lines without \n
def get_file_content(path):
    infile = open(path, 'r')
    content = infile.read().splitlines()

    return content

def savefile(dir, filename, content):
    print("Writing", filename, "to", dir)
    outfile = open(join(dir, filename), "w")
    outfile.write(content)
