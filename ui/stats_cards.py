import customtkinter as ctk


class StatsCards(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        stats = [
            ("Businesses", "0"),
            ("Contacted", "0"),
            ("Replies", "0"),
            ("Clients", "0"),
        ]

        for title, value in stats:

            card = ctk.CTkFrame(self, width=180, height=90)

            card.pack(side="left", padx=10, pady=10)

            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 14)
            ).pack(pady=(15, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Segoe UI", 26, "bold")
            ).pack()