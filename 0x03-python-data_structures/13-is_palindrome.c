#include "lists.h"

/**
 * reverse - reverse a linked list
 * @head: pointer to the LL
 * Return: pointer to reversed LL
 */

listint_t *reverse(listint_t *head)
{
	listint_t prev = NULL;
	listint_t current = head;
	listint_t next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - function that checks if a LL is palindrome
 * @head: pointer to linked list
 * Return: 1 if true 0 if false
 */

int is_palindrome(listint_t **head)
{
	listint_t secondHalf;
	listint_t *fast = head;
	listint_t *slow = head;

	if (head == NULL || head->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	secondHalf = reverse(slow);
	while (secondHalf != NULL)
	{
		if (head->data != secondHalf->data)
			return (0);
		head = head->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}
