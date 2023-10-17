import extractor
import simple_check


def main():
    # TODO add toggle to determine whether we should extract_articles()
    # extractor.extract_articles()
    # TODO add interface to work off each article one by one
    wikitext = extractor.extract_wikitext("Frankreich")
    simple_check.check_for_table(wikitext)


if __name__ == "__main__":
    main()
