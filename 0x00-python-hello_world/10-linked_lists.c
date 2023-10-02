#include "lists.h"

/**
 * check_cycle - function athst check if there's a cycle
 * @list: pointer to linked list
 * Return: 0 if not found or 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (slow && fast->next && fast->next->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
