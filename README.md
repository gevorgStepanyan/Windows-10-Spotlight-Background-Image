# Windows 10 Spotlight Background Image

## Description

This application is designed to copy windows 10 spotlight images to a folder and set them as a wallpaper. The application is designed to be run in the background at login.

## Installation

To install the application, clone the repository and setup the following command to be run as a task at login. Follow this tutorial if you don't know how to do that: [How to Run a Program Automatically When Windows Starts](https://www.howtogeek.com/228467/how-to-make-a-program-run-at-startup-on-any-computer/).

```bash
python main.py
```

## Arguments

The main.py file accepts the following arguments:

- `--src_dir` or `-s` - The path to the windows spotlight folder. Default is the `%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets`.
  
- `--dest_dir` or `-d` - The path to the folder where the images will be saved. Default is the `./wallpapers`.

## How to run the application in the background at login

- Open the Task Scheduler
- Click on `Create Basic Task`
- Follow the wizard and set 
  - the trigger to `When I log on`
  - the action to `Start a program`

Once the task is setup, find it in the list of tasks and open its properties. In the `General` tab, check the `Hidden` checkbox to not have the command prompt window open at login.