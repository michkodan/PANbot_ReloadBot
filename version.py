import os


def get_version():
    try:
        version = open(os.path.abspath('version.txt'), 'r')
        vs = version.read()
        return vs
    except Exception as e:
        return e


def set_version():
    try:
        new_version = float(get_version()) + 0.01
        version = open(os.path.abspath('version.txt'), 'w')
        version.write(str(round(new_version, 2)))
        version.close()
    except Exception as e:
        return e
