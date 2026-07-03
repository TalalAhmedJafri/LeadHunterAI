from openpyxl import Workbook
from datetime import datetime
import os


def export_to_excel(data):
    """
    data = [
        (company, website, country, status),
        ...
    ]
    """

    os.makedirs("exports", exist_ok=True)

    filename = datetime.now().strftime(
        "exports/businesses_%Y-%m-%d_%H-%M-%S.xlsx"
    )

    wb = Workbook()
    ws = wb.active
    ws.title = "Businesses"

    # Headers
    ws.append([
        "Company",
        "Website",
        "Country",
        "Status"
    ])

    # Data
    for row in data:
        ws.append(row)

    wb.save(filename)

    return filename