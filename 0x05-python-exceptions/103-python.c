#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info -> Prints some basic info about Python lists
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	int i = 0;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while (i < PyList_Size(p))
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}

/**
 * print_python_bytes -> Prints some basic info about Python bytes
 * @p: PyObject
 */

void print_python_bytes(PyObject *p)
{
	int i = 0;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	if (PyBytes_Size(p) > 10)
		printf("  first 10 bytes: ");
	else
		printf("  first %ld bytes: ", PyBytes_Size(p));
	str = PyBytes_AsString(p);
	while (i < PyBytes_Size(p) + 1 && i < 10)
	{
		if (i == PyBytes_Size(p) || i == 9)
			printf("%02x\n", str[i] & 0xff);
		else
			printf("%02x ", str[i] & 0xff);
		i++;
	}
}

/**
 * print_python_float -> Prints some basic info about Python float
 * @p: PyObject
 */

void print_python_float(PyObject *p)
{
	char *str;
	double d;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	d = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * main - Entry point
 * Return: 0 on success
 */

int main(void)
{
	PyObject *p;
	PyObject *f;
	PyObject *b;

	setbuf(stdout, NULL);
	p = PyList_New(0);
	PyList_Append(p, Py_BuildValue("i", 0));
	PyList_Append(p, Py_BuildValue("i", 1));
	PyList_Append(p, Py_BuildValue("i", 2));
	PyList_Append(p, Py_BuildValue("i", 3));
	PyList_Append(p, Py_BuildValue("i", 4));
	PyList_Append(p, Py_BuildValue("i", 5));
	print_python_list_info(p);
	PyList_SetItem(p, 4, Py_BuildValue("i", 99));
	print_python_list_info(p);

	b = PyBytes_FromString("Hello, Holberton");
	print_python_bytes(b);
	f = PyFloat_FromDouble(3.14);
	print_python_float(f);

	return (0);
}
