from ui.business_table import BusinessTable
from services.lead_finder import search_businesses
import customtkinter as ctk


def create_app():
    # -----------------------
    # Window Configuration
    # -----------------------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("LeadHunter AI")
    app.geometry("1200x700")

    # -----------------------
    # Sidebar
    # -----------------------
    sidebar = ctk.CTkFrame(app, width=220, corner_radius=0)
    sidebar.pack(side="left", fill="y")

    logo = ctk.CTkLabel(
        sidebar,
        text="LeadHunter AI",
        font=("Segoe UI", 22, "bold")
    )
    logo.pack(pady=30)

    buttons = [
        "🏠 Dashboard",
        "🔍 Find Leads",
        "📧 Outreach",
        "📊 Analytics",
        "⚙️ Settings"
    ]

    for text in buttons:
        btn = ctk.CTkButton(
            sidebar,
            text=text,
            width=180,
            height=40
        )
        btn.pack(pady=8)

    # -----------------------
    # Main Area
    # -----------------------
    main = ctk.CTkFrame(app)
    main.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    title = ctk.CTkLabel(
        main,
        text="Dashboard",
        font=("Segoe UI", 30, "bold")
    )
    title.pack(anchor="w", pady=(10, 20))

    # -----------------------
    # Search Section
    # -----------------------
    search_frame = ctk.CTkFrame(main)
    search_frame.pack(fill="x", pady=10)

    keyword = ctk.CTkEntry(
        search_frame,
        placeholder_text="Enter business niche (e.g. Supplements)",
        width=300
    )
    keyword.pack(side="left", padx=10, pady=10)

    country = ctk.CTkOptionMenu(
        search_frame,
        values=["USA", "Canada", "UK", "Australia"]
    )
    country.pack(side="left", padx=10)

    # -----------------------
    # Business Table
    # -----------------------
    table = BusinessTable(main)
    table.pack(fill="both", expand=True, pady=20)

    # -----------------------
    # Search Function
    # -----------------------
    def find_businesses():
        keyword_text = keyword.get().strip()
        country_text = country.get()

        if keyword_text == "":
            return

        data = search_businesses(keyword_text, country_text)

        if not data:
            return

        # Create a fresh table every search
        nonlocal table
        table.destroy()

        table = BusinessTable(main)
        table.pack(fill="both", expand=True, pady=20)

        for name, website in data:
            table.add_row(
                company=name,
                website=website,
                country=country_text,
                status="New"
            )

    # -----------------------
    # Search Button
    # -----------------------
    search_btn = ctk.CTkButton(
        search_frame,
        text="Find Businesses",
        command=find_businesses
    )
    search_btn.pack(side="left", padx=10)

    return app