#include <Python.h>

/**
 * print_python_list_info: Prints basic info on python list
 *
 * @p: Python objexct
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t plen, allo, ele_idx;
	PyObject *item;
	const char *ele;

	plen = PyList_Size(p);
	allo = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", plen);
	printf("[*] Allocated = %ld\n", allo);

	for (ele_idx = 0; ele_idx <= plen - 1; ele_idx++)
	{
		item = PyList_GetItem(p, ele_idx);
		ele = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", ele_idx, ele);
	}
}
