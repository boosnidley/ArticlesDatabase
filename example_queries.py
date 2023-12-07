# example query: print all articles published by CNN
def cnn_example_query()
  cnnquery = { "publisher": "CNN" }
  cnndocs = articles.find(cnnquery)
  for x in cnndocs:
    print(x)
