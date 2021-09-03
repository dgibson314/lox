import sys

from scanner import Scanner

class Lox:
    had_error = False

    def main(self):
        if len(sys.argv) > 1:
            print("Usage: jlox [script]")
        elif len(sys.argv) == 1:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()

    def run_file(path):
        pass

    def run_prompt(self):
        while True:
            line = input("> ")
            if (line == null):
                break
            self.run(line)
            self.had_error = False

    def run(self, source):
        scanner = Scanner(source)
        pass

    def error(self, line, message):
        self.report(line, "", message)

    def report(self, line, where, message):
        print(f"[{line}] ERROR {where}: {message}")
        self.had_error = True
