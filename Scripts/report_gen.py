from warnings import simplefilter
import re
from reportlab.pdfgen import canvas
from reportlab import *
from reportlab.rl_config import *
from reportlab.lib.units import cm, inch, mm, pica, toLength
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import csv




simplefilter(action='ignore', category=FutureWarning)


def gen_pdf(file_name, message):
    message = message.replace("#", "")
    pdf_file = file_name


    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rigthMargin=2*cm,leftMargin=2*cm,topMargin=2*cm,bottomMargin=2*cm)
    doc.build([Paragraph(message.replace("\n", "<br />"), getSampleStyleSheet()['Normal']), ])










