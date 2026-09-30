Forked repo link
https://github.com/achinthyamb05/19_battleship

Lab 4 Tasks Completed
Task 1 — Consistent Coordinate Handling

Fixed the coordinate representation between the player, board, and AI.

Internal coordinates use zero-based (row, column) tuples.
User-facing coordinates are displayed using one-based numbering.
AI coordinates are now handled consistently throughout the game.
Ship hit detection works correctly with the same coordinate representation.
Task 2 — Multiple Ships and Fleet Tracking

Added support for multiple ships for both the player and the enemy.

The game now supports:

Multiple ships
Individual ship damage tracking
Repeated-shot prevention
Ship sinking detection
Complete fleet sinking detection
Game completion when all enemy ships are sunk
Task 3 — Improved AI Targeting

Improved the AI so that after successfully hitting a ship, it prioritizes nearby untried cells.

The AI:

Tracks previously attempted coordinates
Avoids firing at the same coordinate twice
Prioritizes adjacent cells after a hit
Handles the situation where no untried cells remain
Task 4 — Shot and Sinking Feedback

Added clear feedback for each actual shot.

The game displays:

HIT! when a shot hits a ship
MISS! when a shot misses
You sank a ship. when an individual enemy ship is completely destroyed
You sank the fleet. when all enemy ships are destroyed
AI scored a hit when the AI hits a player ship
AI missed when the AI misses
AI sank your ship. when the AI completely destroys a player ship
Testing

The following functionality was tested:

Player hits
Player misses
Repeated player shots
Invalid coordinates
Coordinates outside the board
Sinking an individual ship
Sinking the complete enemy fleet
AI coordinate handling
AI repeated-shot prevention
AI adjacent targeting after a hit
AI hit and miss feedback
Quitting the game
Dependencies

This project uses only Python standard-library functionality.

No third-party packages are required.

LLM / Vibe Coding

An LLM was used during development to:

Understand the existing code and identify defects
Fix coordinate representation inconsistencies
Implement multiple-ship functionality
Improve AI targeting
Add shot and sinking feedback
Suggest and verify tests

All generated changes were reviewed, tested, and verified before being committed.

Git Commit History

The implementation was committed incrementally:

Fix AI coordinate handling
Add multiple ship and fleet tracking
Improve AI targeting
Add shot and sunk feedbackpage link, with the complete chat history
