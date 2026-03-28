# Task Tracker CLI

Task Tracker is a command-line interface (CLI) application designed to help you manage and track your tasks and to-do lists efficiently. With this CLI, you can add, update, delete, and track tasks, while storing them in a simple JSON file.

This project was created to help practice programming skills, including handling user inputs, interacting with the file system, and building a functional CLI tool.

## Features

- Add, update, and delete tasks
- Mark tasks as **in-progress**, **done**, or **to-do**
- List tasks by **status** (e.g., `done`, `todo`, `in-progress`)
- Automatically creates a JSON file to store tasks if it doesn't already exist
- Lightweight and easy to use

## Requirements

- A programming language of your choice (Python, JavaScript, etc.)
- JSON file for storing tasks
- Command line usage with positional arguments for task actions

### Task Properties

Each task in the tracker has the following properties:

- `id`: A unique identifier for the task
- `description`: A brief description of the task
- `status`: The current status of the task (can be `todo`, `in-progress`, or `done`)
- `createdAt`: The timestamp of when the task was created
- `updatedAt`: The timestamp of when the task was last updated

## Installation

To get started with the Task Tracker CLI:

1. Clone the repository:

   ```bash
   git clone https://github.com/bajracae/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Install the package:

   ```bash
   pip install .
   ```

   If you encounter a warning that the script is installed in a directory that’s not in your `PATH`, follow the instructions below to add it.

### Add `task_cli` to your PATH (if needed)

If you see a warning about the script not being in your `PATH`, add the following to your shell's configuration file:

- For **Bash**:

  ```bash
  echo 'export PATH=$PATH:/home/username/.local/bin' >> ~/.bashrc
  source ~/.bashrc
  ```

- For **Zsh**:

  ```bash
  echo 'export PATH=$PATH:/home/username/.local/bin' >> ~/.zshrc
  source ~/.zshrc
  ```

## Usage

### Adding a New Task

To add a task to your list:

```bash
task-cli add "Buy groceries"
```

This will add the task with the description `"Buy groceries"` to your task list and assign it a unique ID.

### Updating a Task

To update an existing task:

```bash
task-cli update <task_id> "New task description"
```

For example, to update task 1:

```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Deleting a Task

To delete a task:

```bash
task-cli delete <task_id>
```

For example, to delete task 1:

```bash
task-cli delete 1
```

### Marking a Task

You can mark tasks as **in-progress** or **done** using these commands:

- Mark a task as **in progress**:

  ```bash
  task-cli mark-in-progress <task_id>
  ```

- Mark a task as **done**:

  ```bash
  task-cli mark-done <task_id>
  ```

### Listing Tasks

To list all tasks:

```bash
task-cli list
```

To list tasks by status, use the following commands:

- List all **done** tasks:

  ```bash
  task-cli list done
  ```

- List all **to-do** tasks:

  ```bash
  task-cli list todo
  ```

- List all tasks that are **in-progress**:

  ```bash
  task-cli list in-progress
  ```

## Getting Started

Here’s a quick guide to getting started with the Task Tracker CLI:

### Set Up Your Development Environment

- Choose your preferred programming language (e.g., Python, JavaScript, etc.).
- Ensure you have a code editor or IDE installed (e.g., VSCode, PyCharm).

### Project Initialization

1. **Create a new project directory** for your Task Tracker CLI.
2. **Initialize version control** (e.g., using Git) to manage your project.

### Implementing Features

- Start by implementing the core functionality (e.g., adding tasks).
- Then, implement listing, updating, and deleting tasks.

### Testing and Debugging

- Test each feature individually (adding, updating, marking tasks, etc.).
- Use the JSON file to verify that tasks are being correctly stored and updated.

### Finalizing the Project

- Ensure all features are fully implemented and tested.
- Clean up the code and add comments where necessary.
- Write a good `README.md` to explain how to use the Task Tracker CLI.

## Contributing

We welcome contributions to improve the Task Tracker CLI! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit and push your changes (`git push origin feature-name`).
5. Submit a pull request.

## Useful Links

Project URL: https://roadmap.sh/projects/task-tracker
CLI application with Python: https://dev.to/kanakos01/create-a-cli-application-with-python-1j37

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
