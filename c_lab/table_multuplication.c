#include <stdio.h>
/**
 * times_table - Print the table of meltuplication
 *
 * Return: Nothing
 *
 */
void times_table(void)
{
	int i, j;

	for (i = 0; i <= 9; i++)
	{
		putchar('0');
		for (j = 1; j <= 9; j++)
		{
			if (i * j >= 10)
			{
				putchar(',');
				putchar(' ');
				putchar('0' + (i * j) / 10);
				putchar('0' + (i * j) % 10);
			}
			else
			{
				putchar(',');
				putchar(' ');
				putchar(' ');
				putchar('0' + j * i);
			}
		}
		putchar('\n');
	}

}

int main(void)
{
	times_table();
	return (0);
}
