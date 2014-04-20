"""An experiment in shimming from Cython / Python."""

import os


cdef extern from "dlfcn.h":
    void* dlsym(void*, char*)
    void* RTLD_NEXT


cdef extern from "Python.h":
    void Py_Initialize() nogil


cdef extern void initpyshim()


cdef int real_execvp(const char *file, char *const argv[]):
    """Hand off to the real execvp."""
    print "Looking up real execvp"
    libc_execvp = dlsym(RTLD_NEXT, "execvp")
    if libc_execvp:
        print "Found real execvp, now delegating"
        with nogil:
            return (<int(*)(const char*, char * const *) nogil>libc_execvp)(file, argv)


cdef extern int execvp(const char *file, char *const argv[]) nogil:
    """Intercept execvp and decide whether to permit."""
    Py_Initialize()
    with gil:
        initpyshim()
        if "PERMIT" in os.environ:
            return real_execvp(file, argv)
        else:
            print "Refusing execvp"
            return -1

