# General Data Quality Rules

## Player ID

- player_id must not be NULL.
- player_id must be unique for each player record.

## Game ID

- game_id must not be NULL.
- game_id must correspond to a valid game.

## Session Duration

- session_minutes must not be negative.
- session_minutes may be zero for sessions with no recorded activity.