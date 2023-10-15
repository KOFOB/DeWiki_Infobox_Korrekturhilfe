# This class checks given wikitext if it contains a self-made infobox
from extractor import extract_wikitext


class Checker:
    def __int__(self, article_name, wiki_text):
        self.article_name = ""
        self.wiki_text = extract_wikitext(article_name)

    # Checks whether there is a raw wiki table in the article
    def check_for_table(self):
        if self.wiki_text.contains("wikitable"):
            return True
        return False
