#include <stdio.h>

int main() 
{
	int i = 1;
	/* (1)(2)(3) */
	unsigned long int p1, p2, n1, n2, a1, a2, c1, c2; 
	unsigned long int div = 100000000000000000;

	/* previos_value = 1; */
	p1 = 0;
	p2 = 1;

	/* actual_value = 2; */
	c1 = 0;
	c2 = 2;

	n1 = 0;
	n2 = 0;

	while (i <= 93)
	{ 
		printf("%lu$", n1);
		printf("%lu, ", n2 % div);

		// next_value = previos_value + actual_value;
		// n1 = (p1 + c1) % div;
		// n2 = (p2 + c2) + (p1 + c1) / div;
		
		n1 = n2 / div;
		n2 = (p2 + c2) % div;
		// previos_value = actual_value;
		p1 = c1, p2 = c2;

		// actual_value = next_value;
		c1 = n1, c2 = n2;
		i++;
	}

	printf("\n");
	return (0);
}
