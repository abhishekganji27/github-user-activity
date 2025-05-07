# github-user-activity

## Brief Introduction
- This is a CLI tool that can be used to fetch key actions performed by a GitHub user in the last 90 days. 
- The actions performed by the GitHub user will trigger events in GitHub. These events are recorded by GitHub.  
- The latest 300 events from the last 90 days will be fetched. (GitHub API limits.)
- This tool is written in Python. 

## Setup
- Fork and clone this repository onto your local machine. 
- (Optional Step) In your terminal/cmd prompt, create a python virtual environment using the command python -m .venv <virtual-environment-name>
- Navigate to the root location in this project. 
- Install the requirements for the application by running pip install -r requirements.txt

## Usage 
- To fetch the GitHub activity for a user, just type the following in your terminal.
- python main.py <github-username>
- The output will be visible in the terminal.

This project idea was taken from the backend developer roadmap of roadmap.sh
Project page URL on roadmap.sh: https://roadmap.sh/projects/github-user-activity