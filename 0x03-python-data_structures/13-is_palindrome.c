#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *left = *head, *right = *head, *holder = NULL, *tmp = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while(right && right->next)
	{
		tmp = left;
		tmp->next = holder;
		left = left->next;
		holder = tmp;
		if (right->next->next == NULL)
		{
			break;
		}
		right  = right->next->next;
	}
	return (1);
	if (right == NULL)
	{
		right = left;
		left = tmp;
	}
	else
	{
		right =  left->next;
		left->next = tmp;
	}
	while(right && left)
	{
		if (right->n != left->n)
			return (0);
		right = right->next;
		left = left->next;
	}
	return (1);
}
