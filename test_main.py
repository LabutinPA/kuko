import unittest
import main


class TestMain(unittest.TestCase):

    def test_byte_to_bit(self):
        self.assertEqual(main.byte_to_bit(0), [0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(main.byte_to_bit(4), [0, 0, 0, 0, 0, 1, 0, 0])
        self.assertEqual(main.byte_to_bit(255), [1, 1, 1, 1, 1, 1, 1, 1])
        with self.assertRaises(AssertionError):
            main.byte_to_bit(-1)
        with self.assertRaises(AssertionError):
            main.byte_to_bit(256)

    def test_bytes_to_bits(self):
        bytestream0 = bytes(2)
        bytestream1 = bytes([255, 255])
        bytestream2 = bytes([20, 47])
        list0 = []
        [list0.append(0) for x in range(16)]
        list1 = []
        [list1.append(1) for x in range(16)]
        list2 = [0, 0, 0, 1, 0, 1, 0, 0,
                 0, 0, 1, 0, 1, 1, 1, 1]
        self.assertEqual(main.bytes_to_bits(bytestream0), list0)
        self.assertEqual(main.bytes_to_bits(bytestream1), list1)
        self.assertEqual(main.bytes_to_bits(bytestream2), list2)
