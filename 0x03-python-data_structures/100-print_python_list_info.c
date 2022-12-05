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
	Py_ssize_t plen, allo, ele;

	plen = PyList_Size(p);
	allo = ((PyListObject *)p)->allocate;

	printf("[*] Size of the Python List = %ld\n", plen);
	printf("[*] Allocated = %ld\n", allo);

	for (ele = 0; ele <= plen - 1; ele++)
	{
		printf("Element %ld: %s\n", idx, (PY_TYPE(PyList_GetItem(p, idx)))->tp_name);
	}
}
