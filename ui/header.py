import customtkinter as ctk


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="LeadHunter AI Dashboard",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(side="left", padx=20, pady=15)

        user = ctk.CTkLabel(
            self,
            text="👤 Talal Ahmed",
            font=("Segoe UI", 16)
        )

        user.pack(side="right", padx=20)