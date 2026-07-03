import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.pack_propagate(False)

        # ------------------------
        # Logo
        # ------------------------
        logo = ctk.CTkLabel(
            self,
            text="🚀 LeadHunter AI",
            font=("Segoe UI", 22, "bold")
        )
        logo.pack(pady=(30, 25))

        # ------------------------
        # Menu Buttons
        # ------------------------
        self.create_button("🏠 Dashboard")
        self.create_button("🔍 Find Leads")
        self.create_button("📧 Outreach")
        self.create_button("📊 Analytics")
        self.create_button("⚙️ Settings")

    def create_button(self, text):
        button = ctk.CTkButton(
            self,
            text=text,
            width=180,
            height=42,
            corner_radius=10
        )

        button.pack(pady=8)