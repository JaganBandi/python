class Cricket:

	Team = "India"

	def __init__(self, player_name, role):
		self.player_name = player_name
		self.role = role

	def display(self):
		print("Player_name:", self.player_name)
		print("Role:", self.role)


	@classmethod
	def show_team(cls):
		print("Team:", cls.Team)


c1 = Cricket("Virat Kohli", "Batsman")
c2 = Cricket("Ravindra Jedeja", "All Rounder")

c1.display()
c2.display()

Cricket.show_team()