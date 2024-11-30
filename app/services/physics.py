import math

def calculate_collision(ball1, ball2):
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx**2 + dy**2)
    if distance < (ball1.radius + ball2.radius):
        return True
    return False

def update_positions(balls, time_step):
    for ball in balls:
        ball.x += ball.vx * time_step
        ball.y += ball.vy * time_step
        # Apply friction
        ball.vx *= 0.98
        ball.vy *= 0.98
