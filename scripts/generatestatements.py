import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app import app, db
from app.models import Statement

STATEMENTS = [
    "Let’s hang out tonight.",
    "I’ll fix you up.",
    "It’s up to you.",
    "Don’t get me wrong.",
    "Suit yourself.",
    "Get real.",
    "Freedom is not free.",
    "No pains, no gains.",
    "Money doesn’t grow on trees.",
    "It’s never too late to learn.",
    "It costs me an arm and a leg to buy this house.",
    "We’re in hot water.",
    "I’m hung up on this problem.",
    "You rained on my parade.",
    "He is a big baller.",
    "Let’s face the music.",
    "What’s your name?",
    "What’s wrong with you?",
    "Can you do me a favor?",
    "Could you please give me a ride?",
    "Where are you from?",
    "What’s your phone number?",
    "How come you never married?",
    "Where are you right now?",
    "Be careful.",
    "Be careful driving.",
    "Can you translate this for me?",
    "Chicago is very different from Boston.",
    "Don't worry.",
    "Everyone knows it.",
    "Everything is ready.",
    "Excellent.",
    "From time to time.",
    "Good idea.",
    "He likes it very much.",
    "Help!",
    "He's coming soon.",
    "He's right.",
    "He's very annoying.",
    "He's very famous.",
    "How are you?",
    "How's work going?",
    "Hurry!",
    "I ate already.",
    "I can't hear you.",
    "I'd like to go for a walk.",
    "I don't know how to use it.",
    "I don't like him.",
    "I don't like it.",
    "I don't speak very well.",
    "I don't understand.",
    "I don't want it.",
    "I don't want that.",
    "I don't want to bother you."
]

if __name__ == "__main__":
    for s in STATEMENTS:
        new_statement = Statement(original=s) 
        db.session.add(new_statement)
        db.session.commit()
