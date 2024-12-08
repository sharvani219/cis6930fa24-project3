import pdfplumber
import re
from pypdf import PdfReader
import urllib.request
import sqlite3
import argparse
from pypdf import PdfReader
import os
from collections import defaultdict
import re

def extract_data_from_pdf(pdf_path):
    """
    Extracts incident data from a NormanPD-style PDF and structures it into a list of rows.
    Does not perform any post-processing like adding 'Count' column or dropping rows.
    """
    reader = PdfReader(pdf_path)
    nature_counts = defaultdict(int)
    incidents = []  

    for page in reader.pages:
        text_lines = page.extract_text(
            extraction_mode="layout", layout_mode_space_vertically=False
        ).split("\n")

        if text_lines:
            for line in text_lines:
                line = line.strip()
                if "Incident Report" in line or "Page" in line:
                    continue

                if line:
                    fields = re.split(r'\s{2,}', line)  # Split by two or more whitespace
                    if len(fields) >=4:
                        incident_time = fields[0]  
                        incident_number = fields[1]  
                        incident_location = fields[2]  
                        nature = fields[3]  
                        incident_ori = fields[4] if len(fields) > 4 else None 
                        
                        # Count the nature type
                        nature_counts[nature] += 1
                        incidents.append((incident_time, incident_number, incident_location, nature, incident_ori))

    return nature_counts, incidents  
