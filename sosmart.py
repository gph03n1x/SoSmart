from flask import Flask, render_template, request
from nltk.corpus import wordnet, stopwords

app = Flask(__name__)
STOP_WORDS = set(stopwords.words('english'))


def iamsosmart(sentence):
    retval = ''
    for word in sentence.split():
        longest_word = word
        if word.lower() not in STOP_WORDS:
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    l = l.name()
                    if '_' in l:
                        continue
                    if len(l) > len(longest_word):
                        longest_word = l
        retval += f' {longest_word}'
    return retval.strip()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def results():
    so_smart = ""
    if request.form:
        sentence = request.form.get("sentence")
        so_smart = iamsosmart(sentence)
    return render_template('response.html', so_smart=so_smart)
