# AutoMeetX
A library used to automate the google meet using python. This library is developed for automating virtual meetings and ensuring timely participation without manual intervention.

### Features
- __Automated Meeting Join__: Automatically joins Google Meet sessions based on a predefined schedule.
- __Automated Meeting Disconnect__: Monitors the meeting participant count and disconnects if fewer participants are detected, potentially indicating the end of the meeting.
- __Customizable Schedule__: Easily configurable schedule for different days of the week.
- __Notification System__: Sends notifications with meeting links when they are detected.

### Requirements
- Python 3.7
- Selenium
- pynput
- notify_run
- Google Chrome (or another compatible browser)
- ChromeDriver (or another compatible WebDriver)

### Installation
1. Clone the repo:
```bash
git clone https://github.com/dedsec995/assignmentx.git
cd assignmentx
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Download and set up [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) with your browser. Ensure that the WebDriver is available in your system's PATH.

### Usage
1. __Configuration__: Edit meet.py to configure your schedule, meeting links, and login credentials.
```bash
usrname = "your email Id"
passwrd = "your password"
LEC1 = "google meet link"
LEC2 = "google meet link"
# Add additional meeting links as needed

monday = [LEC1, LEC2, LEC3]
tuesday = [LEC2, LEC1, LEC3]
# Define schedules for other days
```
2. __Run the Scipt__: You can run the script directly using Python or set up a batch file (`run.bat`) for convenience.
```bash
python meet.py
```
Or execute the batch file:
```bash
run.bat
```
