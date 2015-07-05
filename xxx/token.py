from rply.token import BaseBox

class BoxInt(BaseBox):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value
