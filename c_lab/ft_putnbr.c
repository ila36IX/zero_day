#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void    putnbr(int nb)
{
	unsigned int n;

	if (nb < 0)
	{
		putchar('-');
		n = -nb;
	} 
	else
		n = nb;
	if (n >= 10)
		putnbr(n / 10);   
	putchar(n % 10 + '0');
}

int main(int ac, char **av)
{
	putnbr(atoi(av[1]));
}
