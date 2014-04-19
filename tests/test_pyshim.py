#!/usr/bin/env python
# encoding: utf-8


"""Testing of the functionality contained in the shim library."""

import unittest
import subprocess

from os.path import join, dirname, pardir, abspath


class WriterInterception(unittest.TestCase):
    """An end to end test."""

    def test_echos_write_output_to_stderr(self):
        shim = abspath(join(dirname(__file__), pardir, "pyshim", "pyshim.so"))
        cmdline = ["/usr/bin/env", "LD_PRELOAD=", shim, "python", "-V"]
        output = subprocess.check_output(cmdline, stderr=subprocess.STDOUT)
        self.assertIn("dont know yet", output)


if __name__ == "__main__":
    unittest.main()

