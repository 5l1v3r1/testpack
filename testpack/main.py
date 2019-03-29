import os

def test():
    with open(os.path.join(os.path.dirname(__file__), 'info.txt')) as f:
        print(f.read())
