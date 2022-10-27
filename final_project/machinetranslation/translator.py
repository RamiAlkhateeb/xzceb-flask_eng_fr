"""
docstring
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
#print(apikey)
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
# translation = language_translator.translate(
#     text='Hello, how are you today?',
#     model_id='en-fr').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))
"""
"""
def english_to_french(englishtext):
    #write the code here
    if not englishtext: return None
    frenchtext = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return frenchtext['translations'][0]['translation']

"""
"""
def french_to_english(frenchtext):
    if not frenchtext: return None
    englishtext = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    return englishtext['translations'][0]['translation']

#print(french_to_english("Bonjour"))
