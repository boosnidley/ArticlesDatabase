# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database

from example_queries import cnn_example_query

dbname = get_database()
articles = dbname["articles"]
 
# item_details = articles.find()
# for item in item_details:
#    # This does not give a very readable output
#    print(item)

cnn_example_query(articles)

print("Exiting")