def is_foul(ball_pocketed):
    return ball_pocketed == "cue_ball"

def calculate_score(player, points):
    player.score += points
