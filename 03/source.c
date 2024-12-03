#include <stdio.h>
#include <string.h>
#include <regex.h>

#define PATTERN     "(mul\\(([0-9]+),([0-9]+)\\))|(do\\(\\))|(don't\\(\\))"
#define OPERAND_A   2
#define OPERAND_B   3
#define IS_DO       4
#define IS_DONT     5
#define MATCH_SIZE  6

int main() {
	int is_on = 1;
	int sum1 = 0;
	int sum2 = 0;

	char *line = NULL;
	size_t linecap = 0;
	ssize_t linelen;

	regex_t regex;
	regmatch_t pmatch[MATCH_SIZE];

	regcomp(&regex, PATTERN, REG_EXTENDED);

	while ((linelen = getline(&line, &linecap, stdin)) > 0) {
		char *ptr = line;

		while (!regexec(&regex, ptr, MATCH_SIZE, pmatch, 0)) {
			if (!~pmatch[OPERAND_A].rm_so) {
				is_on = ~pmatch[IS_DO].rm_so;
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
