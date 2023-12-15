
def tag_query(container , tag):
  tagQuery = { "tags": { "$regex": tag, "$options": "i" } }
  results = container.find(tagQuery)
  return [record for record in results]