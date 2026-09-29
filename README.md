# Student Goal Tracker

## Introduction

**Student Goal Tracker** is a Python-based program designed to help students organize and track their academic goals. The program allows students to add goals, assign them to subjects, set deadlines, choose priorities, and monitor their progress.

The program stores the goals in a **JSON file**, allowing the data to remain available when the program is run again.

## Features

### 1. Add Goal

The user can add a new goal by entering:

* Goal name
* Subject name
* Deadline
* Priority
* Initial progress

The priority can be selected as:

* High
* Medium
* Low

The program also checks that:

* The deadline is not empty.
* The deadline follows the `dd-mm-yyyy` format.
* The deadline is not a past date.

### 2. View Goals

The user can view all the goals stored in the program.

For each goal, the program displays:

* Goal
* Subject
* Deadline
* Priority
* Progress
* Status

A goal with 100% progress is shown as **Completed**, while other goals are shown as **In Progress**.

### 3. Update Progress

The user can select a goal and update its progress between 0% and 100%.

### 4. Progress Report

The program provides an overall progress report containing:

* Total number of goals
* Number of completed goals
* Overall progress percentage

## Data Storage

The program uses a JSON file named:

`DATA.json`

The goals are stored in this file so that they can be loaded when the program starts again.

## Technologies Used

* Python
* JSON
* `datetime` module
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* File handling

## Program Structure

The main functions used in the program are:

* `save_goals()` – Saves goals to the JSON file.
* `add_goal()` – Adds a new goal.
* `view_goals()` – Displays stored goals.
* `update_progress()` – Updates the progress of a goal.
* `progress_report()` – Displays the overall progress report.

## Purpose

The purpose of this project is to provide students with a simple way to organize their goals and monitor their academic progress while demonstrating the practical use of Python programming concepts.

## Future Improvements

Possible improvements include:

* Adding the ability to edit or delete goals.
* Adding automatic reminders for approaching deadlines.
* Adding sorting by priority or deadline.
* Adding a graphical user interface.
* Adding more detailed progress statistics.
