# Snake (Python / Turtle) — Work in Progress

A Snake game built with Python's built-in `turtle` module, following an
object-oriented structure: a `Snake` class owns the body segments and movement,
and `main.py` drives the game loop.

> **Status: incomplete prototype.** The window, background, and segment-following
> movement are implemented. Controls, food, scoring, and collision detection are
> **not yet implemented**, so it currently cannot be played. See Roadmap.

## 🗂️ Files

| File       | Purpose                                      |
|------------|----------------------------------------------|
| `main.py`  | Sets up the screen and runs the game loop    |
| `snake.py` | `Snake` class: creates segments, moves them  |

## 🎯 What's Implemented

- 600×600 window, red background, title "SNAKE".
- `screen.tracer(0)` + manual `screen.update()` for smooth, flicker-free animation.
- **`Snake.create_snake()`** — builds three 20×20 square segments at
  `(0,0)`, `(-20,0)`, `(-40,0)`.
- **`Snake.move()`** — each segment takes the position of the one ahead of it
  (classic Snake body-following), and the head moves forward 20px.

## 🚀 How to Run

Requires Python 3 (uses only the standard library).

```bash
python main.py
