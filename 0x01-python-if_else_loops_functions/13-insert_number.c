#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert node in a sorted list
 *
 * @head: pointer to list head pointer
 * @number: list value
 *
 * Return: address of new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *temp2, *new;

	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	temp = *head;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	else if (temp->next == NULL)
	{
		if (temp->n > new->n)
		{
			new->next = temp;
			*head = new;
		}
		else
			temp->next = new;
	}
	if (temp->n > new->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next != NULL)
	{
		if ((temp->next->n) > (new->n))
		{
			temp2 = temp->next;
			temp->next = new;
			new->next = temp2;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
