#!/bin/sh

#
# Works with the sample input, but not with the real puzzle input.
#
# Remove the '-q' option from the 'tsort' invocation to observe that it reports
# cycles.
#

# Grab the ordering rules and topologically sort all objects
awk -F '|' '/^$/{exit}1{print $1,$2}' | tsort -q > RAW_SORT

# For every update sequence, produce a paragraph in which each line consists of two integer:
# - the order of the item in the topological sort
# - the item itself
awk -F, '
	BEGIN {
		while (getline x < "RAW_SORT") order[x] = ++n
	}

	{
		for (i=1; i<=NF; i++) print order[$i], $i
		print ""
	}
' \
	| awk '
		BEGIN {
			RS = "\n\n"
			FS = "\n"
		}

		{
			# For every update sequence:
			# - copy it to file "ACTUAL"
			# - sort it according to tsort and save it to file "ORDERED"
			# - compare both files:
			#   * if they do not differ, the sequence is correct
			#   * in either case, refer to "ORDERED" to grab the middle item

			print > "ACTUAL"
			print | (sort_cmd = "sort -g > ORDERED")
			close("ACTUAL")
			close(sort_cmd)

			if (! system("diff -q ORDERED ACTUAL >/dev/null")) {
				pt1 += get_middle()
			} else {
				pt2 += get_middle()
			}
		}

		END {
			print pt1
			print pt2
		}

		function get_middle(m) {
			RS = "\n"
			for (i = int(NF / 2) + 1; i > 0; i--) {
				getline line < "ORDERED"
				split(line, parts, " ")
				m = parts[2]
			}
			RS = "\n\n"
			close("ORDERED")
			return m
		}
	'
