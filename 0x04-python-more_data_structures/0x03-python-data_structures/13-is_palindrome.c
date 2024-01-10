#include "lists.h"
#include <stdio.h>
/**
 * check_if_palindrome  -  checks if a linked_list is really a palindrome
 * @head: address of head of linked list.
 * @nxt_ptr: pointer to the next linked_list node
 * Return: 1 if its a linked list, 0 otherwise
 */
int check_if_palindrome(listint_t **head, listint_t *nxt_ptr)
{
	if (nxt_ptr->next != NULL && !check_if_palindrome(head, nxt_ptr->next))
	{
		return (0);
	}
	if ((*head)->n == nxt_ptr->n)
	{
		*head = (*head)->next;
		return (1);
	}
	else
	{
		return (0);
	}
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *nxt_ptr;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	nxt_ptr = *head;
	return (check_if_palindrome(head, nxt_ptr->next));
}
