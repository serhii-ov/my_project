class Frame:
    frame = 0

    def __init__(self, scores):
        self.scores = scores

    def skittles(self):
        throw_ = int(input('Input number from 0 to 10: '))
        if throw_ < 10:
            throw_two = int(input('Input number from 0 to 10: '))
            return throw_, throw_two
        return throw_

    def frame_state(self):
        if throw_ + throw_two < 10:
            return False
        return True

    def scores_storage(self):
        scores = throw_ + throw_two
        return scores


class Game(Frame):

    frame_types = {'1': 'open', '2': 'spare', '3': 'strike'}

    def scores_board(self):
        super().skittles()
        return ('{}  {}'.format( throw_, throw_two))

def on_play():
    pass

player = Game(scores=0)
print(player.skittles())
print(player.scores_board())



