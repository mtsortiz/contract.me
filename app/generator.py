import pdfkit
import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def generatePDFContract(data: dict, output_path: str= "contract.pdf") -> str:
    template = env.get_template("freelancerContract.html")
    html_content = template.render(data)
    pdfkit.from_string(html_content, output_path)
    return output_path