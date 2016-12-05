class Pokemon:
	def __init__(self, name, types, LV, baseStats, nature=None):
		def nat_modifier(nat, stat):
			if stat in natures[nat]:
				if natures[nat].index(stat) == 0:
					return 1.1
				return .9
			return 1
		self.name = name
		self.type = types
		self.LV = LV
		self.b_stats = {"HP": 0, "AT": 0, "DE": 0, "SA": 0, "SD": 0, "SP": 0}
		for stat in baseStats:
			nature_modifier = 1
			self.b_stats[stat] = int(LV / 50 * baseStats[stat] + 5)
		self.stat_stg = {"AT": 0, "DE": 0, "SA": 0, "SD": 0, "SP": 0}
		self.status = {"BRN": False, "PAR": False, "PSN": False, "TOX": False, "FRZ": False, "SLP": False}
		self.status_count = {"TOX": 0, "SLP": 0}

	def inflict_status(self, condition):
		if True in list(self.status.values()):
			pass
		else:
			self.status[condition] = True
		if condition == "TOX":
			self.status_count["TOX"] += 1

	def heal_status(self):
		for s in self.status:
			self.status[s] = False
		for s in self.status_count:
			self.status_count[s] = 0

	def get_stat(self, stat):
		modifier = 1
		if self.stat_stg[stat] != 0:
			modifier += (.5 * self.stat_stg[stat])
			if self.stat_stg[stat] < 0:
				modifier = 1 / modifier
		return int(self.b_stats[stat] * modifier)
