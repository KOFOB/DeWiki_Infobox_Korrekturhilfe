# This class checks given wikitext if it contains a self-made infobox
import re

from extractor import extract_wikitext


class Checker:
    def __int__(self, article_name, wiki_text):
        self.article_name = ""
        self.wiki_text = extract_wikitext(article_name)

    # Checks whether there is a raw wiki table in the article
    def check_for_table(self):
        copy = self.wiki_text.copy()

        # Define a regular expression pattern to match "<math> ... </math>" to remove math, as there are
        # also substrings of the form "{|" or "|}", which we want to ignore
        pattern = r'<math>.*?</math>'

        # Use re.sub() to replace the matched pattern with an empty string
        copy = re.sub(pattern, '', copy)

        if copy.contains("{|"):
            return True
        return False
