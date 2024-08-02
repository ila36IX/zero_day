#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

int secret;
int main(int argc, char **argv){
	printf("%s %n\n", argv[1], &secret);
	printf("Secret -> %d\n", &secret);
	if (secret)
		printf("You got me!");
}
