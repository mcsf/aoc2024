#!/usr/bin/env awk -f

is_safe() { pt1++ }
is_tolerably_safe() { pt2++ }

END {
	print pt1
	print pt2
}


function is_safe() {
	return find_bad_level() == -1
}

function is_tolerably_safe(lvl) {
	if (is_safe()) return 1
	for (lvl = 1; lvl <= NF; lvl++) {
		if (find_bad_level(lvl) == -1) {
			return 1
		}
	}
}

function find_bad_level(skip_lvl,    lvl, prev_pitch) {
	for (lvl = 2; lvl <= NF; lvl++) {
		# Determine which levels to compare
		if (lvl == skip_lvl) continue
		prev_lvl = (lvl - 1 != skip_lvl) ? lvl - 1 : lvl -2
		curr_lvl = (lvl != skip_lvl) ? lvl : lvl + 1
		if (! prev_lvl) continue

		# Find any errors
		diff = $curr_lvl - $prev_lvl
		dist = diff >= 0 ? diff : -diff
		pitch = diff >= 0 ? 1 : -1
		if (!prev_pitch) prev_pitch = pitch
		if (prev_pitch != pitch || dist < 1 || dist > 3) {
			return lvl
		}
	}
	return -1
}
