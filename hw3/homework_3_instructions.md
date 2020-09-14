Homework 3
======

Setup Instructions
-----

1. Sign into GitHub
2. Sign into repl.it using GitHub authentication
3. Then copy n' paste GitHub Classroom invitation link into url

General Instructions
-------

- You have to work completely individually on this assignment.
    + You should never see anyone's code.
    + You can reference:
        * [Course materials](https://github.com/brianspiering/computation_course)
        * [Python documentation](https://docs.python.org/3/)
        * [Python Fundamentals videos](https://www.oreilly.com/library/view/python-fundamentals/9780135917411/)
        * [Intro to Python for Computer Science and Data Science book](https://learning.oreilly.com/library/view/intro-to-python/9780135404799/)
- Do not import anything else.
- Do not modify any testing code.
- __Every__ line of code you write must have a comment written by you. Comments should always describe the logic behind the code. Comments most often answer the "why" of code choices.
- The supported workflow is "Work in Repl.it". I'm happy to help out if there any questions or concerns with that workflow. You are free to use any other workflow (along as all your code stays private). However, I can not help if there are issues with a custom workflow.
- All help will be given during class time, office hours, or on Slack. All help will be given through replit. Please clearly state what you think the problem is. Also, share a link to your replit - Click "Share", then "invite someone with a join link".
- Submit assignments early and often through repl.it's version control. The assignments close at the due date and time. The last version you "commit & push" is what is graded.
- A video walk-through of setup, workflow, and submission is [here](https://www.youtube.com/embed/UAMk2taXIX4).

Specific Instructions
------

These problems are designed to practice processing lists with list methods and list comprehensions. Thus, your answers should be centered around those techniques.

You may be tempted to use `set` and `dict`. Those data structures may help (and you may use them), but they are not required to solved the problems. And yes, I have intentionally included many "unhashable" types to force you to process the data a list-centric way.

During list processing, you should try to minimize the number of passes through the data. If you make unnecessary passes through the data, you'll will lose points.

Hints on how to reduce the number of passes through the data:

- Use `list` methods.
- Use built-in functions.
- Use clever looping with `enumerate`, `zip`, and `reversed`.
- Use indexing to look at the remaining part of the data (in contrast to always looking at all the data).  

Just to emphasize it - you should be using as many [built-in functions](https://docs.python.org/3/library/functions.html) as possible. If there is a built-in function you could have used but instead you implemented something unnecessarily more complex, you will lose points.

General Grading Guidelines
------

- Effectiveness (50% of points per function)
    - Code implements both the letter and the spirit of the specification
    - Runs without errors
    - Passes all unit tests
    - Passes all tests within time limits
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Elegance (10% of points per function)
    + Uses Python idioms 
    + Selects correct data structures
    + Select correct built-in functions
    + Uses packages appropriately 
    + No unnecessarily repeated work 
    + No unnecessary hard coding
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Readability (10% of points per function)
    - Clear, semantic naming
    - A single line only contains a single idea
    - No unnecessary variables
    - Style follows [pep8](https://pep8.org/) conventions as much as possible
    - Consistent formatting
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Documentation (30% of points per function)
    + Each line has a comment
    + Each comment is a meaningful and complete thought
    + Each comment is consistent with [style guidelines](https://github.com/brianspiering/computation_course/blob/master/resources/advice/comment_style_guidelines.md)
    - Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Just to be clear - "implements both the letter and the spirit of the specification" means you do not use any part of the unit test or intentionally circumnavigate the requirements of the prompt. Assuming you follow both the letter and spirit of the specification, the "Effectiveness" grading category is judged entirely correct or not by the testing suite for that function. There is no partial credit for effectiveness for each respective function. 

Specific Grading Guidelines
------

Homework #3 (100 points):

- Strictly increasing  (10): 
    - Effectiveness (5)
    - Elegance (1)
    - Readability (1)
    - Documentation (3)
- All equal  (20): 
    - Effectiveness (10)
    - Elegance (2)
    - Readability (2)
    - Documentation (6)
- Duplicity problem  (20):   
    - Effectiveness (10)
    - Elegance (2)
    - Readability (2)
    - Documentation (6)  
- Dropped data problem  (20):   
    - Effectiveness (10)
    - Elegance (2)
    - Readability (2)
    - Documentation (6)  
- Valid pairs  (30):     
    - Effectiveness (15)
    - Elegance (3)
    - Readability (3)
    - Documentation (9)  
