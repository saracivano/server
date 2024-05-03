import subprocess

class Runner:
    def __init__(self, cmd: str, text: str):
        self.process = None
        self.cmd = cmd
        self.text = text
    
    def run(self):
        self.process = subprocess.Popen(
            self.cmd.format(file=self.text),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

class Python(Runner):
    def __init__(self):
        super().__init__("py -m {file}")

class Program:
    def __init__(self, runner, text: str):
        runner.run()