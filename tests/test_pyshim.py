#!/usr/bin/env python
# encoding: utf-8


"""Testing of the functionality contained in the shim library."""

import unittest
import subprocess
from os.path import join, dirname, pardir, abspath


SHIM = abspath(join(dirname(__file__), pardir, "pyshim", "pyshim.so"))


class WriterInterception(unittest.TestCase):
    """An end to end test."""

    def test_permits_passthru(self):
        CMDLINE = ["/usr/bin/env", "PERMIT=1", "LD_PRELOAD=" + SHIM, "/usr/bin/env", "echo", "testing..."]
        output = subprocess.check_output(CMDLINE, stderr=subprocess.STDOUT)
        self.assertIn("testing...", output)

    def test_prevents_passthru(self):
        CMDLINE = ["/usr/bin/env", "LD_PRELOAD=" + SHIM, "/usr/bin/env", "echo", "testing..."]
        try:
            output = subprocess.check_output(CMDLINE, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            pass
        else:
            self.fail("Unexpectedly permitted passthrough")


if __name__ == "__main__":
    unittest.main()

