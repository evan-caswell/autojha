from pydantic import BaseModel
from datetime import date


class Task(BaseModel):
    task_name: str
    task_description: str
    is_indoors: bool


class JobData(BaseModel):
    job_name: str
    job_date: date
    job_location: str
    site_conditions: str
    tasks: list[Task]
