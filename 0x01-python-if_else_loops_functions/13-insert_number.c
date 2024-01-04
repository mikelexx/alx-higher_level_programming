#include "lists.h"
/**
 * insert_node - inserts a number into a sorted linked_list
 * @head: head of linked_list
 * @number: number to be inserted
 * Return: address of inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *prev = NULL, *newnode = NULL;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (curr == NULL)
		*head = newnode;
		return (newnode);
	}
	if (curr->n > number)
	{
		newnode->next =  curr;
		*head = newnode;
		return (newnode);
	}
	while (curr && curr->n <= number)
	{
		prev = curr;
		curr = curr->next;
	}
	prev->next = newnode;
	newnode->next = curr;
	return (newnode);
}
