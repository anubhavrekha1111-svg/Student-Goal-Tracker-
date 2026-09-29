# Student Goal Tracker – Project Statement

## Problem Statement

Students often have multiple academic goals, assignments, projects, and other tasks to complete. Keeping track of these goals, their deadlines, priorities, and completion status can become difficult.

The objective of this project is to develop a Python-based **Student Goal Tracker** that allows students to record their goals, assign subjects and deadlines, set priorities, and monitor their progress.

## Objectives

* To develop a simple goal management system for students.
* To allow users to add and store their academic goals.
* To assign a subject to each goal.
* To set and validate deadlines.
* To assign different priorities to goals.
* To track the progress of each goal.
* To generate an overall progress report.
* To store goal information using a JSON file.

## Methodology

The program starts by loading previously stored goals from a JSON file. If no saved data is available, an empty goal list is created.

The user is provided with a menu containing five options:

1. **Add Goal**
2. **View Goals**
3. **Update Progress**
4. **Progress Report**
5. **Exit**

When adding a goal, the user enters the goal name, subject, deadline, and priority. The program validates the entered deadline and prevents past or incorrectly formatted dates from being accepted.

Each goal is stored as a dictionary containing its goal name, subject, deadline, priority, and progress. These dictionaries are stored in a list and saved in `DATA.json`.

The progress of individual goals can be updated by selecting the corresponding goal number. The progress report then calculates the total number of goals, completed goals, and overall progress.

## Python Concepts Used

The project demonstrates the following Python concepts:

* Variables and data types
* Lists
* Dictionaries
* Functions
* `if-elif-else` statements
* `while` and `for` loops
* User input
* Exception handling
* File handling
* JSON data storage
* Date and time handling
* String formatting

## Expected Outcome

The program provides students with a simple system for recording and monitoring their goals. It helps organize goals according to their subjects, deadlines, and priorities while allowing students to track their progress.

The use of JSON file storage also allows the goal information to be saved and accessed again when the program is restarted.

## Conclusion

The **Student Goal Tracker** successfully demonstrates how Python can be used to solve a practical student-related problem.

The project combines basic Python programming concepts with file handling, JSON data storage, and date validation to create a functional goal-tracking system. It provides students with a simple method to organize their goals and monitor their progress.

The project can be further developed by adding features such as goal editing and deletion, reminders, sorting, graphical interfaces, and more detailed progress analysis.
