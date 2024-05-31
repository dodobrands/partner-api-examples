import services.auth as auth
import services.config as config
from models.constants import DATE_FORMAT
from datetime import datetime, timedelta
from services.apiService import ApiService
from services.helper import Confirmation
from models.getScheduleResponse import GetSchedulesResponse
    
def deleteSchedulesOnWeek(apiService: ApiService, unit: str, weekMondayDate: datetime):
    # Get the last day of the week from which copying occurs
    weekSundayDate = weekMondayDate + timedelta(days=6)
    # Load a schedule for a given unit for the period from the first to the last day of the copied week
    schedules: list[GetSchedulesResponse.Schedule] = apiService.getSchedules(
        units=[unit],
        beginFrom=weekMondayDate.date(),
        beginTo=(weekSundayDate + timedelta(days=1)).date()
    )
    
    if not any(schedules):
        return
    
    # Sending a request to delete a schedule
    for schedule in schedules:
        apiService.deleteSchedule(schedule.id)

# Get Auth token
token = auth.authorize()
# Configure api service
apiService = ApiService(config.api_url, token)
# Execute the schedule deletion method
deleteSchedulesOnWeek(
    apiService=apiService,
    unit=config.unit,
    weekMondayDate=config.copySchedulesToWeekMonday
)