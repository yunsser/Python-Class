class ChatMsg:
    def __init__(self, contents, to=None, frm=None, attach=None):
        self.contents = contents
        self.to = to
        self.frm = frm
        self.attach=attach
    def __str__(self):
        return "contents={}, from={}, to={}".format(self.contents, self.to, self.frm)
