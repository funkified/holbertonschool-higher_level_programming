#include "lists.h"
/**
 * check_cycle - checks if list has a cycle in int
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (0);
		}
	}
	return (1);
}
