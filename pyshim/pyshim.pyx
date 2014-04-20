"""An experiment in shimming from Cython / Python."""


cdef extern from "dlfcn.h":
    void* dlsym(void*, char*)
    void* RTLD_NEXT


cdef extern int execvp(const char *file, char *const argv[]) with gil:
    print "Intercepted lookup of %r" % file
    libc_execvp = dlsym(RTLD_NEXT, "execvp")
    if libc_execvp:
        with nogil:
            return (<int(*)(const char*, char * const *) nogil>libc_execvp)(file, argv)
    return -1

