from pkg_resources import resource_filename

def test():
    with open(resource_filename(__name__, 'data/info.txt')) as f:
        print(f.read())
