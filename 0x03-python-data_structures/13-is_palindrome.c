#include "lists.h"

/**
 * reverse_list - a function to reverse a singly linked list.
 * @head: the first node
 * Return: the first node of  a reversed linked list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next;

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
 * is_palindrome - a function that checks if a singly linked list is
 * a palindrome.
 * @head: the first node of the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half,
		  *prev_of_slow = *head;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_of_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	slow = *head;
	fast = second_half;
	while (second_half != NULL)
	{
		if (slow->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		slow = slow->next;
		second_half = second_half->next;
	}
	prev_of_slow->next = reverse_list(fast);
	return (is_palindrome);
}

