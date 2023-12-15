# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database

# Import the queries
from queries.TylerQuery import date_query
from queries.BradyQuery import tag_query
from queries.IanQuery import publisher_query
from helpers import print_articles, bookmark_article

# Initialize database connection
dbname = get_database()
articles = dbname["articles"]
bookmarks = dbname["bookmarks"]

# Main program loop
while(True):
    print("Welcome to NewsQuery! Choose one of the following options:")
    print("(1) Query news articles by date.")
    print("(2) Query news articles by topic.")
    print("(3) Query news articles by publisher.")
    print("(4) View bookmarked articles.")
    print("(q) Quit.")

    response = input()

    if(response == '1'):
        date = input("Enter the date you want to search by in the following format: yyyy-mm-dd\n")
        try:
            results = date_query(articles, date)
            print_articles(results)
            bookmark_article(results, bookmarks)
        except:
            print("Failure. Ensure the date format was correct and you have a network connection.")
    elif(response == '2'):
        topic = input("Enter the topic you want to search by\n")
        try:
            results = tag_query(articles, topic)
            print_articles(results)
            bookmark_article(results, bookmarks)
        except:
            print("Failure. Ensure you have a network connection.")
    elif(response == '3'):
        publisher = input("Enter the publisher you want to search by\n")
        try:
            results = publisher_query(articles, publisher)
            print_articles(results)
            bookmark_article(results, bookmarks)
        except:
            print("Failure. Ensure you have a network connection.")
    elif(response == '4'):
        try:
            print_articles(bookmarks.find())
        except:
            print("Failure. Ensure you have a network connection.")
    elif(response =='q'):
        break

print("Thank you!")
