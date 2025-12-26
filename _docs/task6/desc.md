# Task 6: Automate Your Test Suite (Bonus Task)

## What you'll learn 
What continuous integration is and why it is useful for developers

## What you'll do
Implement a bash script, which automatically runs the test suite

---

## Bonus task!
This is an optional bonus task! If you do not wish to complete it, please type N/A into the text field below to finish the program. 

### Background information

Continuous integration is the practice of frequently merging the feature branch you are working on with the main branch shared by everyone else working on the same codebase. The goal of continuous integration is to replace large, conflicting merges with smaller, gradual changes. Consider a scenario wherein four developers are working on different parts of the same codebase. This codebase has a main branch, as well as a one-feature branch per developer.

Three of the developers are using a continuous integration workflow. They make small incremental changes, commit them, and merge their feature branches into main several times a day. The fourth developer decides against the practice, creates a feature branch when they start work on their ticket, and does not attempt to merge until a week later when it is complete. Unfortunately, the main branch has changed significantly by the time dev four attempts to merge their feature branch. 

They now must spend a significant amount of time combing through merge conflicts just to merge their feature branch. Needless to say, they don’t have a good time. The three developers using a CI workflow kept their feature branches relatively up to date with main, and as such, spent far less time resolving merge conflicts and more time on the company ping-pong tables.

Furthermore, most CI engines have powerful automated testing and deployment capabilities. In addition to avoiding merge conflicts, the CI engine ensures all tests pass with each commit and can even deploy them to staging environments. As such, developers are instantly made aware that their code behaves as expected when combined with everyone else's. In this task, you will focus on the test automation side of CI — your goal is to make the test you created in the last task executable by a CI engine.

### Task instructions

In this task, you will implement a bash script, which automatically runs the test suite you created in the last task. You could integrate this script into a CI engine to allow the test suite to run automatically. The bash script should do the following:

1. Activate the project virtual environment.
2. Execute the test suite.
3. Return exit code 0 if all tests passed, or 1 if something went wrong.

When you’ve finished implementing your bash script, commit and push your changes, then submit a link to your repo below! 