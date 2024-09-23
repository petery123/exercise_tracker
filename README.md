# exercise_tracker
Project Based Component: EXERCISE WEIGHT TRACKER

PROBLEM: Whenever I go to the gym to workout, I tend to forget the mass of the weights I use for the each workout so it gets hard to keep track of my progress and set a bench mark for the next workout.

SOLUTION: I built an Exercise Tracker that can help me to better keep track of the last weight I used for a particular exercise so I do not have to worry about forgetting every time I want to do that workout.

Using the tracker, the user can add workout sessions which is made up of exercises because like many people, I workout certain muscle groups on certain days. In each session, a workout can be added and the current weight. After using the application for several sessions, the user can also view their progress for each of the exercises.

When the application is closed, the data added is saved on a JSON file which is then reloaded at the start of the next program run into an object.

CHALLENGES FACED
Initially, I had a minor issue handling the importing of the modules due to wrong syntax. I also did a lot of considerations as to how I would handle the inputs and outputs from the terminal on the user interface since there were 3 layers in the application. I decided to make the user interface hadling a package of it’s own with 3 modules for the main page, session editor and individual exercise editor which made it easier to handle the code. Finally, I had a few problems with making the JSON file connection work properly because of the nesting of the objects (The sessions manager having a list of sessions in it and each session having a list of exercises in it also). 