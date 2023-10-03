#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in sorted linked list 
 * @head: head of linked list
 * @n: number to add
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (*head == NULL || !head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	current = head;
	while (current)
	{
		if (current->next->n >= n)
		{
			current->next = new_node;
			new_node->next = current->next;
		}
		current = current->next;
	}
	return new_node;
}
