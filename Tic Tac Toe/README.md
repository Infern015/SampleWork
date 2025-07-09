
# 🕹️ Tic Tac Toe Multiplayer + AI Game

This is a complete multiplayer Tic Tac Toe game built with **Python (Flask + SocketIO)** for the backend and **HTML/CSS/JavaScript** for the frontend. It supports:

- ✅ Multiplayer over LAN (using `myxando.com`)
- ✅ Single-player mode with AI (Easy → Expert)
- ✅ Score tracking
- ✅ Player join history
- ✅ Mobile + Desktop responsive UI

---

## 🚀 Getting Started

### 🧾 Requirements

- Python 3.7+
- pip

---

### 📦 Installation

1. **Unzip the project folder**  
   Extract `tictactoe_game.zip`.

2. **Navigate into the folder**
   ```bash
   cd tictactoe_game
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

### 🧠 Running the Game

Start the server:

```bash
python app.py
```

Then open in your browser:
```
http://localhost:5000
```

Or if you're on LAN:
```
http://<your_local_ip>:5000
```

To use a **custom domain like `myxando.com`**:
1. Open `C:\Windows\System32\drivers\etc\hosts` (as admin)
2. Add this line (replace with your IP):
   ```
   192.168.1.10 myxando.com
   ```
3. Access from browser:
   ```
   http://myxando.com:5000
   ```

Do the same on mobile (or use a local DNS proxy app like "HTTP Custom").

---

## 🕹️ Game Modes

### 🧍 Single Player
- Choose AI difficulty: Easy, Medium, Hard, Expert
- You play as X, AI is O

### 👥 Multiplayer
- Two players connect via browser
- Works over LAN using same IP or custom domain

---

## 🛠️ Project Structure

```
tictactoe_game/
├── app.py              # Flask + SocketIO server
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Game UI
└── static/
    ├── style.css       # Styles
    └── script.js       # Game logic + AI
```

---

## 📲 Tested On

- Google Chrome (PC)
- Firefox
- Android (Chrome browser)
- iPhone Safari

---

## 👨‍💻 Author

Built by [Your Name]. Inspired by multiplayer and AI Tic Tac Toe implementations.

---

## 📜 License

MIT License – Free for personal and commercial use.
