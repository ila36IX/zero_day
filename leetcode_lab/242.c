#include <string.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


bool isAnagram(char* s, char* t) {
	int buff[26];
	int i;

	if (strlen(s) != strlen(t))
		return (0); 
	for (i = 0; i < 23; i++)
		buff[i] = 0;
	for (i = 0; s[i]; i++)
		buff[s[i] - 'a']++;
	for (i = 0; t[i]; i++)
		if (--buff[t[i] - 'a'] < 0) return (0);
	return (1);
}

int main(int ac, char **argv) 
{
	int is = isAnagram(argv[1], argv[2]);
	printf("\n%s\n", is ? "TRUE" : "FALSE");
}
