def attack_damage(p1, p2, move):
	modifier = 1
	CRIT = False
	if move.is_stab(p1):
		modifier *= 1.5
	modifier *= p2.type_mod(move)
	if p1.is_critical(move):
		crit = True
		modifier *= 1.5
	modifier *= (.85 + .15 * random.random())

	DEF_modifier = 1
	if move.is_physical:
		if not crit:
			def_modifier = p1.get_stat("AT")/p2.get_stat("DE")
		else:
			def_modifier = p1.AT/p2.DE
	else:
		if not crit:
			def_modifier = p1.get_stat("SA")/p2.get_stat("SD")
		else:
			def_modifier = p1.SA/p2.SD

	return ((2 * p1.level + 10) / 250 * DEF_modifier * move.base + 2) * modifier