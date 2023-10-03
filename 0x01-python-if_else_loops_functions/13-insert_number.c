#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in sorted linked list
 * @head: head of linked list
 * @number: number to add
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
