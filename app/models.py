from . import db

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Player {self.name}>"

class Game(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    current_turn = db.Column(db.Integer, nullable=False, default=1)  # 1 or 2
    active = db.Column(db.Boolean, default=True)

    player1 = db.relationship("Player", foreign_keys=[player1_id])
    player2 = db.relationship("Player", foreign_keys=[player2_id])

    def __repr__(self):
        return f"<Game {self.id}>"

class Ball(db.Model):
    __tablename__ = "balls"

    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float, nullable=False)
    y = db.Column(db.Float, nullable=False)
    radius = db.Column(db.Float, nullable=False, default=5.73)  # Standard size
    vx = db.Column(db.Float, nullable=False, default=0.0)
    vy = db.Column(db.Float, nullable=False, default=0.0)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)

    game = db.relationship("Game", backref="balls")

    def __repr__(self):
        return f"<Ball {self.id} at ({self.x}, {self.y})>"
