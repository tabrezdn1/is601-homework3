# Homework3
## 3 Levels Of Calculator

This assignment introduces the principles of object oriented programming, unit testing, and design principles such as SOLID, DRY, GRASP, and seperation of concerns.


In this repository, you can see that there are 3 branches:
1. master - Basic Calculator with functions
![alt text](<Screenshot 2024-02-13 at 7.33.49 PM.png>)
2. part2 - Intermediate Calculator with static methods on Calculator class and instance methods on Calculation class to perform operations on the data in the calculation instance.
![alt text](<Screenshot 2024-02-13 at 7.34.47 PM.png>)
3. part3 - Advanced Calculator with parameterized unit testing.
![alt text](<Screenshot 2024-02-13 at 7.35.35 PM.png>)

## Notes on Advanced Calculator
The advanced calculator in part 3 contains static methods on the Calculator, instance methods on the Calculation, and class methods on the Calculations class.  In addition, it has more advanced testing that uses parameterized test data and a fixture to make it easy to setup each test with consistent data.  There are also modifciations to the .pylintrc file to control pylint's code analysis.

## Calculator has following funtionalities

1. Has operations (add subtract, multiply, divide). 
2. Exception throwing and testing on divide by zero.
3. Use of static, class, and instance methods correctly.
4. Having a calculation class that stores the arthitmentic operation in a instance property.
5. Having a calculation history to store calculation instances.
6. Having the convenience methods on the calculations class to manage the history
7. Using parameterized test data.