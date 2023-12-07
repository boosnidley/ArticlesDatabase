def tag_example_query(container , tag)
  tagquery = { "tags": tag }
  politicsdocs = container.find(tagquery)
  for x in politicsdocs:
    print(x)
