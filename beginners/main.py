files_names = ['Countdown Timer','Fibonacci Sequence Generator','Prime Number Checker','Leap Year Checker','Rock, Paper, Scissors Game','Word Count in a Text','Unit Converter (Miles to Kilometers, etc.)','Temperature Converter (Celsius to Fahrenheit)','Basic Contact Book','Currency Converter','Hangman Game','Simple Mad Libs Generator','BMI Calculator','Password Generator','Random Joke Generator','Alarm Clock','Simple Stopwatch','Palindrome Checker','Multiplication Table Generator','Basic Interest Calculator','Binary to Decimal Converter','Number Factorizer','Area and Perimeter Calculator (Various Shapes)','Email Slicer (Username and Domain Extraction)','Find the GCD (Greatest Common Divisor)','Simple Quiz App','Vowel Counter','Number Reversal Program','Sum of Natural Numbers','Factorial Calculator','Reverse a String','Basic Shopping Cart System','Armstrong Number Checker','Odd or Even Number Identifier','Create a Basic Timer','Age Calculator','Simple Banking System','String Splitter','Sorting a List','FizzBuzz Game','Password Strength Checker','File Renaming Utility','Character Frequency Counter','Find the Second Largest Number in a List','Merge Two Lists','Matrix Addition and Subtraction','String Anagram Checker','Decimal to Binary Converter','Simple Tic-Tac-Toe Game','Random Password Generator','Voting System','Acronym Generator','Random Name Picker','Find the Maximum and Minimum in a List','Display Current Date and Time','Remove Duplicates from a List']

c=5

for index,file in enumerate(files_names):
    name = str("{:02d}".format(c))+f"-{file.lower().replace(' ','-')}"
    if index !=0:
        prev_file_name = str("{:02d}".format(c-1))+f"-{files_names[index-1].lower().replace(' ','-')}"+".html"
        next_file_name = str("{:02d}".format(c+1))+f"-{files_names[index+1].lower().replace(' ','-')}"+".html"
        with open('demo.html', 'r') as f:
            html_code = f.read()
            html_code = html_code.replace('[PROJECTTITLE]', file)
            html_code = html_code.replace('[NUMBER]', "{:02d}".format(c))
            html_code = html_code.replace('[PREVLINK]', prev_file_name)
            html_code = html_code.replace('[NEXTLINK]', next_file_name)
            with open(name+".html", 'w') as t:
                t.write(html_code)
    c+=1

