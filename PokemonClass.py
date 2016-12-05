class Pokemon:
	natures = [{"name":"Adamant","HP":1,"AT":1.1,"DE":1,"SA":0.9,"SD":1,"SP":1},
			{"name":"Bashful","HP":1,"AT":1,"DE":1,"SA":1,"SD":1,"SP":1},
			{"name":"Bold","HP":1,"AT":0.9,"DE":1.1,"SA":1,"SD":1,"SP":1},
			{"name":"Brave","HP":1,"AT":1.1,"DE":1,"SA":1,"SD":1,"SP":0.9},
			{"name":"Calm","HP":1,"AT":0.9,"DE":1,"SA":1,"SD":1.1,"SP":1},
			{"name":"Careful","HP":1,"AT":1,"DE":1,"SA":0.9,"SD":1.1,"SP":1},
			{"name":"Docile","HP":1,"AT":1,"DE":1,"SA":1,"SD":1,"SP":1},
			{"name":"Gentle","HP":1,"AT":1,"DE":0.9,"SA":1,"SD":1.1,"SP":1},
			{"name":"Hardy","HP":1,"AT":1,"DE":1,"SA":1,"SD":1,"SP":1},
			{"name":"Hasty","HP":1,"AT":1,"DE":0.9,"SA":1,"SD":1,"SP":1.1},
			{"name":"Impish","HP":1,"AT":1,"DE":1.1,"SA":0.9,"SD":1,"SP":1},
			{"name":"Jolly","HP":1,"AT":1,"DE":1,"SA":0.9,"SD":1,"SP":1.1},
			{"name":"Lax","HP":1,"AT":1,"DE":1.1,"SA":1,"SD":0.9,"SP":1},
			{"name":"Lonely","HP":1,"AT":1.1,"DE":0.9,"SA":1,"SD":1,"SP":1},
			{"name":"Mild","HP":1,"AT":1,"DE":0.9,"SA":1.1,"SD":1,"SP":1},
			{"name":"Modest","HP":1,"AT":0.9,"DE":1,"SA":1.1,"SD":1,"SP":1},
			{"name":"Naive","HP":1,"AT":1,"DE":1,"SA":1,"SD":0.9,"SP":1.1},
			{"name":"Naughty","HP":1,"AT":1.1,"DE":1,"SA":1,"SD":0.9,"SP":1},
			{"name":"Quiet","HP":1,"AT":1,"DE":1,"SA":1.1,"SD":1,"SP":0.9},
			{"name":"Quirky","HP":1,"AT":1,"DE":1,"SA":1,"SD":1,"SP":1},
			{"name":"Rash","HP":1,"AT":1,"DE":1,"SA":1.1,"SD":0.9,"SP":1},
			{"name":"Relaxed","HP":1,"AT":1,"DE":1.1,"SA":1,"SD":1,"SP":0.9},
			{"name":"Sassy","HP":1,"AT":1,"DE":1,"SA":1,"SD":1.1,"SP":0.9},
			{"name":"Serious","HP":1,"AT":1,"DE":1,"SA":1,"SD":1,"SP":1},
			{"name":"Timid","HP":1,"AT":0.9,"DE":1,"SA":1,"SD":1,"SP":1.1}]

	def __init__(self, name, types, LV, baseStats, nature):
		def nat_modifier(nat, stat):
			for n in natures:
				if nature["name"] == nat:
					return nature[stat]
		self.name = name
		self.type = types
		self.LV = LV
		self.b_stats = {"HP": 0, "AT": 0, "DE": 0, "SA": 0, "SD": 0, "SP": 0}
		for stat in baseStats:
			self.b_stats[stat] = (level / 50 * baseStats[stat] + 5) * nat_modifier(nature, stat)
		SELF.stat_stg = {"AT": 0, "DE": 0, "SA": 0, "SD": 0, "SP": 0}
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
				modifier == 1 / modifier
		return int(self.b_stats[stat] * modifier)