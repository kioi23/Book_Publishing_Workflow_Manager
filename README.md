 Book Publishing Workflow Manager

Hey, I'm a student and I am working on a lab that uses mostly python and I need clear explanations and step by step guide to it, provide reasons to your choices, also use the resources provided as reference. Use this mvp below to create the CLI project. Make sure to make me understand all the codes as well. My github repo link(https://github.com/kioi23/Book_Publishing_Workflow_Manager)
Start by providng a BDD of the project in a file called bdd.txt
 
Book Publishing Workflow Manager 
Project Description
A CLI system that manages authors, editors, books, and editing tasks throughout the publishing process.

Project MVP
Register authors and editors.
Create book projects.
Assign editing tasks.
Track publishing milestones.

User Stories
As an editor, I should be able to assign revisions.
As an author, I should be able to view editing feedback.
As a publisher, I should be able to monitor book progress.

Here is the main project;

Summative Lab: Python Project Management CLI Tool 

You will build a Python-based Command-Line Interface (CLI) application that manages a simulated multi-user project tracker system. The CLI should allow users to:

Create and manage users, projects, and tasks.
Display and search projects assigned to specific users.
Use file IO to persist data locally.
Use pip to manage external packages (e.g., for pretty printing, date formatting, or input validation).
Structure code using modules, classes, and object relationships.
Document, test, and debug your solution.
The Scenario: Create a Command-Line Project Management Tool 
You are tasked with creating a command-line project management tool for a team of developers. The tool should allow administrators to manage users, projects, and tasks through structured CLI commands. The system must support:

Creating and listing users via the command line.
Adding projects to specific users and displaying their associated projects.
Assigning tasks to projects and marking them as complete.
Editing and persisting project/task data using file I/O.
Navigating the tool with clear, user-friendly CLI commands.
Managing data relationships like one-to-many (users to projects) and many-to-many (projects to tasks with contributors).
Create and manage users, projects, and tasks.

