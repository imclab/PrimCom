import hashlib


def string_to_md5(content):
    """Calculate the md5 hash of a string.

    This 'string' can be the binary content of a file too."""
    return hashlib.md5(content).hexdigest()


def file_to_md5(filename, block_size=8192):
    """Calculate the md5 hash of a file. Memory-friendly solution,
    it reads the file piece by piece.

    https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python"""
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()
