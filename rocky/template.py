import re

patterns = {
    'var' : '\[\[ (\w+) ]]'
}

class Template:
    def __init__(self, path, content):
        self.path = path
        self.content = content

    def render(self, content, attributes):
        rendered = ""
        for line in self.content:
            newline = line
            result = re.search(patterns['var'], line)

            if result:
                key = result.group(1)
                if key == 'content':
                    newline = re.sub(patterns['var'], content, line)
                elif key in attributes:
                    newline = re.sub(patterns['var'], attributes[key], line)

            rendered += newline + '\n'
        return rendered
