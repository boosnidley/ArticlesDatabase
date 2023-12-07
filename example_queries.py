# example query: print all articles published by CNN
def cnn_example_query(container):
  cnnquery = { "publisher": "CNN" }
  cnndocs = container.find(cnnquery)
  for x in cnndocs:
    print(x)
