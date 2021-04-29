#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of list head pointer
 * Return: 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int i, ii, arr[300];
	listint_t *trav = *head;

	if (!head || !*head)
		return (1);
/*	for (i = 0; trav; i++)*/
/*		trav = trav->next;*/
/*	arr = malloc(sizeof(int) * i);*/
/*	trav = *head;*/
	for (i = 0; trav; i++)
	{
		arr[i] = trav->n;
		trav = trav->next;
	}
	for (--i, ii = 0; ii <= i; ii++, i--)
		if (arr[ii] != arr[i])
			return (0);
	return (1);
}
