
def date_query(container , date):
  dateQuery = { "date": date }
  results = container.find(dateQuery)
  return [record for record in results]