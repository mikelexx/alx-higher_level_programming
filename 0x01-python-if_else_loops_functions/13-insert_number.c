#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *newnode = NULL, *holder = NULL;

	if (head == NULL)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (curr == NULL)
	{	curr = newnode;
		return (newnode);
	}
	if (curr->n > number)
	{
		newnode->next =  curr;
		return (newnode);
	}
	while (curr != NULL)
	{
		if (curr->next == NULL)
		{
			if (curr->n < number)
				curr->next = newnode;
			else
			{
				newnode->next = curr;
			}
			return (newnode);
		}
		if (curr->n <= number && curr->next->n >= number)
		{
			holder = curr->next;
			curr->next = newnode;
			newnode->next = holder;
			return (newnode);
		}
		curr = curr->next;
	}
	return (NULL);
}
