#include <stdio.h>
#include <stdlib.h>
/**
 * reverse a singly linked list
 */
typedef struct _Link
{
	int n;
	struct _Link *next;
} Link;

Link *node_end(Link **h, int n)
{
	Link *node, *walk;

	node = malloc(sizeof(Link));
	if (!node)
		printf("malloc failed!\n");
	node->n = n;
	node->next = NULL;
	walk = *h;
	while (walk)
	{
		if (walk->next == NULL)
		{
			walk->next = node;
			return node;
		}
		walk = walk->next;
	}
	if (!(*h))
	{
		(*h) = node;
		return node;
	}
	return NULL;
}

void reverse(Link **h)
{
	Link *tmp_node;
	Link *tmp_next;
	Link *walk = *h;

	tmp_next = NULL;
	tmp_node = NULL;

	while (walk)
	{
		tmp_next = walk->next;
		walk->next = tmp_node;
		tmp_node = walk;
		walk = tmp_next;
		if (!walk)
			(*h) = tmp_node;
	}
}

void print(Link *h)
{
	Link *walk;

	walk = h;
	while (walk)
	{
		printf("%d\n", walk->n);
		walk = walk->next;
	}
}

int main()
{
	Link *walk, *head = NULL;

	node_end(&head, 1);
	node_end(&head, 2);
	node_end(&head, 3);
	node_end(&head, 4);
	node_end(&head, 5);
	node_end(&head, 5);

	print(head);
	printf("-------------\n");
	reverse(&head);
	print(head);
}
