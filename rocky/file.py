from fileio import savefile
import re

patterns = {
    'setter' : '(]) (\w+) (.+)',
    'tag' : '(\[) (\w+) (.+) (])',
    'link' : '([^ ]+) (.+)',
}

substitutes = {
    'link' : r'<a href="\1">\2</a>',
    'img'  : r'<img href="\1" alt="\2">'
}

class File:
    def __init__(self, path, raw):
        self.path = path
        self.raw = raw

        self.parsed = ""
        self.attributes = {}
        for line in raw:
            self.parseline(line)

        self.templated = ""

    def parseSetter(self, line):
        result = re.match(patterns['setter'], line)

        key = result.group(2)
        value = result.group(3)
    
        print("Set", key, "\tto", value)
        self.attributes[key] = value

    def processTag(self, tag, content):
        if tag == 'link':
            newline = re.sub(patterns['link'], substitutes['link'], content)
            return newline
        if tag == 'image':
            newline = re.sub(patterns['link'], substitutes['img'], content)
            return newline

        if tag == 'section':
            tag = 'h1'
        elif tag == 'subsection':
            tag = 'h2'
        return '<'+tag+'>' + content + '</'+tag+'>'

    def parseTag(self, line):
        result = re.search(patterns['tag'], line)

        tag = result.group(2)
        content = result.group(3)
        
        print("Processing", tag, "\t", content)

        processed = self.processTag(tag, content)
        newline = re.sub(patterns['tag'], processed, line)
        return newline
    
    def parseline(self, line):
        if re.match(patterns['setter'], line):
            self.parseSetter(line)
        elif re.search(patterns['tag'], line):
            self.parsed += self.parseTag(line) + '\n'
