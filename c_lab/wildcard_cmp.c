#include <stdio.h>


int wildcmp(char *s1, char *s2)
{
	if (*s1 == '\0' && *s2 == '\0')
		return (1);
	if (*s2 == '*' && *(s2 + 1))
	{
		if(*(s2 + 1) == *s1 || *(s2 + 1) == '*')
			return wildcmp(s1, s2 + 1);
	}
	if (*s2 == '*' && *s1 == '\0' && *(s2 + 1) == '\0')
		return (1);
	if (*s2 == '*')
		return wildcmp(s1 + 1, s2);
	if (*s1 == *s2)
		return wildcmp(s1 + 1, s2 + 1);
	else
		return (0);
}


int main(void)
{
	int r;

	r = wildcmp("main.c", "*.c");
	printf("%d\n", r);
	r = wildcmp("main.c", "m*a*i*n*.*c*");
	printf("%d\n", r);
	r = wildcmp("main.c", "main.c");
	printf("%d\n", r);
	r = wildcmp("main.c", "m*c");
	printf("%d\n", r);
	r = wildcmp("main.c", "ma********************************c");
	printf("%d\n", r);
	r = wildcmp("main.c", "*");
	printf("%d\n", r);
	r = wildcmp("main.c", "***");
	printf("%d - 1\n", r);
	r = wildcmp("main.c", "m.*c");
	printf("%d - 0\n", r);
	r = wildcmp("main.c", "**.*c");
	printf("%d - 1\n", r);
	r = wildcmp("main-main.c", "ma*in.c");
	printf("%d - 1\n", r);
	r = wildcmp("main", "main*d");
	printf("%d - 0\n", r);
	r = wildcmp("abc", "*b");
	printf("%d - 0\n", r);
	return (0);
}
