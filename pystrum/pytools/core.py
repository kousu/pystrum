import collections, math

def flatten_collection(l):
    # https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten_collection(el)
        else:
            yield el

def humanize_filesize(filesize):
    """ show human readable file size

    Args:
        filesize ([type]): [description]

    Returns:
        [type]: [description]
    """
    sizes_list = ['B','KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']

    power = int(math.floor(math.log(filesize, 2)/10))
    return "%.3f%s" % (filesize/math.pow(1024, power), sizes_list[power])
