import nfl_data_py as nfl


position = input("Enter position (QB, RB, WR, TE): ").upper()
player_name = input("Enter player name: ")
season = int(input("Enter season: "))

ids = nfl.import_ids()
match = ids[
    (ids["position"] == position) &
    (ids["name"].str.contains(player_name, case=False, na=False))
]

if match.empty:
    print("no player found")
    exit()

player_id = match.iloc[0]["gsis_id"]
print(f"✅ Found {player_name} -> player_id: {player_id}")



weekly = nfl.import_weekly_data([season], downcast=True)
player_weekly = weekly[weekly["player_id"] == player_id]

if position == "QB":
    cols = ["season", "week", "recent_team", "opponent_team",
            "completions", "attempts", "passing_yards",
            "passing_tds", "interceptions", "fantasy_points_ppr"]
elif position == "RB":
    cols = ["season", "week", "recent_team", "opponent_team",
            "carries", "rushing_yards", "rushing_tds",
            "receptions", "receiving_yards", "fantasy_points_ppr"]
elif position in ["WR", "TE"]:
    cols = ["season", "week", "recent_team", "opponent_team",
            "receptions", "targets", "receiving_yards",
            "receiving_tds", "fantasy_points_ppr"]
else:
    print("Unsupported position")
    exit()

print(player_weekly[cols])