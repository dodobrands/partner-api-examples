from __future__ import annotations
from datetime import datetime, timedelta
from services.apiService import ApiService
from models.getScheduleResponse import GetSchedulesResponse
from models.addSchedulesRequest import AddSchedulesRequest
from models.constants import DATE_FORMAT
import services.auth as auth
import services.config as config

# A method that changes the date of a specific schedule from one week to another
def scheduleToDate(
        schedule: GetSchedulesResponse.Schedule, # schedule to update
        weekFromMondayDate: datetime, # The first day of the week from which we copy the schedules
        weekToMondayDate: datetime # First day of the week for which we want to save the schedules
    ) -> AddSchedulesRequest.Schedule:

    deltaStartDays: int = (schedule.scheduledShiftStartAtLocal.date() - weekFromMondayDate.date()).days
    deltaEndDays: int = (schedule.scheduledShiftEndAtLocal.date() - weekFromMondayDate.date()).days

    scheduleStartDate: datetime = weekToMondayDate + timedelta(days= deltaStartDays)
    scheduleEndDate: datetime = weekToMondayDate + timedelta(days= deltaEndDays)

    scheduleToAdd: AddSchedulesRequest.Schedule = AddSchedulesRequest.Schedule.fromSchedule(schedule)
    scheduleToAdd.changeDate(
        newStartDate= scheduleStartDate,
        newEndDate= scheduleEndDate
    )
    return scheduleToAdd

# A method that copies a schedule from one week to another
def copySchedules(
        apiService: ApiService, # service for send http requests to DodoIs API
        unit: str, # Unit being processed
        weekFromMonday: datetime, # The first day of the week from which we copy the schedules
        weekToMonday: datetime # First day of the week for which we want to save the schedules
    ) -> None: 
    # Get the last day of the week from which copying occurs
    weekFromSunday: datetime = weekFromMonday + timedelta(days=6)
    # Load a schedule for a given unit for the period from the first to the last day of the copied week
    schedules: list[GetSchedulesResponse.Schedule] = apiService.getSchedules(
        units=[unit],
        beginFrom=weekFromMonday.date(),
        beginTo=(weekFromSunday + timedelta(days=1)).date()
    )

    if not any(schedules):
        return
    
    # Changing schedule dates for a new week
    schedulesToAdd: list[AddSchedulesRequest.Schedule] = [scheduleToDate(schedule, weekFromMonday, weekToMonday) for schedule in schedules]

    # Sending a request to save a new schedules
    apiService.addSchedules(schedulesToAdd)

# Get Auth token
token = auth.authorize()
# Configure api service
apiService = ApiService(config.api_url, token)
# Execute copy schedules
copySchedules(
    apiService=apiService,
    unit= config.unit,
    weekFromMonday= config.copySchedulesFromWeekMonday,
    weekToMonday= config.copySchedulesToWeekMonday,
)