from pkg_resources import resource_string

def test():
    with open(resource_string(__name__, 'info.txt')) as f:
        print(f.read())
