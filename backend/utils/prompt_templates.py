from datetime import date
from backend.schemas.jha_schema import JobData


# TODO: Create a markdown template for standardize output of JHAs.
# Most consistent solution would be to receive structured JSON output to then create the
# the document from. This can be done using pydantic to create a response schema.
def jha_prompt(job_data: JobData, weather_data: dict):
    prompt = f"""
Given a JSON file with information about a job and the associated tasks,
write a text job hazard analysis (JHA).

JSON:
{job_data.model_dump_json()}

Weather data for the job location:
{weather_data}
"""
    
    return prompt
