from openpyxl import Workbook


def export_leads(leads):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Leads"

    # Header
    sheet.append(["Company", "Website", "Country", "Status"])

    # Data
    for lead in leads:
        sheet.append(lead)

    workbook.save("exports/leads.xlsx")