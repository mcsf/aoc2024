#!/usr/bin/awk -f

BEGIN {
	FS = "[A-Za-z:,= ]+"
	RS = "\n\n"
}

{
	ax = $2; ay = $3
	bx = $4; by = $5
	px = $6; py = $7
	pt1 += solve()

	px += 10000000000000
	py += 10000000000000
	pt2 += solve()
}

END {
	print pt1
	print pt2
}

# https://en.wikipedia.org/wiki/Cramer%27s_rule
function solve() {
	det = ax * by - bx * ay
	det_x = px * by - bx * py
	det_y = ax * py - px * ay
	x = det_x / det
	y = det_y / det

	if (x == int(x) && y == int(y)) {
		return 3 * x + y
	}
}
