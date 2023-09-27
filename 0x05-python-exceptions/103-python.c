#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - a function that prints information
 * about python float
 * @p: the address of python object struct
 */
void print_python_float(PyObject *p) {
	double f;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p)) {
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	f = PyFloat_AsDouble(p);
	printf("  Value: %f\n", f);
}

/**
 * print_python_bytes - a function that print the information about
 * python bytes
 * @p: address of pyobject strcut
 */
void print_python_bytes(PyObject *p)
{
	size_t i, size, length;
	char *char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [EROOR] Invalid Bytes object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	length = size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", length);
	for (i = 0; i < length; i++)
	{
		printf("%02hhx%s", str[i], i + 1 < len ? " " : "");
	}
	printf("\n");
}

/**
 * print_python_list_info - a function that prints basic info about
 * python lists
 * @p: a PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size_x, all, x;
	PyObject *object;

	size_x = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size_x);
	printf("[*] Allocated = %d\n", all);

	for (x = 0; x < size_x; x++)
	{
		printf("Element %d: ", x);

		object = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

