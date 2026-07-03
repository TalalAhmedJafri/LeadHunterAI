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
            label.grid(
                row=0,
                column=col,
                padx=15,
                pady=10,
                sticky="w"
            )

    def clear(self):
        # Remove all widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Recreate headers
        headers = ["Company", "Website", "Country", "Status"]

        for col, header in enumerate(headers):
            label = ctk.CTkLabel(
                self,
                text=header,
                font=("Segoe UI", 14, "bold")
            )
            label.grid(
                row=0,
                column=col,
                padx=15,
                pady=10,
                sticky="w"
            )

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
                pady=5,
                sticky="w"
            )

        self.current_row += 1

    def get_all_data(self):
        data = []

        for row in range(1, self.current_row):
            values = []

            for col in range(4):
                widget = self.grid_slaves(row=row, column=col)

                if widget:
                    values.append(widget[0].cget("text"))
                else:
                    values.append("")

            data.append(tuple(values))

        return data