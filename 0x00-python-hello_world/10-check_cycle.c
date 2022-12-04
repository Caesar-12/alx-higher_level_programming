#include "lists.h"

/**
 * check_cycle - Check is linked list has a cycle
 *
 * @list: List to check for cycle
 *
 * Return: 0 for no loop, 1 for loop
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
		{
			return (1);
		}
	}

	return (0);
}
