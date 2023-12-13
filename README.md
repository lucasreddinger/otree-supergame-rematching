# supergames with random rematching

Here I have taken the "supergames" app from [otree-snippets](https://www.otreehub.com/projects/otree-snippets/). I attempt to add random rematching between supergames. I also add a variable to subsession that marks for debugging purposes when `subsession.group_randomly()` is executed. These changes are made in `__init__.py`.

  - expected behavior:
      - for each round with `subsession.period == 1`
          - randomly rematch participants
          - mark `subsession.rematched = True`
      - else
          - mark `subsession.rematched = False`
  - actual behavior:
      - for every round, participants are rematched.
      - however `subsession.rematched` is changed as expected!

[Please see my commit 174a979.](https://github.com/lucasreddinger/otree-supergame-rematching/commit/174a97903c9846140ad9ea91bf30d790523b5fd8)

