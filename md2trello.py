#!/usr/bin/env python
import sys
from markdown_to_trello.markdown_to_trello import MarkdownToTrello, SaveCards

content = sys.stdin.read()
cards = MarkdownToTrello(content).convert_to_cards()

SaveCards(board = "Jeans Life", lane = "Today").perform(cards)

