class Scanner:
    start = 0
    current = 0
    line = 1
    tokens = []

    def __init__(self, source):
        self.source = source

    def scan_tokens():
        pass

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def is_at_end(self):
        return self.current >= len(self.source)
