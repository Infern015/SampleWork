from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

players = []
player_scores = {'X': 0, 'O': 0}
player_history = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    name = data['name']
    player = data['player']
    if len(players) < 2:
        players.append({'player': player, 'name': name})
        player_history.append(name)
        emit('player_joined', {'players': players, 'history': player_history}, broadcast=True)

@socketio.on('move')
def on_move(data):
    emit('move_made', data, broadcast=True)

@socketio.on('reset')
def on_reset():
    emit('reset_game', broadcast=True)

@socketio.on('win')
def on_win(data):
    winner = data['winner']
    if winner in player_scores:
        player_scores[winner] += 1
    emit('score_update', player_scores, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
