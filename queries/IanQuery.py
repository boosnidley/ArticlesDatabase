from helper import print_articles

def publisher_query(container, publisher):
  publisherQuery = { "publisher": { "$regex": publisher, "$options": "i" } }
  docs = container.find(publisherQuery)
  print_articles(docs)
