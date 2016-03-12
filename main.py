#!/usr/bin/env python3
import functools


def byte_to_bit(byte):
    """Converts an integer byte to a list of bits
    4 -> [0, 0, 0, 0, 0, 1, 0, 0]
    Args:
        byte (int): Value should be :math:`\in [0, 255]`.
    Returns:
        list of (int): The bits of the given byte.
        e.g. [0, 0, 0, 0, 0, 1, 0, 0]
    Raises:
        AssertionError: If byte is outside of :math:`[0,255]`
    """
    # TODO: Consider using list of boolean values instead for optimisation
    assert byte <= 255 and byte >= 0
    answer = []
    while(byte > 0):
        answer.append(byte % 2)
        byte //= 2
    # pad answer
    while(len(answer) < 8):
        answer.append(0)
    answer.reverse()
    return answer


def bytes_to_bits(bytes_):
    """Converts a byte stream to a list of bits
    bytes([4]) -> [0, 0, 0, 0, 0, 1, 0, 0]
    Args:
        bytes_ (bytes): A bytes stream
    Returns:
        list of (int): The bits of the given bytes stream.
        e.g. [0, 0, 0, 0, 0, 1, 0, 0]
    Raises:
        AssertionError: If byte is outside of :math:`[0,255]`
    """
    # TODO: Use list comprehension
    return functools.reduce(list.__add__, list(map(byte_to_bit, bytes_)))


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


def mp3_parse_main_data(frame):
    """Parses a logical frame into useful data

    """
    mp3data = bytes(0)
    return mp3data

if __name__ == '__main__':
    file = open('test.mp3', 'rb')
    # This should create a bytes immutable object
    bytes_ = file.read()
    # How long is the file?
    print(len(bytes_))
