#include <stdio.h>
#include <limits.h>
#include <string.h>

int _putchar(char c)
{
	return putchar(c);
}

void putnbr(int n)
{
	unsigned int n_, big_n;
	int divider;

	big_n = n_ = n;
	if (n < 0)
	{
		big_n = n_ = n * -1;
		_putchar('-');
	}
	divider = 1;
	while (n_ >= 10)
	{
		n_ /= 10;
		divider *= 10;
	}

	while (divider >= 1)
	{
		_putchar('0' + big_n / divider);
		big_n = big_n - (big_n / divider) * divider;
		divider /= 10;
	}
}
int main()
{
	int i;

	for (i = -100; i <= 100; i++)
	{
		putnbr(i);
		printf("\n%d\n", i);
		printf("-----------------\n");
	}
}
