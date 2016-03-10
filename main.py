#!/usr/bin/env python3


file = open('test.mp3', 'rb')
# This should create a bytes immutable object
bytes_ = file.read()
# How long is the file?
print(len(bytes_))


def mp3seek(bytes_):
    """Skips to important part of mp3 stream.

    This will take a byte stream and return
    a trimmed version of it that will have
    all metadata (ID3 tags, etc) fast-forwarded.
    Args:
        bytes_ (bytes): A bytes mp3 file stream.

    Returns:
        bytes: The trimmed version of the mp3 stream with
        all metadata at the beginning trimmed.

    Raises:
        TODO: e.g.
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
    # TODO:
    bytes__ = bytes(0)
    return bytes__


def mp3_unpack_frame(bytes_):
    """Unpacks a single logical frame.

    Args:
        bytes_ (bytes): An mp3 bytes stream

    Returns:
        (bytes__ (bytes), frame (bytes)): This is
        a tuple of the mp3 stream fast-forwarded
        by one logical frame and the extracted
        logical frame.

    Raises:
        TODO:
    """
    bytes__ = frame = bytes(0)
    return (bytes__, frame)
