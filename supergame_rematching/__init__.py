from otree.api import *


doc = """
Supergames consisting of multiple rounds each
"""


def cumsum(lst):
    total = 0
    new = []
    for ele in lst:
        total += ele
        new.append(total)
    return new


class C(BaseConstants):
    NAME_IN_URL = 'supergames'
    PLAYERS_PER_GROUP = None

    # first supergame lasts 2 rounds, second supergame lasts 3 rounds, etc...
    ROUNDS_PER_SG = [2, 3, 4, 5]
    SG_ENDS = cumsum(ROUNDS_PER_SG)
    # print('SG_ENDS is', SG_ENDS)
    NUM_ROUNDS = sum(ROUNDS_PER_SG)


class Subsession(BaseSubsession):
    sg = models.IntegerField()
    period = models.IntegerField()
    is_last_period = models.BooleanField()


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        sg = 1
        period = 1
        # loop over all subsessions
        for ss in subsession.in_rounds(1, C.NUM_ROUNDS):
            ss.sg = sg
            ss.period = period
            # 'in' gives you a bool. for example: 5 in [1, 5, 6] # => True
            is_last_period = ss.round_number in C.SG_ENDS
            ss.is_last_period = is_last_period
            if is_last_period:
                sg += 1
                period = 1
            else:
                period += 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class NewSupergame(Page):
    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.period == 1


class Play(Page):
    pass


page_sequence = [NewSupergame, Play]

