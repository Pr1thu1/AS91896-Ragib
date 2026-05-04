_______________________


# A list of dictionaries to store questions and answers
quiz_questions = [
   {
       "question": "What is the output of: print(5 * 2)?",
       "options": ["10", "25", "52"],
       "answer": "10"
   },
   {
       "question": "What type of loop is used to repeat a block of code a fixed number of times?",
       "options": ["while", "for", "loop"],
       "answer": "for"
   },
   {
       "question": "What does 'if' do in Python?",
       "options": ["Starts a function", "Checks a condition", "Declares a variable"],
       "answer": "Checks a condition"
   },
   {
       "question": "Which function gets input from the user?",
       "options": ["input()", "print()", "str()"],
       "answer": "input()"
   },
   {
       "question": "What is the correct syntax to define a function?",
       "options": ["function myFunc():", "def myFunc():", "define myFunc():"],
       "answer": "def myFunc():"
   }
]


# Shuffle questions to randomize order
_____________________________________


# Initialize score counter
__________________


print("Welcome to the Year 12 Python Quiz!\n")


# Loop through each question
for i, q in enumerate(quiz_questions, 1):
   print(f"Q{i}: {q['question']}")
   for j, option in enumerate(q["options"], 1):
       print(f"  {j}. {option}")


   try:
       user_choice = int(input("Enter the number of your answer: "))
      _____________________________________________
           selected_answer = q["options"][user_choice - 1]
           if selected_answer == q["answer"]:
               print("Correct!\n")
               _________________________
           else:
               print(f"Incorrect. The correct answer was: {q['answer']}\n")
       ______
           print("Invalid choice. Moving to next question.\n")
   except ValueError:
       _________________________________________


# Final Score
print(f"Quiz Completed! Your final score: {score}/{len(quiz_questions)}")