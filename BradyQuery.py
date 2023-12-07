def tag_example_query(container)
  tagquery = { "tag": "politics" }
  politicsdocs = container.find(tagquery)
  for x in politicsdocs:
    print(x)
