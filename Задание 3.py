class test_me:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'I am instance of test_me Class'

    def __eq__(self, other):
        if isinstance(other, test_me):
            return self.name == other.name
        return NotImplemented
