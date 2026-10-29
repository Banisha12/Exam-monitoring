import os
from fpdf import FPDF
import pandas as pd

# 1. Install the library first: pip install fpdf

# Create the reports folder
os.makedirs('../reports', exist_ok=True)

print("📄 Generating 15,000 PDF reports... (This might take a minute)")

# Load the AI reports metadata
reports_df = pd.read_csv('../data/synthetic/ai_reports_large.csv')

# Generate a simple PDF for the first 100 sessions (to save time)
# In production, you would generate all 15,000
for index, row in reports_df.head(100).iterrows():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt=f"ExamGuard AI Report - Session {row['session_id']}", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Candidate ID: {row['candidate_id']}", ln=True)
    pdf.cell(200, 10, txt=f"Summary: {row['summary']}", ln=True)
    pdf.cell(200, 10, txt=f"Model Version: {row['model_version']}", ln=True)
    
    # Save the file to the reports folder
    filepath = f"../reports/session_{row['session_id']}.pdf"
    pdf.output(filepath)

print("✅ Successfully generated 100 sample PDF reports in the 'reports' folder!")