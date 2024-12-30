#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// It is about buffer overflow.
// Ignore the flag.txt file

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    printf("\033[32m\"Introspection is the key to unlocking your fullest potential; knowing yourself is the first step.\"\033[0m\n\n");
    printf("                                                                                         - Zwique \n");
    printf("Have you thought about what you really wanted in life?\n");
    char flag[50];
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) 
    {
        printf("Congrats!!! Now, run the nc instance to get the flag.");
        exit(1);
    }
    fread(flag, 1, 50, file);
    char buf[1008];
    printf(">> ");
    read(0, buf, 1008);
    printf("I wish for you that you get %s", buf);
}