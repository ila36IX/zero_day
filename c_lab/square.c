#include <stdio.h>

void tr(int size)
{
	int i, j;

	for (i = 1; i <= size; i++)
	{
		for (j = 1; j <= size - i; j++)
		{
			putchar(' ');
		}
		for (j = 1; j <= i; j++)
		{
			putchar('0');
		}
		putchar('\n');
	}
}

int main(void)
{
	tr(4);
}
