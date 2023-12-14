from helper import print_articles

def publisher_query(container, publisher):
  publisherQuery = { "publisher": publisher }
  docs = container.find(publisherQuery)
  print_articles(docs)