Tools and Resources - here are the resources
PythonLinks to an external site. 3.10+ (https://www.python.org/) =>
VS CodeLinks to an external site. (or IDE of your choice)
Git + GitHubLinks to an external site. ()
Python Standard LibraryLinks (https://docs.python.org/3/library/index.html) to an external site. (argparse, os, json, etc.)
Optional: External packages such as rich or python-dateutil
My github repository link(https://github.com/kioi23/Book_Publishing_Workflow_Manager)

Also guide me on where to commit to gitbub, and the commit message, ensure to include brief relevant comments...emphasize on python in the explanations, keep in mind you are explaining to a beginner. follow the following instructions I will provide closely;


Instructions
Task 1: Define the Problem
Design a CLI tool that enables:

1. Admins to manage users and projects.
2. Each user to have one or more projects.
3. Each project to have one or more tasks.
4. CLI commands to add, view, and update these entities.

Example CLI Actions
add-user --name "Alex"
add-project --user "Alex" --title "CLI Tool"
add-task --project "CLI Tool" --title "Implement add-task"

Task 2: Determine the Design
1. Classes: User, Project, Task
2. Relationships:
One-to-many: User -> Projects
One-to-many: Project -> Tasks
3. Attributes
Users: name, email
Projects: title, description, due_date
Tasks: title, status, assigned_to
4. File Structure
main.py: CLI entry point
models/: contains class definitions
data/: local JSON or CSV file storage
utils/: helper functions, custom hooks
5. Persistence
Use json for saving/loading users, projects, and tasks
6. Package Setup:
External dependencies listed in requirements.txt or a pipfile

Task 3: Develop the Code
1. Set Up CLI Entry
Use argparse to define CLI structure.
Implement subcommands like add-user, list-projects, complete-task.
2. Build Object Model
Use classes for User, Project, and Task.
Apply __init__, instance methods, and relationships.
Use class methods to create or retrieve object collections.
Implement __str__() or __repr__() for clean CLI output.
3. Add OOP Features
Use @property and setter methods to control access to attributes.
Use class attributes (e.g., ID counters).
Add inheritance where appropriate (e.g., Person → User).
4. Configure File IO
Save and load objects via JSON files.
Handle missing files or malformed data with try-except.
Use Python scripting best practices (if __name__ == "__main__").
5. Use External Packages
Install and use at least one PyPi package (e.g., rich, tabulate, typer).
Track packages in requirements.txt or a pipfile

Task 4: Test and Debug
1. Add unit tests for your class methods and CLI logic.
2. Test input/output interactions using mock data.
3. Use print/logging/debugger to trace logic.
4. Refactor large files into reusable modules.

Task 5: Document and Maintain
1. Comment on all class methods and utility functions.
2. Create a README.md with:
Setup instructions
How to run CLI commands
Overview of features and known issues
3. Ensure all code is pushed to GitHub.


->Ensure you achieve the grading criteria that I will also provide below

Submission and Grading Criteria
1.Submit a public GitHub repo that includes:
-Complete source code
-Data files (JSON or CSV)
-A README.md with clear instructions
-Requirements.txt file or a pipfile with dependencies
-Test files, if applicable
2.Review the rubric below as a guide for how this lab will be graded.
3.Complete your assignment using your preferred IDE.
4.When you are ready, push your final script to GitHub.
5. Share the link to your GitHub repo below and submit your assignment.


Summative Lab: Python Project Management CLI Tool
Criteria	Ratings	Pts
This criterion is linked to a Learning OutcomeObject-Oriented Design
20 pts
Excelled
Advanced use of classes with inheritance, encapsulation, and dynamic behavior
16 pts
Met Expectations
Clear use of classes with defined relationships (e.g., User → Projects → Tasks)
8 pts
Attempted
Basic class structure, minimal relationships
0 pts
No Attempt
No class structures defined
20 pts
This criterion is linked to a Learning OutcomeCommand-Line Interface (CLI)
20 pts
Excelled
Modular CLI with subcommands, error handling, and user-focused design
16 pts
Met Expectations
Uses argparse to support multiple commands with help messages
8 pts
Attempted
CLI accepts basic input (e.g., single command)
0 pts
No Attempt
No CLI interaction implemented
20 pts
This criterion is linked to a Learning OutcomePersistence with File I/O
20 pts
Excelled
Full persistence with file error handling and clean load/save structure
16 pts
Met Expectations
JSON used effectively to save and load structured data
8 pts
Attempted
Data written to or read from file manually or incompletely
0 pts
No Attempt
No persistence logic present
20 pts
This criterion is linked to a Learning OutcomeCode Structure & Reusability
15 pts
Excelled
Highly modular project with clear separation of concerns (e.g., CLI, models, utils, data)
12 pts
Met Expectations
Classes separated into modules; reusable functions grouped in utils
6 pts
Attempted
Some use of modules or folders
0 pts
No Attempt
Code exists in one script with minimal separation
15 pts
This criterion is linked to a Learning OutcomeExternal Package Usage
10 pts
Excelled
Multiple packages used effectively; all dependencies managed in Pipfile
8 pts
Met Expectations
One PyPi package installed and used via Pipfile
4 pts
Attempted
One package installed manually
0 pts
No Attempt
No external packages used
10 pts
This criterion is linked to a Learning OutcomeTesting & Debugging
10 pts
Excelled
Full testing coverage for all major components; debugging tools or logs used during development
8 pts
Met Expectations
Unit tests for key logic or CLI functions using pytest or similar
4 pts
Attempted
Minimal or manual testing
0 pts
No Attempt
No testing present
10 pts
This criterion is linked to a Learning OutcomeGit Workflow & Management
5 pts
Excelled
Organized PRs, merged branches, and clean repo history
4 pts
Met Expectations
Uses feature branches; commits regularly with meaningful messages
2 pts
Attempted
Basic commits with minimal message quality
0 pts
No Attempt
No commits or history
5 pts
Total Points: 100

MAKE SURE YOU ACHIEVE AT LEAST 94%