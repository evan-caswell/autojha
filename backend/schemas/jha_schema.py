from pydantic import BaseModel
from datetime import date


class Task(BaseModel):
    task_name: str
    task_description: str
    is_indoors: bool


class JobData(BaseModel):
    job_name: str
    job_date: str
    job_location: str
    site_conditions: str
    tasks: list[Task]


class JHATask(BaseModel):
    task_name: str
    task_description: str
    task_hazards: list[str]
    task_control_measures: list[str]
    task_ppe: list[str]


class JHA(BaseModel):
    job_data: JobData
    weather: list[str]
    site_hazards: list[str]
    site_control_measures: list[str]
    site_ppe: list[str]
    jha_tasks: list[JHATask]
