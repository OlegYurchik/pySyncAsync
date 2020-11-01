class Generator:
    def __init__(self, generator):
        self.generator = generator
        self.result = None

    def __iter__(self):
        self.result = yield from self.generator
