# files_names = ['Countdown Timer','Fibonacci Sequence Generator','Prime Number Checker','Leap Year Checker','Rock, Paper, Scissors Game','Word Count in a Text','Unit Converter (Miles to Kilometers, etc.)','Temperature Converter (Celsius to Fahrenheit)','Basic Contact Book','Currency Converter','Hangman Game','Simple Mad Libs Generator','BMI Calculator','Password Generator','Random Joke Generator','Alarm Clock','Simple Stopwatch','Palindrome Checker','Multiplication Table Generator','Basic Interest Calculator','Binary to Decimal Converter','Number Factorizer','Area and Perimeter Calculator (Various Shapes)','Email Slicer (Username and Domain Extraction)','Find the GCD (Greatest Common Divisor)','Simple Quiz App','Vowel Counter','Number Reversal Program','Sum of Natural Numbers','Factorial Calculator','Reverse a String','Basic Shopping Cart System','Armstrong Number Checker','Odd or Even Number Identifier','Create a Basic Timer','Age Calculator','Simple Banking System','String Splitter','Sorting a List','FizzBuzz Game','Password Strength Checker','File Renaming Utility','Character Frequency Counter','Find the Second Largest Number in a List','Merge Two Lists','Matrix Addition and Subtraction','String Anagram Checker','Decimal to Binary Converter','Simple Tic-Tac-Toe Game','Random Password Generator','Voting System','Acronym Generator','Random Name Picker','Find the Maximum and Minimum in a List','Display Current Date and Time','Remove Duplicates from a List']

# c=5

# for index,file in enumerate(files_names):
#     name = str("{:02d}".format(c))+f"-{file.lower().replace(' ','-')}"
#     if index !=0:
#         prev_file_name = str("{:02d}".format(c-1))+f"-{files_names[index-1].lower().replace(' ','-')}"+".html"
#         next_file_name = str("{:02d}".format(c+1))+f"-{files_names[index+1].lower().replace(' ','-')}"+".html"
#         with open('demo.html', 'r') as f:
#             html_code = f.read()
#             html_code = html_code.replace('[PROJECTTITLE]', file)
#             html_code = html_code.replace('[NUMBER]', "{:02d}".format(c))
#             html_code = html_code.replace('[PREVLINK]', prev_file_name)
#             html_code = html_code.replace('[NEXTLINK]', next_file_name)
#             with open(name+".html", 'w') as t:
#                 t.write(html_code)
#     c+=1





# import os

# def list_files_in_directory(directory):
#     files = []
#     for file in os.listdir(directory):
#         if os.path.isfile(os.path.join(directory, file)):
#             files.append(file)
#     return files

# # Example usage
# directory_path = '.'  # Change '.' to the path of the directory you want to list
# print(list_files_in_directory(directory_path))

all_files = ['01-simple-calculator.html', '02-number-guessing-game.html', '03-to-do-app.html', '04-dice-rolling-simulator.html', '05-countdown-timer.html', '06-fibonacci-sequence-generator.html', '07-prime-number-checker.html', '08-leap-year-checker.html', '09-rock,-paper,-scissors-game.html', '10-word-count-in-a-text.html', '11-unit-converter-(miles-to-kilometers,-etc.).html', '12-temperature-converter-(celsius-to-fahrenheit).html', '13-basic-contact-book.html', '14-currency-converter.html', '15-hangman-game.html', '16-simple-mad-libs-generator.html', '17-bmi-calculator.html', '18-password-generator.html', '19-random-joke-generator.html', '20-alarm-clock.html', '21-simple-stopwatch.html', '22-palindrome-checker.html', '23-multiplication-table-generator.html', '24-basic-interest-calculator.html', '25-binary-to-decimal-converter.html', '26-number-factorizer.html', '27-area-and-perimeter-calculator-(various-shapes).html', '28-email-slicer-(username-and-domain-extraction).html', '29-find-the-gcd-(greatest-common-divisor).html', '30-simple-quiz-app.html', '31-vowel-counter.html', '32-number-reversal-program.html', '33-sum-of-natural-numbers.html', '34-factorial-calculator.html', '35-reverse-a-string.html', '36-basic-shopping-cart-system.html', '37-armstrong-number-checker.html', '38-odd-or-even-number-identifier.html', '39-create-a-basic-timer.html', '40-age-calculator.html', '41-simple-banking-system.html', '42-string-splitter.html', '43-sorting-a-list.html', '44-fizzbuzz-game.html', '45-password-strength-checker.html', '46-file-renaming-utility.html', '47-character-frequency-counter.html', '48-find-the-second-largest-number-in-a-list.html', '49-merge-two-lists.html', '50-matrix-addition-and-subtraction.html', '51-string-anagram-checker.html', '52-decimal-to-binary-converter.html', '53-simple-tic-tac-toe-game.html', '54-random-password-generator.html', '55-voting-system.html', '56-acronym-generator.html', '57-random-name-picker.html', '58-find-the-maximum-and-minimum-in-a-list.html', '59-display-current-date-and-time.html', '60-remove-duplicates-from-a-list.html']


for file in all_files:
    with open(file,"r") as f:
        data = f.read()
        data = data.replace('</head>','<link rel="stylesheet" href="../style.css" /></head>')
        with open(file,"w") as g:
            g.write(data)