<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=Grandmaster%20Croupier%20&descAlign=53&descAlignY=53&animation=fadeIn&fontSize=30&textBg=false"/>
</p>

##  Description

This is a simple poker game simulation between a human player and a computer (AI). The game follows basic poker rules including dealing cards, betting rounds, and determining a winner.

---

##  Features

* Deck of 52 cards
* Two players (Human vs Computer)
* Multiple betting rounds:

  * Pre-Flop
  * Flop
  * Turn
  * River
* Betting actions:

  * Call
  * Raise
  * Fold
  * Check
* Pot system
* Winner determination based on hand strength

---

##  Game Flow

1. Initialize game and players (2000 starting money each)
2. Shuffle deck and deal 2 cards to each player
3. First betting round begins
4. Reveal 3 community cards (Flop)
5. Second betting round
6. Reveal 4th card (Turn)
7. Third betting round
8. Reveal 5th card (River)
9. Final betting round
10. Determine winner and award pot
11. Start a new round or end game

---

##  Project Structure

* **Card** → Represents a single card (suit, rank)
* **Deck** → Manages the 52-card deck (shuffle, deal)
* **Player** → Stores player data (money, hand, bets)
* **Game** → Controls overall game flow
* **AI Player** → Handles computer decisions

---

## ▶ How to Run

1. Clone the repository

   ```
   git clone <your-repo-link>
   ```
2. Navigate to the project folder

   ```
   cd poker-game
   ```
3. Run the program

   ```
   python main.py
   ```

   *(or the relevant file depending on your language)*

---

## 🔧 Requirements

* Python 3.x *(or your chosen language environment)*

---


## 👤 Author

Nelson Romeo

---

