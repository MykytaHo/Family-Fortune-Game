# Family-Fortune-Game
Mini game on Python 
This is a simple text-based "Family Fortune" game implemented in Python, inspired by the classic TV game show "Family Feud". The game allows two players to compete by answering questions with multiple possible correct answers. Players take turns buzzing in and attempting to guess the most popular answers to survey questions.

Features:
Buzzer System: Players can "buzz in" by pressing keys (Enter for Player 1, Spacebar for Player 2).
Questions and Answers: Randomized questions are selected, and players must guess the most popular answers from a predefined list.
Scorekeeping: Each correct answer earns points, and the first team to answer correctly keeps playing until they accumulate 3 wrong answers.
Stealing Mechanism: If one team answers 3 questions incorrectly, the other team gets a chance to steal the points by answering correctly.
Replayability: After each game round, players are given the option to play again.
How to Play:
Players take turns buzzing in to answer questions.
The first player to buzz in gets the chance to answer the question.
If they answer incorrectly, they can make up to 3 attempts before the other player gets a chance to steal the points.
Points are awarded for correct answers, and the first team to score 3 correct answers wins the round.
Requirements:
Python 3.x
No external libraries required, only standard Python libraries (random, time).
How to Run:
Simply run the script in your Python environment. The game will prompt players to buzz in and answer questions, and will display the final scores at the end of each round.
