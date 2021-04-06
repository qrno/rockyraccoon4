from fileio import get_filepaths_with_ext, get_filepaths, get_file_content, savefile
from file import File
from template import Template

from os.path import join, basename, splitext

input_dir = 'posts'
output_dir = 'output'
templates_dir = join(input_dir, 'templates')

post_paths = get_filepaths_with_ext(input_dir, '.rocky')
template_paths = get_filepaths_with_ext(templates_dir, '.html')

templates = {}
for file in template_paths:
    content = get_file_content(file)
    filename_without_ext = splitext(basename(file))[0]
    templates[filename_without_ext] = content

files = []
for file in post_paths:
    f = File(file, get_file_content(file))
    files.append(f)

print("Templates loaded:", [key for key in templates])
print("Files loaded:", [f.path for f in files])

for file in files:
    if 'template' in file.attributes:
        file_template = file.attributes['template']
        print("File", file.path, "has template", file_template)

        if file_template in templates:
            t = Template(file_template, templates[file_template])
            rendered = t.render(file.parsed, file.attributes)

            savefile(output_dir, file.attributes['slug'] + '.html', rendered)
            print("Rendered and saved")
        else:
            savefile(output_dir, file.attributes['slug'] + '.html', rendered)
            print("Template not found! Non-rendered file saved")

