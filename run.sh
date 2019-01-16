#!/usr/bin/env bash

python -m nltk.downloader wordnet
python -m nltk.downloader stopwords
gunicorn sosmart:app -w 1 -b 0.0.0.0:8080 --reload