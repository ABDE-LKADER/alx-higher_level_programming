#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *bytes = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  [.] size: %ld\n", size);
    printf("  [.] trying string: %s\n", bytes);

    if (size > 10) {
        size = 10;
    }

    printf("  [.] first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02hhx", bytes[i]);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
