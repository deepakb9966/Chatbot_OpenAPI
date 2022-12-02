import os
import random
import json
import pickle
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

import connexion
import numpy as np
import nltk
from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from google.protobuf.json_format import MessageToJson, MessageToDict

from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
words = pickle.load(open('/workspaces/Chatbot_OpenAPI/openapi/server/openapi_server/words.pkl', 'rb'))
labels = pickle.load(open('/workspaces/Chatbot_OpenAPI/openapi/server/openapi_server/labels.pkl', 'rb'))
intents = json.loads(open('/workspaces/Chatbot_OpenAPI/openapi/server/openapi_server/intents.json').read())
model = load_model('/workspaces/Chatbot_OpenAPI/openapi/server/openapi_server/chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bagofwords(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bagofwords(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': labels[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(message):
    intents_list = predict_class(message)
    prob = float(intents_list[0]['probability'])
    tag = intents_list[0]['intent']
    # print(tag,end="0000")
    # print(prob)
    # print(tag)
    list_of_intents = intents['intents']
    if prob > 0.8:
        for i in list_of_intents:
            # print(i['tag'])
            if i['tag'] == tag:
                return random.choice(i['responses'])
            # print(result)
    return "sorry! I didn't get you..."


def predict_intent(message_u):
    text = message_u
    # TODO: check if the text is valid
    text = text.lower()
    response = get_response(text)
    ints = predict_class(text)
    prob = float(ints[0]['probability'])
    intent = ints[0]['intent']
    message = {'answer': response}
    if response == 'your appointment was confirm':
        message = {'answer': 'tell me a bit about you!enter your name'}
        return (message)
    else:
        return (message)


print(predict_intent('hi'))
