class Scanner:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []

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
