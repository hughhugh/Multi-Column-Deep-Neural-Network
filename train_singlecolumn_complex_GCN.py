from pylearn2.config import yaml_parse

with open("yaml/singlecolumn_complex_GCN.yaml", 'r') as f:
    train = f.read()
train = yaml_parse.load(train)
train.main_loop()