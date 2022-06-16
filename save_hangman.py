import random
from gamedata.hangman_words_list import word_list
from gamedata.game_view import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

def guess_letter():
  print(logo)
  lives = 6
  display = []

  # Add underscores to the list
  for _ in range(word_length):
      display += "_"

  # Guessing letters...
  while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print("Already guessed, don't repeat yourself ¯\_(ツ)_/¯")

    # Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
        print("Guessed, continue...")
        print(f"{''.join(display)}")

    # While there are letters to guess - count lives
    if guess not in chosen_word:
      print(f"You lose a life, {guess} not in word you are guessing!")
      lives -= 1
      print(stages[lives])
    if lives == 0:
      print("You lose.")
      
  print("Wohooo! Guessed word => ", f"{''.join(display)}")

guess_letter()
