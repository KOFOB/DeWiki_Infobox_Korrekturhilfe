# This part of the script just does the most simple checks to see whether an article is even a candidate

import requests
import mwparserfromhell


# Given the name of the article this method saves the content in wiki-text format in a String
def get_content(article_name):
    response = requests.get(
        'https://de.wikipedia.org/w/api.php',
        params={
            'action': 'query',
            'format': 'json',
            'titles': 'article_name',
            'prop': 'revisions',
            'rvprop': 'content', }).json()
    print(response['query']['pages'].values())


# Checks whether there is a raw wiki table in the article as we only want to replace those with infoboxes, if possible
def check_for_table(article):
    print("Placeholder again")
