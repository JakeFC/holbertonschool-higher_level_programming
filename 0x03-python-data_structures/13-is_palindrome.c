#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of list head pointer
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int i, ii, *arr;
	listint_t *trav = *head;

	if (!head || !*head)
		return (1);
	for (i = 0; trav; i++)
		trav = trav->next;
	arr = malloc(sizeof(int) * i);
	if (!arr)
		return (0);
	trav = *head;
	for (i = 0; trav; i++)
	{
		arr[i] = trav->n;
		trav = trav->next;
	}
	for (--i, ii = 0; ii <= i; ii++, i--)
		if (arr[ii] != arr[i])
		{
			free(arr)
			return (0);
		}
	free(arr)
	return (1);
}
