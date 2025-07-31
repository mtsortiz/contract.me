from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Obtener el directorio donde está este archivo
current_dir = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "..", "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/select-contract", response_class=HTMLResponse)
async def selectContract(request: Request):
    return templates.TemplateResponse("contractSelector.html", {"request": request})

@app.get("/contracts/freelancer", response_class=HTMLResponse)
async def freelancerContract(request: Request):
    return templates.TemplateResponse("freelancerContract.html", {"request": request})

@app.post("/contracts/freelancer")
async def loadFreelancerContract(
    request: Request,
    clientName: str = Form(...),
    jobDescription: str = Form(...),
    date: str = Form(...),  
    price: str = Form(...)):

    contract = f"""
    CONTRATO DE SERVICIOS FREELANCE

    Entre el/la cliente {clientName} y el prestador de servicios se acuerda lo siguiente:

    Tareas a realizar:
    {jobDescription}

    Fecha estimada de entrega:
    {date}
    
    Precio acordado:
    {price}

    Fecha de generación: a completar manualmente.

    Firma de las partes: __________________________
    """
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "generatedContract": contract
    })