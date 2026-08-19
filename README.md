# 🏓 Pong — The Arcade Game

A simple **Pong arcade game** built in Python using the built-in `turtle` module. The game features two-player paddle controls, ball bouncing, collision detection, scoring, and increasing ball speed as rallies continue.

## 🎮 Features

* Two-player gameplay
* Keyboard-controlled paddles
* Ball and paddle collision detection
* Automatic ball bouncing
* Score tracking for both players
* Ball speed increases after successful paddle hits
* Reset after a player misses the ball
* Simple arcade-style graphical interface

## 🕹️ Controls

| Player    | Move Up | Move Down |
| --------- | ------- | --------- |
| Player 1  | `W`     | `S`       |
| Player 2  | `↑`     | `↓`       |
| Quit Game | `H`     |           |

## 📁 Project Structure

```text
Pong/
├── pong.py          # Main game loop and game logic
├── ball.py          # Ball movement and collision behavior
├── Paddles.py       # Paddle classes and controls
├── scoreboard.py    # Score display and net
└── README.md
```

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python pong.py
```

No external packages are required since the project uses Python's built-in `turtle` module.

## 🧠 Concepts Used

This project demonstrates:

* Object-Oriented Programming
* Classes and inheritance
* Event-driven keyboard input
* Game loops
* Collision detection
* Basic animation
* State management
* Python's `turtle` graphics library

## 🚀 Future Improvements

Possible additions would include sound effects, better collision detection, a start/pause screen, difficulty levels, and a high-score system.
