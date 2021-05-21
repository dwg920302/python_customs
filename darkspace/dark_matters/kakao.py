class Kakao:
    def __init__(self, name, msg):  # parameter
        self.name = name
        self.msg = msg

    def send(self):
        return self.msg