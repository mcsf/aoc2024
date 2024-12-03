#include <stdio.h>
#include <string.h>
#include <regex.h>

#define RE "(mul\\(([0-9]+),([0-9]+)\\))|do\\(\\)|don't\\(\\)"
#define OPERAND_A 2
#define OPERAND_B 3
#define MATCH_SIZE 4

int main() {
	int is_on = 1;
	int sum1 = 0;
	int sum2 = 0;

	char *line = NULL;
	size_t linecap = 0;
	ssize_t linelen;

	regex_t regex;
	regmatch_t pmatch[MATCH_SIZE];

	regcomp(&regex, RE, REG_EXTENDED);

	while ((linelen = getline(&line, &linecap, stdin)) > 0) {
		char *ptr = line;

		while (!regexec(&regex, ptr, MATCH_SIZE, pmatch, 0)) {
			char *match = ptr + pmatch->rm_so;
			int len = pmatch->rm_eo - pmatch->rm_so;

			if (strncmp(match, "do()", len) == 0) {
				is_on = 1;
			} else if (strncmp(match, "don't()", len) == 0) {
				is_on = 0;
			} else {
				int a, b, prod;
				sscanf(ptr + pmatch[OPERAND_A].rm_so, "%d", &a);
				sscanf(ptr + pmatch[OPERAND_B].rm_so, "%d", &b);
				prod = a * b;
				sum1 += prod;
				if (is_on) sum2 += prod;
			}

			ptr += pmatch->rm_eo;
		}
	}

	printf("%d\n", sum1);
	printf("%d\n", sum2);
}
