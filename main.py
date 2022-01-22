questions = {
  "Who is the NBA's all time leader in POINTS?: " : "B",
  "Who is the NBA's all time leader in REBOUNDS?: " : "D",
  "Who is the NBA's all time leader in ASSISTS?: " : "C", 
  "Who is the NBA's all time leader in BLOCKS?: " : "A", 
  "Who is the NBA's all time leader in STEALS?: " : "D",
  "Who is the NBA's all time leader in 3 POINTERS?: " : "C"
}

choices = [["A) Karl Malone", "B) Kareem Abdul-Jabbar", "C) LeBron James", "D) Kobe Bryant"],
  ["A) Elvin Hayes", "B) Kareem Abdul-Jabbar", "C) Bill Russell", "D) Wilt Chamberlain"],
  ["A) Jason Kidd", "B) Mark Jackson", "C) John Stockton", "D) Steve Nash"],
  ["A) Hakeem Olajuwon", "B) Dikembe Mutombo", "C) Kareem Abdul-Jabbar", "D) Mark Eaton"],
  ["A) Gary Payton", "B) Jason Kidd", "C) Michael Jordan", "D) John Stockton"],
  ["A) Ray Allen", "B) Reggie Miller", "C) Stephen Curry", "D) James Harden"]]

def game(): 
    user_selections = []
    correct_selection = 0
    question_num = 0

    for key in questions:
        print( )
        print(key)
        for i in choices[question_num]:
            print(i)
        selection = input("Select (A, B, C, D): ").upper()
        user_selections.append(selection)

        correct_selection += answer_check(questions.get(key), selection)  
        question_num += 1  

    score(correct_selection, user_selections)

def answer_check(answer, selection):
  
    if answer == selection:
        print("Correct!")
        return 1 
    else: 
       print("Incorrect!") 
       return 0

def score(correct_selection, user_selections):
    score = int((correct_selection/len(questions)) * 100)
    print( )
    print("Results: ")
    print( )

    print("Answers: ")
    for i in questions:
      print(questions.get(i))
    print( )

    print("Selections: ")
    for i in user_selections:
      print(i)
    print( )

    print("Your score is: %" + str(score))

def play_again():
  response = input("Do you want to play again? (Yes or No): ").upper()

  if response == "YES":
    return True
  else:
    return False  

game()

while play_again():
  game()

print("Until Next Time!")