# Countdown Timer with Audio Alarm

A fun Python countdown timer inspired by a pasta timer, with an audio alarm that plays when time's up!

## Features

- Interactive time input validation
- Real-time countdown display in `h:m:s` format
- Audio alarm that plays when the timer reaches zero
- Friendly, conversational intro explaining the concept
- Error handling for invalid time formats

## Requirements

- Python 3.x
- pygame (for audio playback)

## Installation

1. Install pygame:
```bash
pip install pygame
```

2. Have an audio file ready (supports `.mp3`, `.wav`, `.ogg`, etc.)

## Usage

1. Run the script:
```bash
countdown.py
```

2. When prompted, enter a time in the format `h:m:s` (hours:minutes:seconds)
   - Example: `00:05:30` for 5 minutes and 30 seconds
   - Example: `01:00:00` for 1 hour

3. The timer will count down and display the remaining time
4. When time reaches zero, an alarm sound plays


## Configuration

To use your own audio file, edit this line in the code:
```python
alarm_sound = pygame.mixer.Sound("Sounds/YOUR PHONE LINGING (sound effect).mp3")
```

Change `"Sounds/YOUR PHONE LINGING (sound effect).mp3"` to the path of your audio file.

## Input Validation

The script validates your input and provides helpful error messages:
- **Format error**: Must be in `h:m:s` format (e.g., `06:06:06`)
- **Range error**: Minutes and seconds must be less than 60

## Notes

- Hours can be any value (0, 1, 2, etc.)
- Minutes must be between 0-59
- Seconds must be between 0-59
- The timer counts down every second (1 second interval)
- The audio will play for 5 seconds after the timer finishes

Enjoy your perfectly timed pasta!
