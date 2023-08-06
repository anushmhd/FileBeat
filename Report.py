from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def gen_report(changes):
    pdf = SimpleDocTemplate("FileBeat_Report.pdf", pagesize=landscape(letter))
    story = []

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    heading_style = styles["Heading2"]

    title = Paragraph("FILE BEAT REPORT", title_style)
    story.append(title)
    story.append(Spacer(1, 10))

    table_data = [["Serial No.", "File Name", "File Path", "Change Type", "Timestamp"]]
    for idx, change in enumerate(changes, start=1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        table_data.append([idx, change["file"], change["path"], change["change"], timestamp])

    table = Table(table_data, colWidths=[50, 150, 150, 150, 150])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lavender),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.palevioletred),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    story.append(table)

    pdf.build(story)