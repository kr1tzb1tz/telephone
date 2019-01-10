from flask import render_template, flash, redirect
from app import app, db
from app.forms import AnswerForm
from app.models import Statement
from random import *
from watson_developer_cloud import LanguageTranslatorV3
import json

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
]


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    form = AnswerForm()
    return render_template('index.html', form=form)

@app.route('/original_statements', methods=['GET'])
def original_statements():
    return json.dumps(str(STATEMENTS))

@app.route('/new_telephone', methods=['GET'])
def new_telephone():
    language_translator = LanguageTranslatorV3(version='2018-05-01', 
    iam_apikey='IO4rsVgzT9k93HBxoZIxqVvHLWpOGTOsrQ_6p0GL0bbf',
    url='https://gateway.watsonplatform.net/language-translator/api')

    statement = Statement.query.get(randint(1, 55))

    translation_spanish = language_translator.translate(
        text=statement.original,
        model_id='en-es').get_result()

    translation_french = language_translator.translate(
        text=translation_spanish['translations'][0]['translation'],
        model_id='es-fr').get_result()

    translation_german = language_translator.translate(
        text=translation_french['translations'][0]['translation'],
        model_id='fr-de').get_result()

    translation_italian = language_translator.translate(
        text=translation_german['translations'][0]['translation'],
        model_id='de-it').get_result()

    back_to_english = language_translator.translate(
        text=translation_italian['translations'][0]['translation'],
        model_id='it-en').get_result()

    back_to_english['original'] = statement.original

    print(json.dumps(back_to_english, indent=2, ensure_ascii=False))
    return json.dumps(back_to_english, indent=2, ensure_ascii=False)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    form = AnswerForm()
    if form.validate_on_submit():
        print("original " + form.original.data)
        print("answer " + form.answer.data)
        if form.original.data == form.answer.data:
            flash('Correct!')
            print("Correct input!")
        else:
            flash('Wrong!')
            print("Incorrect input!")
    return render_template('index.html', form=form)
