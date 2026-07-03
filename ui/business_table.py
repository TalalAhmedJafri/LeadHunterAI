import customtkinter as ctk


class BusinessTable(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.current_row = 1

        headers = ["Company", "Website", "Country", "Status"]

        for col, header in enumerate(headers):
            label = ctk.CTkLabel(
                self,
                text=header,
                font=("Segoe UI", 14, "bold")
            )
            label.grid(row=0, column=col, padx=15, pady=10)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

        headers = ["Company", "Website", "Country", "Status"]

        for col, header in enumerate(headers):
            label = ctk.CTkLabel(
                self,
                text=header,
                font=("Segoe UI", 14, "bold")
            )
            label.grid(row=0, column=col, padx=15, pady=10)

        self.current_row = 1

    def add_row(self, company, website, country, status):
        values = [company, website, country, status]

        for col, value in enumerate(values):
            label = ctk.CTkLabel(
                self,
                text=value,
                anchor="w"
            )
            label.grid(
                row=self.current_row,
                column=col,
                padx=15,
                pady=5
            )

        self.current_row += 1