PyShim
======

An experiment; can i make an LD_PRELOADable shim with Cython?


Getting Started
===============

Install dependencies then install this python package in "editable" mode::

    (pyshim)[user@host pyshim]$ pip install --requirement requirements.txt
    (pyshim)[user@host pyshim]$ pip install --editable .

To rebuild the .so i run::

    [user@host ~]$ python setup.py build_ext --inplace

To use the .so to intercept library calls i run::

    [user@host ~]$ LD_PRELOAD=pyshim/pyshim.so dd if=/dev/zero of=/dev/null count=1

