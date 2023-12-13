# Prints the list of articles in a nice format to the console
def print_articles(articles):
    print("Here are the results:\n")
    for article in articles:
        print(f"Title: \t\t{article['title']}")
        print(f"Author(s): \t{article['authors']}")
        print(f"Publisher: \t{article['publisher']}")
        print(f"Date: \t\t{article['date']}")
        print(f"Topics: \t{article['tags']}\n")