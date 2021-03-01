labels = ['pomogranate' , 'plum' , 'tomato']
img_size = 224
def get_data(data_dir):
  data = []
  for label in labels:
    path = os.path.join(data_dir, label) ...
