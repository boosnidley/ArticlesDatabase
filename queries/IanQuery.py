
def publisher_query(container, publisher):
  publisherQuery = { "publisher": { "$regex": publisher, "$options": "i" } }
  results = container.find(publisherQuery)
  return [record for record in results]