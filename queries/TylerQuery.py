from helper import print_articles

def date_query(container , date):
  dateQuery = { "date": date }
  docs = container.find(dateQuery)
  print_articles(docs)