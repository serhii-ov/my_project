class Frame:

    def __init__(self, scores, throw_one, throw_two, frame, total_scores):
        self.scores = scores
        self.throw_one = throw_one
        self.throw_two = throw_two
        self.frame = frame
        self.total_scores = total_scores
        self.skittles = list(range(11))
        self.frame_types = {'1': 'open', '2': 'spare', '3': 'strike'}

    def one_frame(self):
        self.throw_one = int(input('Input digit from 0 to 10: '))
        if (self.throw_one or self.throw_two) not in self.skittles:
            print('Incorrect input!')
            raise ValueError('Input digit from 0 to 10: ')
        self.scores = self.throw_one
        self.throw_two = 0
        if self.throw_one < 10:
            self.throw_two = int(input('Input digit from 0 to 10: '))
            self.scores = self.throw_one + self.throw_two
        return '({} + {}) => {}'.format(self.throw_one, self.throw_two, self.scores)

    def frame_name(self):
        if self.throw_one > 9:
            self.scores = 10 + self.throw_one + self.throw_two
            name = self.frame_types['3']
        elif (self.throw_one + self.throw_two) == 10:
            self.scores = 10 + self.throw_one
            name = self.frame_types['2']
        else:
            self.scores = self.throw_one + self.throw_two
            name = self.frame_types['1']
        self.frame += 1
        return 'Frame {}: {}({})'.format(self.frame, self.scores, name)

    def scores_storage(self):
        self.total_scores += self.scores
        return 'Scores: {}'.format(self.total_scores)


class Game(Frame):

    def scores_board(self):
        pass


def on_play():
    player = Game(0, 0, 0, 0, 0)
    counter = 0
    while counter < 10:
        counter += 1
        print(player.one_frame())
        print(player.frame_name())
        player.scores_storage()
    print(player.scores_storage())


on_play()



