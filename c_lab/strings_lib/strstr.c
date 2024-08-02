#include <stdio.h>

/* Write a function that locates a substring.
 * Prototype: char *_strstr(char *haystack, char *needle);
 * The _strstr() function finds the first occurrence of the substring needle in
 * the string haystack. The terminating null bytes (\0) are not compared Returns
 * a pointer to the beginning of the located substring, or NULL if the substring
 * is not found.
 */

char *_strstr(char *haystack, char *needle)
{
	int i, j,check = 0;

	if (!haystack || !needle)
		return NULL;
	/* First sulotion! */
	// while (*haystack != '\0')
	// {
	// 	i = 0;
	// 	while (needle[i] && haystack[i])
	// 	{
	// 		if (haystack[i] != needle[i])
	// 		{
	// 			break;
	// 		}
	// 		i++;
	// 		if (needle[i] == '\0')
	// 			return haystack;
	// 	}
	// 	haystack++;
	// }
	/* Second sulotion! */
	for (i = 0; haystack[i]; i++)
	{
		for (j = 0; haystack[i + j] && needle[j] && haystack[i + j] == needle[j]; j++);
		if (needle[j] == '\0')
			return &haystack[i];
	}
	return NULL;
}


int main()
{
	char *haystack1 = "hello worl I'm testing world";
	char *needle1 = "world";
	char *result1 = _strstr(haystack1, needle1);
	printf("Test 1: %s\n", result1 ? result1 : "NULL");

	char *haystack2 = "abcdef";
	char *needle2 = "cd";
	char *result2 = _strstr(haystack2, needle2);
	printf("Test 2: %s\n", result2 ? result2 : "NULL");

	char *haystack3 = "abcdef";
	char *needle3 = "gh";
	char *result3 = _strstr(haystack3, needle3);
	printf("Test 3: %s\n", result3 ? result3 : "NULL");

	char *haystack4 = "mississippi";
	char *needle4 = "issip";
	char *result4 = _strstr(haystack4, needle4);
	printf("Test 4: %s\n", result4 ? result4 : "NULL");

	char *haystack5 = "a";
	char *needle5 = "";
	char *result5 = _strstr(haystack5, needle5);
	printf("Test 5: %s\n", result5 ? result5 : "NULL");

	char *haystack6 = NULL;
	char *needle6 = "a";
	char *result6 = _strstr(haystack6, needle6);
	printf("Test 6: %s\n", result6 ? result6 : "NULL");

	return 0;
}
