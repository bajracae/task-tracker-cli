from setuptools import setup

setup(
    name="task_cli",
    version="1.0",
    packages=["task_cli"],
    entry_points={
        "console_scripts": ["task-cli = task_cli.__main__:main"],
    },
    description="CLI app to track your tasks and manage your to-do list ",
    author="abajrach",
    url="https://github.com/bajracae/task-tracker-cli",
    python_requires=">=3.6",
)