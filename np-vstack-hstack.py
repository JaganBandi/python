import numpy as np  

team_a = np.array([[10, 20, 30]])
team_b = np.array([[40, 50, 60]])

combined_teams = np.vstack((team_a, team_b))
print("Combined Teams:", combined_teams)
combined_scores = np.hstack((team_a, team_b))
print("Combined Scores:", combined_scores)