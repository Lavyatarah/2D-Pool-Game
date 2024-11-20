from app import db
from datetime import datetime

#User model: Storing user related information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(100), unique=True, nullable=False)
    email = db.Column(db.string(100), unique=True, nullable=False)
    password_hash = db.Column(db.string(200), nullable=False)
    games = db.relationship('Game', backref='user', lazy=True)


    def __repr__(self):
        return f'<User {self.username}>'
    
# Game model: This model stores game-related information

class game(db.Model):
    id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))
    game_status = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    shots =db.relationship('shot', backref='game', lazy=True)
    balls = db.relationship('Ball', backref='game', lazy=True)


    def __repr__(self):
        return f'<Game {self.id} - {self.game_status}>'
    

    #PoolTable model: stored the layout and details of the pool table

class PoolTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    layout = db.Column(db.String(255), nullable=False)
    game = db.relationship('Game', backref='pool_table', lazy=True)


    def __repr__(self):
        return f'<PoolTable {self.id}>'
    


#Ball Model: Stores ball0related details for each game

class Ball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    number = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position_x = db.Column(db.Float, nullable=False)
    position_y = db.Column(db.Boolean, default=False)
    is_potted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Ball {self.number}>'
    

#Shot model: Stores information about the shotd made during the game
class shot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    player_id = db.Column(db.Integer, nullable=False)
    game = db.relationship('Game', backref='scores', lazy=True)
    player = db.relationship('User', backref='scores', lazy=True)


    def __repr__(self):
        return f'<Score {self.score} for {self.player.username} in Game {self.game_id}'
    