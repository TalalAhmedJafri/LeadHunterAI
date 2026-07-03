import customtkinter as ctk

from controllers.lead_controller import LeadController
from ui.sidebar import Sidebar
from ui.header import Header
from ui.stats_cards import StatsCards
from ui.business_table import BusinessTable


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
    # Search Frame
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
    # Stats
    # -----------------------------
    stats = StatsCards(main)
    stats.pack(fill="x", padx=20, pady=10)

    # -----------------------------
    # Business Table
    # -----------------------------
    table = BusinessTable(main)
    table.pack(fill="both", expand=True, padx=20, pady=20)

    # -----------------------------
    # Search Function
    # -----------------------------
    def find_businesses():
        
        print("Keyword:", keyword.get())
        print("Country:", country.get())

        table.clear()

        keyword_text = keyword.get().strip()
        country_text = country.get()

        if keyword_text == "":
            table.add_row(
                "Please enter a keyword",
                "-",
                "-",
                "-"
            )
            return

        try:
            businesses = LeadController.find(
                keyword_text,
                country_text
            )

            print("Businesses:", businesses)

            if len(businesses) == 0:
                table.add_row(
                    "No businesses found",
                    "-",
                    country_text,
                    "-"
                )
                return

            for company, website in businesses:

                print(company, website)

                table.add_row(
                    company,
                    website,
                    country_text,
                    "New"
                )

        except Exception as e:

            print(e)

            table.add_row(
                "ERROR",
                str(e),
                "",
                ""
            )

    # -----------------------------
    # Search Button
    # -----------------------------
    search_btn = ctk.CTkButton(
        search_frame,
        text="🔍 Find Businesses",
        command=find_businesses
    )
    search_btn.pack(side="left", padx=10)

    return app