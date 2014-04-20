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

    [user@host ~]$ env LD_PRELOAD=pyshim/pyshim.so env echo Hi
    Refusing execvp
    env: echo: No such file or directory

    [user@host ~]$ env PERMIT=1 LD_PRELOAD=pyshim/pyshim.so env echo Hi
    Looking up real execvp
    Found real execvp, now delegating
    Hi

