# To-Do App

#### Description:
Welcome to the To-Do app, a simple yet powerful command-line tool designed to streamline your task management process. This project empowers users to organize their tasks efficiently through a set of intuitive menu options. Below, we'll explore the key features of the app, the structure of the code, and some design considerations.

## Features:
### 1. Add Task ✏️
   Users can easily add tasks to their to-do list by selecting option 1 from the menu. The app prompts users to enter the task title, and a new task is appended to the list with a default status of not completed.

### 2. Remove Task ✂️
   Removing tasks is made straightforward with option 2. The app displays a numbered list of tasks, allowing users to specify the task they wish to remove by entering the corresponding number.

### 3. Mark Complete ✅
   Task completion is a breeze with option 3. Similar to removing a task, users can choose a task from the list and mark it as complete, updating its status accordingly.

### 4. View All Tasks 📄
   Stay organized by reviewing all your tasks with option 4. The app displays each task's title along with its status, making it easy to track your progress.

### 5. Quit ❌
   When you're done managing tasks, choose option 5 to gracefully exit the To-Do app. A friendly farewell message bids you goodbye.


## Design Considerations:
- **User-Friendly Interface**: The menu-driven interface aims to be user-friendly, allowing individuals to interact with the app effortlessly.
- **Error Handling**: The code incorporates error handling to address invalid inputs, ensuring a smooth user experience. Users are prompted to re-enter information or return to the menu when errors occur.
- **Task Status Visualization**: The status of each task is visualized with emojis (✅ for completed, 🔴 for not completed), offering a quick glance at the task list's overall progress.
