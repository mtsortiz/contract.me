from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.forms import FreelanceContractForm
from app.generator import generatePDFContract

import os

app = FastAPI()

# Obtener el directorio donde está este archivo
current_dir = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "..", "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contracts", response_class=HTMLResponse)
async def selectContract(request: Request):
    return templates.TemplateResponse("contractSelector.html", {"request": request})

@app.get("/contracts/freelancer", response_class=HTMLResponse)
async def freelancerContract(request: Request):
    return templates.TemplateResponse("freelancerForm.html", {"request": request})

@app.post("/contracts/freelancer")
async def loadFreelancerContract(
    request: Request,
    client_name: str = Form(...),
    client_document: str = Form(...),
    employee_name: str = Form(...),
    employee_document: str = Form(...),
    job_description: str = Form(...),
    price: str = Form(...),
    start_date: str = Form(...),
    due_date: str = Form(...)):
        form_data = FreelanceContractForm(
            client_name=client_name,
            client_document=client_document,
            employee_name=employee_name,
            employee_document=employee_document,
            job_description=job_description,
            price=price,
            start_date=start_date,
            due_date=due_date
        )
        output_path = generatePDFContract(form_data.dict())
        return FileResponse(output_path, filename="contrato.pdf", media_type="application/pdf")
