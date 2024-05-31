from collections.abc import Generator
from datetime import datetime
from models.constants import DATE_TIME_FORMAT

class ArrayHelper:
    def getArrayChunks(list: list[any], chunkSize: int) -> Generator[list[any]]:
        chunkSize = max(1, chunkSize)
        return (list[i:i+chunkSize] for i in range(0, len(list), chunkSize))
    
class DateHelper:
    def strToDateTime(dateTimeStr: str) -> datetime:
        return datetime.strptime(dateTimeStr, DATE_TIME_FORMAT)

    def setDate(current: datetime, newDate: datetime) -> datetime:
        return datetime(
                year= newDate.year,
                month= newDate.month,
                day= newDate.day,
                hour= current.hour, 
                minute= current.minute,
                second= current.second,
                microsecond= current.microsecond)