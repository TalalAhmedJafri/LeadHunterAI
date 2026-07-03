from database.database import create_database
from ui.dashboard import create_app

# Create the database when the app starts
create_database()

app = create_app()
app.mainloop()