import os
from typing import List

class MarkdownToTrello:
    def __init__(self, text):
        self.text = text

    def convert_to_cards(self) -> List['Card']:
        return [Card(self.text)]


Command = str

class SaveCards:
    def dry_run(self, cards: List['Card']) -> List[Command]:
        board = "Jeans Life"
        lane = "Inbox"
        description = ''
        position = 'top'
        title = cards[0].title
        cmd = f'trello add-card -b "{board}" -l "{lane}" "{title}" "{description}" -q {position}'

        return [cmd]


    def perform(self, cards: List['Card']):
        commands = self.dry_run(cards)
        for command in commands:
            os.system(command)







class Card:
    def __init__(self, title):
        self.title = title
