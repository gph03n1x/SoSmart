from flask import Flask, render_template, request
from nltk.corpus import wordnet, stopwords

app = Flask(__name__)
STOP_WORDS = set(stopwords.words('english'))
LEMMA_LANGUAGE_CODE = 'eng'


def generate_smarter_sentence(sentence: str) -> str:
    smarter_sentence = " ".join([
        find_smarter_word(word) if word.lower() not in STOP_WORDS else word
        for word in sentence.split()
    ])
    return smarter_sentence


def maintain_capitalization(new_word: str, old_word: str) -> str:
    new_word = new_word.lower()

    if old_word and old_word.isupper():
        return new_word.upper()
    elif old_word and old_word[0].isupper():
        return new_word.title()
    return new_word


def find_smarter_word(word: str) -> str:
    available_lemmas = [
        (len(lemma),  lemma)
        for syn_set in wordnet.synsets(word)
        for lemma in syn_set.lemma_names(lang=LEMMA_LANGUAGE_CODE)
        if '_' not in lemma and '-' not in lemma
    ]
    available_lemmas += [
        (len(word), word)
    ]
    new_word = max(available_lemmas)[1]
    new_word = maintain_capitalization(new_word, word)
    return new_word


@app.route('/', methods=['GET'])
def index() -> str:
    return render_template('index.html')


@app.route('/', methods=['POST'])
def results() -> str:
    so_smart = ""
    if request.form:
        sentence = request.form.get("sentence")
        so_smart = generate_smarter_sentence(sentence)

    return render_template('index.html', so_smart=so_smart)
