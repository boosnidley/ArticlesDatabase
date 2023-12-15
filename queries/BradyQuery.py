from helper import print_articles

def tag_query(container , tag):
  tagQuery = { "tags": { "$regex": tag, "$options": "i" } }
  docs = container.find(tagQuery)
  print_articles(docs)