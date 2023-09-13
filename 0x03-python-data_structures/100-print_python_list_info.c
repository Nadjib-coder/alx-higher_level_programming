#include <Python.h>

/**
 * print_python_list_info - a function that prints basic info about python lists
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

