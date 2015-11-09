# SmartLEDSpeaker
This is an advanced IoT application which allows for music to be streamed to an Intel Galileo board. 

## Git Instructions
1. Get the git command line client (Windows users should use Gitbash).
2. In some directory, use the following command to pull the project to your computer:

   <code>git clone https://github.com/kjwatson/SmartLEDSpeaker.git</code>

3. When working on a project, make sure you have the most recent version:

   <code>git pull origin master</code>

4. When you want to commit your work, first check the **status** of the project, **add** and files that are not being tracked, **commit** any files that have been changed, **pull** (merge if needed) from the current project, and then **push** the project to the repo. So for example:

```
// lists all of the files not staged for commit or not being tracked (in RED)
git status

// Add an untracked file MyFile.cpp
git add MyFile.cpp

// Commit all of your changes. It should begin a text-editor prompt.
git commit -a

// Now make sure you haven't created conflicts. If a merge conflict occurs,
// commit again.
git pull origin master

// Once you have fixed all issues and the project still compiles, then you may
// safely send your project to the repo.
git push origin master
```


