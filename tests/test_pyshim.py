#!/usr/bin/env python
# encoding: utf-8


"""Testing of the functionality contained in the shim library."""

import unittest
import subprocess
from os.path import join, dirname, pardir, abspath


SHIM = abspath(join(dirname(__file__), pardir, "pyshim", "pyshim.so"))
CMDLINE = ["/usr/bin/env", "LD_PRELOAD=" + SHIM, "/usr/bin/env", "echo"]


class WriterInterception(unittest.TestCase):
    """An end to end test."""

    def test_intercepts_call_and_produces_intercepted_output(self):
        output = subprocess.check_output(CMDLINE, stderr=subprocess.STDOUT)
        self.assertIn("Intercepted lookup of", output)


if __name__ == "__main__":
    unittest.main()

