from random import randint
class game(object):
    def __init__(self):
        self.pos = 0
        self.dice = 4
        self.doubles = 0
        self.nfields = 40
        self.nvisited = [0] * self.nfields
        self.n = 0
        self.cc = {}
        self.ch = {}
        self.cc_moves = (0, 10)
        self.ch_moves = (0, 10, 11, 24, 39, 5, 'R', 'R', 'U', -3)
        self.shuffle()
        print self.cc
        print self.ch

    def play(self, moves):
        i = self.n
        while self.n < i + moves:
            self.advance()

    def advance(self):
        a = randint(1, self.dice)
        b = randint(1, self.dice)
        if a == b:
            self.doubles += 1
        else:
            self.doubles = 0
        if self.doubles == 3:
            self.doubles = 0
            self.pos = 10
        else:
            self.pos += a + b
        self.pos = self.pos % self.nfields
        if self.pos in (7, 22, 36):
            self.pick_card('ch')
        if self.pos in (2, 17, 33):
            self.pick_card('cc')
        if self.pos == 30:
            self.pos = 10

        # print self.pos
        self.nvisited[self.pos] += 1
        self.n += 1

    def shuffle(self):
        self.icc = 0
        self.ich = 0
        for i in self.cc_moves:
            while True:
                r = randint(0, 15)
                if r not in self.cc:
                    break
            self.cc[r] = i

        for i in self.ch_moves:
            while True:
                r = randint(0, 15)
                if r not in self.ch:
                    break
            self.ch[r] = i


    def pick_card(self, cardType):
        d = None
        if cardType == 'cc':
            if self.icc in self.cc:
                d = self.cc[self.icc]
            self.icc = (self.icc + 1) % 16
        else:
            if self.ich in self.ch:
                d = self.ch[self.ich]
            self.ich = (self.ich + 1) % 16

        if d is not None:
            if type(d) == int:
                if d >= 0:
                    self.pos = d
                else:
                    self.pos = (self.pos + d) % self.nfields
            else:
                if d == 'R':
                    while self.pos not in (5, 15, 25, 35):
                        self.pos = (self.pos + 1) % self.nfields
                if d == 'U':
                    while self.pos not in (12, 28):
                        self.pos = (self.pos + 1) % self.nfields

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


for i in range(4):
    monopoly = game()
    monopoly.play(1000000)
    print monopoly.nvisited
    ind = argsort(monopoly.nvisited)
    print ind[-5:]
    if i == 0:
        res = monopoly.nvisited
    for j in range(monopoly.nfields):
        res[j] += monopoly.nvisited[j]
print argsort(res)[-3:]
