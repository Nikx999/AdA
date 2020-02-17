def Tower_of_hanoi(n, prev_rod, next_rod, aux_rod):
	if n == 1:
		print("move disk 1 from", prev_rod, "to", next_rod)
		return
	Tower_of_hanoi(n - 1, prev_rod, aux_rod, next_rod)
	print("move disk", n, "from", prev_rod, "to", next_rod)
	Tower_of_hanoi(n - 1, aux_rod, next_rod, prev_rod)

Tower_of_hanoi(4, 'A', 'C', 'B')
