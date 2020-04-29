import requests
import pymongo

def get_cat_facts():
    r = requests.get('https://cat-fact.herokuapp.com/facts/')
    return r.json()

def get_dog_facts():
    r = requests.get('https://dog-api.kinduff.com/api/facts?number=100')
    return r.json()
