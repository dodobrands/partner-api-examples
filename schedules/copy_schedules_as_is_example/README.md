# Examples of working with scheduling APIs

- copySchedulesAsIs.py - copying a schedule from one week to another
- copySchedulesByAvailability.py - Copying a schedule from one week to another by employee availability
- removeSchedules.py - Removing shifts from the schedule

## Required Dependencies

- Python

## Before launch

Open `services.config.py`
- set your auth token (`token`)
- set the unit ID (`unit`)
- set the first days of the copied (`copySchedulesFromWeekMonday`) and target (`copySchedulesToWeekMonday`) week

## Launch via IDE

You can use IDE. For example VS Code or PyCharm. In this case, the page you need to start will open in your browser

## Manual launch

python ./copySchedulesAsIs.py
python ./copySchedulesByAvailability.py
python ./removeSchedules.py


