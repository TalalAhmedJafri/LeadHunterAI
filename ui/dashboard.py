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
    # Results Box
    # -----------------------
    results = ctk.CTkTextbox(main, height=400)
    results.pack(fill="both", expand=True, pady=20)

    def find_businesses():
        results.delete("1.0", "end")

        keyword_text = keyword.get().strip()
        country_text = country.get()

        data = search_businesses(keyword_text, country_text)

        if not data:
            results.insert("end", "No businesses found.")
            return

        for i, (name, website) in enumerate(data, start=1):
            results.insert(
                "end",
                f"{i}. {name}\nWebsite: {website}\n\n"
            )

    search_btn = ctk.CTkButton(
        search_frame,
        text="Find Businesses",
        command=find_businesses
    )
    search_btn.pack(side="left", padx=10)

    results.insert(
        "end",
        "Welcome to LeadHunter AI!\n\n"
        "Type Supplements or Skincare and click Find Businesses."
    )

    return app