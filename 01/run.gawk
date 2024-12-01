#!/usr/bin/env gawk -f

{
	left[NR] = $1
	right[NR] = $2
	occur[$2] += 1	# Part 2
}

END {
	asort(left)
	asort(right)

	for (i = 1; i <= NR; i++) {
		distsum += abs(left[i] - right[i])
		simscore += left[i] * occur[left[i]]
	}

	print distsum
	print simscore
}

function abs(n) { return n >= 0 ? n : -n }
