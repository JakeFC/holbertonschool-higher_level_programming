#include "lists.h"

/**
 * check_cycle - checks if a singly linked list is cyclical
 * @list: list input
 * Return: 0 if none found, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t tort, hare;

	if (!list)
		return (0);
	tort = list;
	hare = list->next;
	while (hare)
	{
		if (tort = hare)
			return (1);
		tort = tort->next;
		if (!hare->next)
			return (0);
		hare = hare->next->next;
	}
	return (0);
}
