import customtkinter as ctk
from tkinter import messagebox

from controllers.lead_controller import LeadController
from ui.sidebar import Sidebar
from ui.header import Header
from ui.stats_cards import StatsCards
from ui.business_table import BusinessTable
from services.export_service import export_to_excel
from database.database import save_business, get_all_businesses

def create_app():
    # -----------------------------
    # Window
    # -----------------------------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("LeadHunter AI")
    app.geometry("1400x800")

    # -----------------------------
    # Sidebar
    # -----------------------------
    sidebar = Sidebar(app)
    sidebar.pack(side="left", fill="y")

    # -----------------------------
    # Main Area
    # -----------------------------
    main = ctk.CTkFrame(app)
    main.pack(side="right", fill="both", expand=True)

    # -----------------------------
    # Header
    # -----------------------------
    header = Header(main)
    header.pack(fill="x", padx=20, pady=(20, 10))

    # -----------------------------
    # Search Area
    # -----------------------------
    search_frame = ctk.CTkFrame(main)
    search_frame.pack(fill="x", padx=20, pady=10)

    keyword = ctk.CTkEntry(
        search_frame,
        placeholder_text="Enter business niche (e.g. Supplements)",
        width=350
    )
    keyword.pack(side="left", padx=10, pady=15)

    country = ctk.CTkOptionMenu(
        search_frame,
        values=["USA", "Canada", "UK", "Australia"]
    )
    country.set("USA")
    country.pack(side="left", padx=10)

    # -----------------------------
    # Statistics
    # -----------------------------
    stats = StatsCards(main)
    stats.pack(fill="x", padx=20, pady=10)

    # -----------------------------
    # Business Table
    # -----------------------------
    table = BusinessTable(main)
    table.pack(fill="both", expand=True, padx=20, pady=20)

    # -----------------------------
    # Find Businesses
    # -----------------------------
    def find_businesses():

        table.clear()

        keyword_text = keyword.get().strip()
        country_text = country.get()

        if keyword_text == "":
            messagebox.showwarning(
                "Missing Keyword",
                "Please enter a business niche."
            )
            return

        try:
            businesses = LeadController.find(
                keyword_text,
                country_text
            )

            if not businesses:
                table.add_row(
                    "No businesses found",
                    "-",
                    country_text,
                    "-"
                )
                return

            for company, website in businesses:

                save_business(
                    company,
                    website,
                    country_text,
                    "New"
                )

                table.add_row(
                    company,
                    website,
                    country_text,
                    "New"
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    # -----------------------------
    # Export Excel
    # -----------------------------
    def export_excel():

        data = table.get_all_data()

        if len(data) == 0:
            messagebox.showwarning(
                "No Data",
                "There is no data to export."
            )
            return

        filename = export_to_excel(data)

        messagebox.showinfo(
            "Export Complete",
            f"Excel file saved successfully!\n\n{filename}"
        )

    def load_saved_leads():

        table.clear()

        businesses = get_all_businesses()

        print("Businesses loaded:", businesses)

        if len(businesses) == 0:
            messagebox.showinfo(
               "Saved Leads",
               "No saved leads found."
            )
            return

        for company, website, country, status in businesses:
           print(company)

           table.add_row(
               company,
               website,
               country,
               status
            )
    # -----------------------------
    # Buttons
    # -----------------------------
    search_btn = ctk.CTkButton(
        search_frame,
        text="🔍 Find Businesses",
        command=find_businesses
    )
    search_btn.pack(side="left", padx=10)

    export_btn = ctk.CTkButton(
        search_frame,
        text="📤 Export Excel",
        command=export_excel
    )
    export_btn.pack(side="left", padx=10)

    saved_btn = ctk.CTkButton(
         search_frame,
         text="📂 Saved Leads",
         command=load_saved_leads
    )

    saved_btn.pack(side="left", padx=10)

    return app