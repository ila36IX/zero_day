#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <inttypes.h>

/**
 * Given an integer array nums, return true if any value appears at least twice
 * in the array, and return false if every element is distinct.
 */
typedef struct node {
	int n;
	struct node *next;
} node;

typedef struct unique {
	unsigned size;
	node **set;
} unique;

void add_node(node **array, int value)
{
	node *item, *walk;

	item = malloc(sizeof(node));
	item->n = value;
	item->next = NULL;

	if (!*array)
	{
		*array = item;
		return;
	}
	walk = *array;
	while(walk->next)
	{
		walk = walk->next;
	}
	walk->next = item;
}

int in_array(node *array, int value)
{
	node *walk;
	if (!array)
		return (0);
	walk = array;
	while(walk)
	{
		if (walk->n == value)
			return (1);
		walk = walk->next;
	}
	return (0);
}
void print_array(node *array)
{
	node *walk;

	walk = array;
	while(walk)
	{
		printf("%d", walk->n);
		walk = walk->next;
		if (walk)
		{
			printf(", ");
		}
		else
		{
			printf("\n");
		}
	}
}

unsigned hash(int x, int size)
{
	x = (x ^ (x >> 30)) * UINT64_C(0xbf58476d1ce4e5b9);
	x = (x ^ (x >> 27)) * UINT64_C(0x94d049bb133111eb);
	x = x ^ (x >> 31);
	if (size == 0)
	{
		printf("List size should not be zero\n");
		exit(100);
	}
	return x % size;
}

void add(unique *s, int value)
{

	node **cell;

	cell = &s->set[hash(value, s->size)];
	add_node(cell, value);
	// printf("%d\n", (*(s->set + hash(value, s->size)))->n);
}

void print_set(unique *s)
{
	int i;

	for (i = 0; i < s->size; i++)
	{
		if (s->set[i])
		{
			printf("NODE: ");
			print_array(s->set[i]);
		}
		else
		{
			printf("NULL\n");
		}
	}
}

unsigned in_set(unique *s, int value)
{
	node *cell;

	cell = *(s->set + hash(value, s->size));
	// print_array(cell);
	if (in_array(cell, value))
		return (1);
	else
		return (0);
}

unique *init(unsigned size)
{
	unique *s;
	unsigned i;

	s = malloc(sizeof(unique));
	s->size = size;
	s->set = malloc(sizeof(node *) * size);
	for (i = 0; i < size; i++)
	{
		s->set[i] = NULL;
	}
	return (s);
}

bool containsDuplicate(int* nums, int numsSize) {
	unsigned i, j;
	unique *s;

	s = init(numsSize);

	for (i = 0; i < numsSize; i++)
	{
		if (in_set(s, nums[i]))
			return (1);
		else
			add(s, nums[i]);
	}
	return (0);
}
int main()
{
	int nums[101] = {-14119, -13170, -12655, -12604, -12598, -12360, -12145, -12066, -11703, -11615, -10730, -10598, -9994, -9727, -9638, -9397, -9338, -9112, -9038, -9036, -9008, -8811, -8588, -7754, -7552, -7501, -7443, -7409, -7234, -7060, -5622, -5496, -5246, -5197, -4899, -4327, -4173, -4016, -3981, -3175, -3035, -2448, -1748, -1339, -889, 214, 558, 687, 771, 1350, 1505, 1610, 2049, 2726, 3078, 3388, 3491, 3723, 4076, 4984, 5203, 5546, 6520, 6867, 7031, 7092, 7233, 7454, 7620, 7924, 8377, 8435, 8608, 9189, 9220, 9275, 9469, 9731, 10031, 10265, 10532, 10577, 11415, 11547, 11576, 11658, 11672, 12085, 12358, 12660, 12998, 12998, 13605, 13913, 14138, 14366, 14397, 14719, 14795, 14828};
	int result, i, size = 100;
	unique *list;

	// size = 15;
	// list = init(size);
	// add(list, 69);
	// add(list, 59);
	// add(list, 59);
	// add(list, 19);
	// print_set(list);
	// result = in_set(list, 19);
	// printf("-> %s\n", result ? "Yes" : "No");
	result = containsDuplicate(nums, size);
	printf("-> %s\n", result ? "Yes" : "No");
}
