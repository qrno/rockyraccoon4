from line import Line, LineType
from fileio import savefile

class File:
    def __init__(self, path, raw):
        self.path = path
        self.raw = raw
        self.attributes = {}

        self.lines = []
        for line in raw:
            self.lines.append(self.parseline(line))

    def parseline(self, line):
        words = line.split(' ')
        if words[0] == '[':
            print('Set', words[1], 'to', words[2])
            self.attributes[words[1]] = words[2]
            return Line(LineType.Attribute, line)
        return Line(LineType.Content, line)
        

    def writefile(self, outdir):
        if not 'slug' in self.attributes:
            print("File has no name")
        else:
            savefile(outdir, self.attributes['slug'], self.get_html())

    def get_html(self):
        result = ""
        for line in self.lines:
            if line.type == LineType.Content:
                result += line.content + '\n'

        return '<html>' + result + '</html>'
