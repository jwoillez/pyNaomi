import os


def path(dir):
    return os.path.join(os.environ['HOME'], f'Dropbox/{dir}')
