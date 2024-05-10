from os.path import getsize, isdir, join
from os import listdir, getcwd

def disk_usage(path):
    """Returns the cumulative total disk space used by the given path"""
    total_size = getsize(path)
    if isdir(path):
        for filename in listdir(path=path):
            total_size += disk_usage(join(path, filename))
    
    print('{0:<7}'.format(total_size), path)
    return total_size


print(disk_usage(getcwd()))