import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2023-02-05',authenticator=authenticator)
language_translator.set_service_url(url)

translation = language_translator.translate(text='Hello, how are you today?',model_id='en-fr').get_result()

def englishtofrench(word):
    """This class does english to french translation"""
    url_lt=url
    apikey_lt=apikey
    version_lt='2023-02-05'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    try:
        word=""
    except:
        print("Please enter a word")

    return translation['translations'][0]['translation']

def englishtogerman(word):
    """This class does english to german translation"""
    url_lt=url
    apikey_lt=apikey
    version_lt='2023-02-05'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-de").get_result()
    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    """This class does french to english translation"""
    url_lt=url
    apikey_lt=apikey
    version_lt='2023-02-05'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()
    try:
        word=""
    except:
        print("Please enter a word")

    return translation['translations'][0]['translation']

def germantoenglish(word):
    """This class does german to english translation"""
    url_lt=url
    apikey_lt=apikey
    version_lt='2023-02-05'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=word, model_id="de-en").get_result()
    return translation['translations'][0]['translation']    