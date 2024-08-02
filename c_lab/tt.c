#include <stdio.h>

void changeme(int *i, int number)
{
	*i = *i * number;
}

int main(int argc, char **argv)
{
	int j = 5;
	int *ptr = &j;
	
	printf("%d\n", j);
	changeme(ptr, 10);
	printf("%d\n", j);
	return (0);
}
