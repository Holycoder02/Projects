# Rock Paper Scissor Game

A classic Rock, Paper, Scissor game where you can play against the computer.

## Features

- **Interactive Gameplay**: Play against the computer
- **Random Computer Moves**: Computer chooses randomly (not conditionally)
- **Score Tracking**: Keeps track of wins for both player and computer
- **Continuous Play**: Play as many rounds as you want
- **Easy Quit**: Type "quit" to exit and see final scores

## Game Rules

| Player | Computer | Result |
|--------|----------|--------|
| Rock | Rock | Tie |
| Rock | Paper | Paper wins |
| Rock | Scissor | Rock wins |
| Paper | Paper | Tie |
| Paper | Rock | Paper wins |
| Paper | Scissor | Scissor wins |
| Scissor | Scissor | Tie |
| Scissor | Rock | Rock wins |
| Scissor | Paper | Scissor wins |

## Gameplay Workflow

1. **Input**: User enters their move (Rock, Paper, or Scissor)
2. **Computer Move**: Computer randomly selects from the same options
3. **Result**: Winner is determined based on classic game rules
4. **Scoring**: Keeps running total of wins
5. **Repeat**: Continue playing until user types "quit"

## Usage

Run the game:

```bash
python main.py
```

### Example Game Session

```
Enter your move (Rock, Paper, Scissor) or 'quit': Rock
User choice: Rock, Computer choice = Paper
Paper wins

Enter your move (Rock, Paper, Scissor) or 'quit': Scissor
User choice: Scissor, Computer choice = Rock
Rock wins

Enter your move (Rock, Paper, Scissor) or 'quit': quit
Final Score - You: 0 | Computer: 2
```

## Requirements

- Python 3.x
- random module (built-in)

## Input Format

- Enter moves as: Rock, Paper, or Scissor
- The game accepts both lowercase and mixed-case input
- Type "quit" to exit and see final scores

## Features

- ✅ Score tracking for entire game session
- ✅ Case-insensitive input
- ✅ Invalid input handling with retry prompt
- ✅ Final score display

## Notes

- The computer's choices are completely random
- Each round is independent
- No ties affect the overall score
- Game exits cleanly with final statistics
