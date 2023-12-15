# Prints the list of articles in a nice format to the console
def print_articles(articles):
    print("Here are the results:\n")
    i = 1
    for article in articles:
        print("Result " + str(i) + ":")
        print(f"Title: \t\t{article['title']}")
        print(f"Author(s): \t{article['authors']}")
        print(f"Publisher: \t{article['publisher']}")
        print(f"Date: \t\t{article['date']}")
        print(f"Topics: \t{article['tags']}\n")
        i += 1

# Code to bookmark an article. Makes life in the main loop easier
def bookmark_article(article_list, container):
    index = input("To bookmark an article, enter its number from the list above. (q to skip).\n")
    if(index != 'q'):
        try:
            container.insert_one(article_list[int(index) - 1])
            print("Bookmark successfully added.")
        except:
            print("Error occurred. Bookmark not added. Perhaps your index was out of range or you already bookmarked that article.")