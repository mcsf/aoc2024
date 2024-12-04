#!/usr/bin/env awk -f

BEGIN {
	FS = ""
}

{
	for (i = 1; i <= NF; i++) {
		lines[NR, i] = $i

		# Keep track of all X's and A's for later
		if ($i == "X") xs[NR, i] = NR SUBSEP i
		else if ($i == "A") as[NR, i] = NR SUBSEP i
	}
}

END {
	# PART 1: Start from any X that we've found
	for (lead in xs) {
		split(lead, coords, SUBSEP)
		y = coords[1]
		x = coords[2]
		# ... and look in all directions
		for (dir = 0; dir < 9; dir++) {
			xdir = dir % 3 - 1
			ydir = int(dir / 3) - 1
			s = ""
			for (i = 0; i < 4; i++) s = s lines[y + i * ydir, x + i * xdir]
			pt1 += s ~ "XMAS"
		}
	}

	# PART 2: Start from any A that we've found
	for (lead in as) {
		split(lead, coords, SUBSEP)
		y = coords[1]
		x = coords[2]
		s1 = s2 = ""
		# ... and draw the two diagonals from there
		for (i = -1; i <= 1; i++) s1 = s1 lines[y + i, x + i]
		for (i = -1; i <= 1; i++) s2 = s2 lines[y + i, x - i]
		pt2 += s1 ~ "MAS|SAM" && s2 ~ "MAS|SAM"
	}

	print pt1
	print pt2
}
