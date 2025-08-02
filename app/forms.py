from pydantic import BaseModel
from datetime import date

class FreelanceContractForm(BaseModel):
    client_name: str
    client_document: str
    employee_name: str
    employee_document: str
    job_description: str
    price: str
    start_date: str
    due_date: str


    