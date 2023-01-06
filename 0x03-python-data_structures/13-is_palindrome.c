#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a list is palindrome
 *
 * @head: list head pointer
 *
 * Return: 0 if not palindrome 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2;
	int nodes, n, ctr *data;

	temp = temp2 = *head;
	if (*head == NULL)
		return (1);
	for (nodes = 0; temp != NULL; nodes++)
		temp = temp->next;
	temp = *head;
	data = (int *)malloc(sizeof(int) * (nodes / 2));
	for (n = 0; n <= nodes; n++)
	{
		data[n] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	if (nodes % 2 == 0)
	{
		for (n = 0; n <= (nodes / 2); n++)
			temp = temp->next;
	}
	else if (nodes % 2 != 0)
	{
		for (n = 0; n <= ((nodes / 2) + 1); n++)
			temp = temp->next;
	}
	printf("equity loop");
	for (n = 0; n < (nodes / 2); n++)
	{
		if (temp->n == temp2->n)
		{
			printf("\ntemp = %d, temp2 =%d\n", temp->n, temp2->n);
			ctrl++;
		}
		else
			return (0);
		temp = temp->next;
		temp2 = temp2->next;
	}
	return (1);
}
