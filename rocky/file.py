from fileio import savefile
import re

patterns = {
    'setter' : '(]) (\w+) (.+)',
    'tag' : '(\[) (\w+) ([^\]\[]+) (])',
    'link' : '([^ ]+) (.+)',
}

substitutes = {
    'link' : r'<a href="\1">\2</a>',
    'img'  : r'<img src="\1" alt="\2">'
}

subtags = {
    'bold' : 'b',
    'italic' : 'i',

    'section' : 'h2',
    'subsection' : 'h3',

    'paragraph' : 'p',
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
            newline = re.sub(patterns['link'], substitutes['link'], content, 1)
            return newline
        if tag == 'image':
            newline = re.sub(patterns['link'], substitutes['img'], content, 1)
            return newline

        if tag in subtags:
            tag = subtags[tag]
        return '<'+tag+'>' + content + '</'+tag+'>'

    def parseTag(self, line):
        result = re.search(patterns['tag'], line)

        tag = result.group(2)
        content = result.group(3)
        
        print("Processing", tag, "\t", content)

        processed = self.processTag(tag, content)
        newline = re.sub(patterns['tag'], processed, line, 1)
        return newline
    
    def parseline(self, line):
        if len(line) > 0 and line[0] == '%':
            self.parsed += line[1:] + '\n'
        elif re.match(patterns['setter'], line):
            self.parseSetter(line)
        else:
            while re.search(patterns['tag'], line):
                line = self.parseTag(line)

            self.parsed += line + '\n'
