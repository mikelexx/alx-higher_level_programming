#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has \
 * a cycle in it.
 * @list: linked list node
 * Return: 0 if there is no cycle, 1 if there is a cyle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	while (fast && fast->next)
	{
		if (fast->next == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
