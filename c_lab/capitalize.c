#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * This function provides the utility to make every string capitalize
 * even if the string contains a banch none alphabitic charachters
 * all cases are hondled.
 */
int isalphanum(char c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		return (1);
	if (c >= '0' && c <= '9')
		return (1);
	return (0);
}

char upper_if_lower(char c)
{
	if (c >= 'a' && c <= 'z')
		return ((int)c - 32);
	return (c);
}

char lower_if_upper(char c)
{
	if (c >= 'A' && c <= 'Z')
		return ((int)c + 32);
	return (c);
}

void capitalize(char *string)
{
	char *s = strdup(string);
	char *s_backup = s;

	if (isalphanum(*s))
		printf("%c", upper_if_lower(*s++));

	while (*s)
	{
		if (!isalphanum(*(s - 1)))
			printf("%c", upper_if_lower(*s));
		else
			printf("%c", lower_if_upper(*s));
		s++;
	}
	free(s_backup);
}

int main()
{
	capitalize("msting+is+  MB.B.b8.bB+aaA3?aA?Aa1aA %c    everyThing! /ll/abCD123.a");
	/*Return: Msting+Is+  Mb.B.B8.Bb+Aaa3?Aa?Aa1aa %C    Everything! /Ll/Abcd123.A*/
	return (0);
}
