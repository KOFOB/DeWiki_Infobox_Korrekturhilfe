"""
This files contains the most simple checks to determine if there even can be a handmade-infobox
"""
import re


# Checks whether there is a raw wiki table in the article by checking for "{|"
def check_for_table(self):
    # Make a copy, so we only change the copy as we will maybe later still need the full wikitext
    copy = self.wiki_text.copy()

    # Define a regular expression pattern to match "<math> ... </math>" to remove math, as there are
    # also substrings of the form "{|" or "|}", which we want to ignore if they are not part of a wikitable
    pattern = r'<math>.*?</math>'

    # Use re.sub() to replace the matched pattern with an empty string
    copy = re.sub(pattern, '', copy)

    return True if "{|" in copy else False
