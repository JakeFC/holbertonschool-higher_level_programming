#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of list head pointer
 * @number: data of new node to insert
 * Return: address of new node, or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *trav, *new, *prev;

	if (!*head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	prev = *head;
	if (prev->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	trav = *head->next;
	while (trav)
	{
		if (trav->n >= number)
		{
			prev->next = new;
			new->next = trav;
			return (new);
		}
		prev = trav;
		trav = trav->next;
	}
	prev->next = new;
	new->next = NULL;
	return (new);
}
