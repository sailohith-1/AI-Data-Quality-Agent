# Gaming Transaction Schema

## Players

- player_id: unique identifier for a player.
- game_id: identifier of the game.
- game_name: human-readable game name.

## Transactions

- purchase_amount: monetary amount associated with a transaction.
- transaction_type: PURCHASE or REFUND.
- session_minutes: duration of the player's session in minutes.