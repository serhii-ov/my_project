class Bowling:

    def __init__(self, scores):
        self.scores = scores

    def one_frame(self, frame=0):
        frame += 1
        scores = int(input('Input number from 0 to 10: '))
        if scores > -1 and scores < 10:
            scores_two = int(input('Input number from 0 to 10: '))
            # frame += 1
            return ('Frame {}: {} + {}'.format(frame, scores, scores_two))
        elif scores == 10:
            return ('Frame {}: {}'.format(frame, scores))
        elif scores == '':
            print('You missed')
        else:
            print('Incorrect input!')
        # n += 1

    def frame_state(self):
        frame_name = {'one': 'open', 'two': 'spare', 'three': 'strike'}
        if scores == 10:
            return ('{}'.format(frame_name['three']))
        elif scores + scores_two > 10:
            return ('{}'.format(frame_name['two']))
        else:
            return ('{}'.format(frame_name['one']))
        # return frame_name[i]


player = Bowling(0)
counter = 0
while counter < 10:
    print(player.one_frame())
    print(player.frame_state())
    counter += 1



