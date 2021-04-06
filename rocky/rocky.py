from fileio import get_filepaths_with_ext, get_filepaths, get_file_content
from file import File

input_dir = 'posts'
output_dir = 'output'

infiles  = get_filepaths_with_ext('posts', '.rocky')
contents = [get_file_content(f) for f in infiles]

for file in infiles:
    f = File(file, get_file_content(file))
    f.writefile(output_dir)
