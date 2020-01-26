from toqito.helper.constants import e0, e1
from toqito.states.bell import bell

import itertools
import unittest
import numpy as np


class TestBell(unittest.TestCase):
    """Unit test for gen_bell."""

    def test_bell_0(self):
        expected_res = 1/np.sqrt(2) * (np.kron(e0, e0) + np.kron(e1, e1))

        res = bell(0)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(all(x == 1 for x in itertools.chain(*bool_mat)), True)

    def test_bell_1(self):
        expected_res = 1/np.sqrt(2) * (np.kron(e0, e0) - np.kron(e1, e1))

        res = bell(1)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(all(x == 1 for x in itertools.chain(*bool_mat)), True)

    def test_bell_2(self):
        expected_res = 1/np.sqrt(2) * (np.kron(e0, e1) + np.kron(e1, e0))

        res = bell(2)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(all(x == 1 for x in itertools.chain(*bool_mat)), True)

    def test_bell_3(self):
        expected_res = 1/np.sqrt(2) * (np.kron(e0, e1) - np.kron(e1, e0))

        res = bell(3)

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(all(x == 1 for x in itertools.chain(*bool_mat)), True)

    def test_bell_invalid(self):
        with self.assertRaises(ValueError):
            bell(4)


if __name__ == '__main__':
    unittest.main()