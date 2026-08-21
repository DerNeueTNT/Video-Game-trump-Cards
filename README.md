# Videogame Trump Cards

A small two-player command-line card game featuring videogame characters from a variety of games.

Each character has six stats:

- **Power**
- **Durability**
- **Mobility**
- **Stealth**
- **Intelligence**
- **Versatility**

Players compare one stat at a time. The winner takes both cards. The first player to collect every card wins.

## Installation

Download the latest compiled release for your operating system from the **Releases** page.

### Windows

1. Download the Windows release.
2. Extract the downloaded archive if necessary.
3. Run the included `.exe`.

You do **not** need Python installed.

### Linux

1. Download the Linux release.
2. Extract the downloaded archive if necessary.
3. If required, make the executable runnable:

```bash
chmod +x ./VideogameTrumpCards
```

4. Run it:

```bash
./VideogameTrumpCards
```

You do **not** need Python installed.

## How to Play

This version is designed for **two players running the game separately**, for example while talking over Discord or another voice/text chat.

Both players should use the **same version of the game**.

### 1. Choose a game code

When the game asks:

```text
Game code:
```

one player can simply press **Enter** to generate a random game code.

The generated code should then be sent to the other player.

The other player must enter the **exact same code**.

Game codes are case-sensitive, so:

```text
AbC123
```

and:

```text
abc123
```

are different seeds.

The game code determines the shuffled deck, allowing both players' copies of the game to stay synchronized without a network connection.

### 2. Choose player numbers

One player selects **Player 1** and the other selects **Player 2**.

Accepted examples include:

```text
1
p1
player 1
```

and:

```text
2
p2
player 2
```

Player 1 takes the first turn.

### 3. Compare cards

Each round, both players are shown their own current card.

The player whose turn it is is also shown the name and origin of the opponent's card.

That player chooses one of the six stats and tells the other player which stat was chosen.

**Both players must enter the same stat.**

For example:

```text
power
```

The game compares the selected stat automatically.

- If your stat is higher, you win the round and take both cards.
- If your stat is lower, your opponent takes both cards.
- If both values are equal, the round is a tie and both cards return to their respective decks.

After the round, the turn passes to the other player.

## Commands

You can enter either the full stat name or its abbreviation.

| Stat | Accepted input |
| --- | --- |
| Power | `power`, `pow` |
| Durability | `durability`, `dur` |
| Mobility | `mobility`, `mob` |
| Stealth | `stealth`, `ste` |
| Intelligence | `intelligence`, `int` |
| Versatility | `versatility`, `ver` |

To quit the game, use any of:

```text
quit
stop
q
end
```

Input is not case-sensitive, and surrounding spaces are ignored.

## Card Stats

Most stats use a scale from **1 to 10**.

Higher values are better.

### Power

How much raw offensive or destructive power the character can bring to a fight.

This is not necessarily the same as lethality. A highly skilled assassin may be extremely dangerous without having enormous destructive power.

### Durability

How much damage the character can endure **without healing, resurrection, rewinding, or returning after defeat**.

### Mobility

How effectively the character can move and reposition, including movement abilities, equipment, traversal tools, teleportation, flight, and similar options.

### Stealth

How effectively the character can avoid detection, infiltrate locations, disguise themselves, or otherwise operate unnoticed.

### Intelligence

The character's demonstrated reasoning, knowledge, technical ability, planning, and problem-solving.

### Versatility

How many genuinely different types of problems the character can handle with their abilities, equipment, or other inherent tools.

Having many weapons that all perform essentially the same role does not automatically mean high versatility.

## Special Values

Some characters have stats outside the normal **1-10** scale.

These are shown with an asterisk:

```text
durability: 0*
versatility: 11*
```

These values are reserved for unusual characters that do not fit cleanly within the normal scale.

## Important Multiplayer Note

The current release does **not** communicate over the internet.

Both copies of the game simulate the same match locally using the shared game code.

Because of this, both players must:

- use the same game version,
- use the exact same game code,
- choose different player numbers,
- enter the same selected stat every round.

If the players enter different stats or use different game data, their games may become desynchronized.

## Terminal Colors

The game uses ANSI terminal formatting for colors and highlighted messages when supported.

If ANSI formatting is unavailable, the game automatically falls back to plain text.

## About the Character Ratings

Character ratings are subjective and are based on a mixture of:

- canon/lore,
- gameplay portrayal,
- demonstrated feats,
- standard equipment and abilities,
- and game balance.

They are intended for the card game rather than as definitive power-scaling rankings.

## Disclaimer

This is an unofficial fan-made project.

All referenced videogame characters, game titles, and related intellectual property belong to their respective owners.

This project is not affiliated with, endorsed by, or sponsored by the owners of those properties.

No official artwork, music, dialogue, or other game assets are included.
