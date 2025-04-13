import tkinter as tk # Import of the "tkinter" package, which is a graphical user interface (GUI) toolkit for Python.
import json # Import of the "json" package, which is used for managing and parsing JSON data.
import os # Import of the "os" package, which provides a way of using operating system-dependent functionality like reading or writing to the file system.
APP_SETTINGS = { # This creates a dictionary called "APP_SETTINGS" that contains default settings for the application.
    "theme": "Light", # Default theme (light) for the application.
    "font_size": 12 # Default font size (12) for the application.
} # This ends the dictionary definition.
SETTINGS_FILE = "settings.json" # This defines the name of the settings file as "settings.json".
def load_settings(): # A method is created called "load_settings" that loads the settings from the settings file.
    default_settings = APP_SETTINGS.copy() # This creates a copy of the default settings.
    if os.path.exists(SETTINGS_FILE): # This checks if the settings file exists.
        try: # This tries to open the settings file and load its contents.
            with open(SETTINGS_FILE, "r") as f: # This opens the settings file in read mode.
                s = json.load(f) # This loads the JSON data from the file.
            return s # This returns the loaded settings.
        except Exception as e: # If there is an error while loading the settings, it prints the error message.
            print("Error loading settings:", e) # This prints the error message.
            return default_settings # This returns the default settings.
    else: # If the settings file does not exist, it creates a new settings file with the default settings.
        return default_settings # This returns the default settings.
def save_settings_to_file(settings): # A method is created called "save_settings_to_file" that saves the settings to the settings file.
    with open(SETTINGS_FILE, "w") as f: # This opens the settings file in write mode.
        json.dump(settings, f, indent=4) # This writes the settings to the file in JSON format with an indentation of 4 spaces.
BOOKS_FILE = "books.json" # This defines the name of the books file as "books.json".
BORROWERS_FILE = "borrowers.json" # This defines the name of the borrowers file as "borrowers.json".
LOANS_FILE = "loans.json" # This defines the name of the loans file as "loans.json".
def load_book_data(): # A method is created called "load_book_data" that loads the book data from the books file.
    default_books = [ # This creates a list of default books.
        {"title": "The Great Gatsby"}, # A new book called "The Great Gatsby" is added to the list.
        {"title": "1984"}, # A new book called "1984" is added to the list.
        {"title": "To Kill a Mockingbird"}, # A new book called "To Kill a Mockingbird" is added to the list.
        {"title": "Pride and Prejudice"}, # A new book called "Pride and Prejudice" is added to the list.
        {"title": "The Catcher in the Rye"} # A new book called "The Catcher in the Rye" is added to the list.
    ] # This ends the list of default books.
    if not os.path.exists(BOOKS_FILE): # This checks if the books file exists.
        with open(BOOKS_FILE, "w") as f: # This opens the books file in write mode.
            json.dump(default_books, f, indent=4) # This writes the default books to the file in JSON format with an indentation of 4 spaces.
        return default_books # This returns the default books.
    else: # If the books file exists, it tries to load the book data from the file.
        try: # This tries to open the books file and load its contents.
            with open(BOOKS_FILE, "r") as f: # This opens the books file in read mode.
                books = json.load(f) # This loads the JSON data from the file.
            if not isinstance(books, list): # This checks if the loaded data is a list.
                return default_books # If the loaded data is not a list, it returns the default books.
            return books # This returns the loaded books.
        except Exception as e: # If there is an error while loading the book data, it prints the error message.
            print("Error loading book data:", e) # This prints the error message.
            return default_books # This returns the default books.
def load_borrowers_data(): # A method is created called "load_borrowers_data" that loads the borrower data from the borrowers file.
    default_borrowers = [ # This creates a list of default borrowers.
        {"name": "John Doe"}, # A new borrower called "John Doe" is added to the list.
        {"name": "Jane Smith"}, # A new borrower called "Jane Smith" is added to the list.
        {"name": "Alice Johnson"}, # A new borrower called "Alice Johnson" is added to the list.
        {"name": "Bob Brown"}, # A new borrower called "Bob Brown" is added to the list.
        {"name": "Carol White"} # A new borrower called "Carol White" is added to the list.
    ] # This ends the list of default borrowers.
    if not os.path.exists(BORROWERS_FILE): # This checks if the borrowers file exists.
        with open(BORROWERS_FILE, "w") as f: # This opens the borrowers file in write mode.
            json.dump(default_borrowers, f, indent=4) # This writes the default borrowers to the file in JSON format with an indentation of 4 spaces.
        return default_borrowers # This returns the default borrowers.
    else: # If the borrowers file exists, it tries to load the borrower data from the file.
        try: # This tries to open the borrowers file and load its contents.
            with open(BORROWERS_FILE, "r") as f: # This opens the borrowers file in read mode.
                borrowers = json.load(f) # This loads the JSON data from the file.
            if not isinstance(borrowers, list): # This checks if the loaded data is a list.
                return default_borrowers # If the loaded data is not a list, it returns the default borrowers.
            return borrowers # This returns the loaded borrowers.
        except Exception as e: # If there is an error while loading the borrower data, it prints the error message.
            print("Error loading borrowers data:", e) # This prints the error message.
            return default_borrowers # This returns the default borrowers.
def save_borrowers_data(borrowers): # A method is created called "save_borrowers_data" that saves the borrower data to the borrowers file.
    with open(BORROWERS_FILE, "w") as f: # This opens the borrowers file in write mode.
        json.dump(borrowers, f, indent=4) # This writes the borrowers to the file in JSON format with an indentation of 4 spaces.
def load_loans_data(): # A method is created called "load_loans_data" that loads the loan data from the loans file.
    default_loans = [ # This creates a list of default loans.
        {"borrower": "John Doe", "book": "1984"}, # A new loan is added with borrower "John Doe" and book "1984".
        {"borrower": "Jane Smith", "book": "To Kill a Mockingbird"} # A new loan is added with borrower "Jane Smith" and book "To Kill a Mockingbird".
    ] # This ends the list of default loans.
    if not os.path.exists(LOANS_FILE): # This checks if the loans file exists.
        with open(LOANS_FILE, "w") as f: # This opens the loans file in write mode.
            json.dump(default_loans, f, indent=4) # This writes the default loans to the file in JSON format with an indentation of 4 spaces.
        return default_loans # This returns the default loans.
    else: # If the loans file exists, it tries to load the loan data from the file.
        try: # This tries to open the loans file and load its contents.
            with open(LOANS_FILE, "r") as f: # This opens the loans file in read mode.
                loans = json.load(f) # This loads the JSON data from the file.
            if not isinstance(loans, list): # This checks if the loaded data is a list.
                return default_loans # If the loaded data is not a list, it returns the default loans.
            return loans # This returns the loaded loans.
        except Exception as e: # If there is an error while loading the loan data, it prints the error message.
            print("Error loading loans data:", e) # This prints the error message.
            return default_loans # This returns the default loans.
def save_loans_data(loans): # A method is created called "save_loans_data" that saves the loan data to the loans file.
    with open(LOANS_FILE, "w") as f: # This opens the loans file in write mode.
        json.dump(loans, f, indent=4) # This writes the loans to the file in JSON format with an indentation of 4 spaces.
class BasePage(tk.Frame): # This creates a class called "BasePage" that inherits from "tk.Frame". This is the base class for the Multi-Level Inheritance that will be used in the application.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "BasePage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.config(bg=self.get_bg_color()) # This sets the background color of the frame based on the current theme.
        self.parent = parent # This assigns the parent of the frame to the "parent" attribute.
    def get_bg_color(self): # This method returns the background color based on the current theme.
        return "#333333" if APP_SETTINGS["theme"] == "Dark" else "white" # This returns a dark gray color for the dark theme and white for the light theme.
    def get_fg_color(self): # This method returns the foreground color based on the current theme.
        return "white" if APP_SETTINGS["theme"] == "Dark" else "black" # This returns white for the dark theme and black for the light theme.
    def create_header(self, text): # This method creates a header label with the specified text.
        header = tk.Label(self, text=text, font=("Arial", APP_SETTINGS["font_size"], "bold"), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label with the specified text, font, background color, and foreground color.
        header.pack(pady=10) # This packs the label with a vertical padding of 10 pixels.
    def update_style(self): # This method updates the style of the frame and its children based on the current theme.
        bg_color = self.get_bg_color() # This gets the background color based on the current theme.
        fg_color = self.get_fg_color() # This gets the foreground color based on the current theme.
        self.config(bg=bg_color) # This sets the background color of the frame.
        self._update_children_styles(self, bg_color, fg_color) # This calls the helper method to update the styles of the children of the frame.
    def _update_children_styles(self, widget, bg_color, fg_color): # This is a helper method that recursively updates the styles of the children of the widget.
        for child in widget.winfo_children(): # A loop is created to iterate through all the children of the widget.
            try: # This tries to set the background color of the child widget.
                child.config(bg=bg_color) # This sets the background color of the child widget.
            except tk.TclError: # If there is an error while setting the background color, it passes.
                pass # This passes the error.
            try: # This tries to set the font size of the child widget.
                child.config(font=("Arial", APP_SETTINGS["font_size"])) # This sets the font size of the child widget.
            except tk.TclError: # If there is an error while setting the font size, it passes.
                pass # This passes the error.
            if isinstance(child, tk.Label): # This checks if the child widget is a label.
                try: # This tries to set the foreground color of the label.
                    child.config(fg=fg_color) # This sets the foreground color of the label.
                except tk.TclError: # If there is an error while setting the foreground color, it passes.
                    pass # This passes the error.
            if isinstance(child, tk.Button): # This checks if the child widget is a button.
                try: # This tries to set the foreground and background colors of the button.
                    child.config(fg=fg_color, activeforeground=fg_color, activebackground=bg_color) # This sets the foreground and background colors of the button.
                except tk.TclError: # If there is an error while setting the colors, it passes.
                    pass # This passes the error.
            if isinstance(child, tk.Entry): # This checks if the child widget is an entry field.
                try: # This tries to set the foreground and background colors of the entry field.
                    entry_bg = "gray20" if APP_SETTINGS["theme"] == "Dark" else "white" # This sets the background color of the entry field based on the current theme.
                    child.config(fg=fg_color, bg=entry_bg) # This sets the foreground and background colors of the entry field.
                except tk.TclError: # If there is an error while setting the colors, it passes.
                    pass # This passes the error.
            if isinstance(child, tk.Text): # This checks if the child widget is a text field.
                try: # This tries to set the foreground and background colors of the text field.
                    text_bg = "gray20" if APP_SETTINGS["theme"] == "Dark" else "white" # This sets the background color of the text field based on the current theme.
                    child.config(fg=fg_color, bg=text_bg) # This sets the foreground and background colors of the text field.
                except tk.TclError: # If there is an error while setting the colors, it passes.
                    pass # This passes the error.
            if child.winfo_class() == "Menubutton": # This checks if the child widget is a menubutton.
                try: # This tries to set the foreground and background colors of the menubutton.
                    child.config(fg=fg_color, bg=bg_color) # This sets the foreground and background colors of the menubutton.
                    menu = child["menu"] # This gets the menu of the menubutton.
                    menu.config(bg=bg_color, fg=fg_color) # This sets the background and foreground colors of the menu.
                except tk.TclError: # If there is an error while setting the colors, it passes.
                    pass # This passes the error.
            self._update_children_styles(child, bg_color, fg_color) # This recursively calls the helper method to update the styles of the children of the child widget.
class LibraryPage(BasePage): # This creates a class called "LibraryPage" that inherits from the "BasePage" class. This is the base class for all the pages in the application.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "LibraryPage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
class DashboardPage(LibraryPage): # This creates a class called "DashboardPage" that inherits from the "LibraryPage" class. This is the dashboard page of the application. This is the first true instance of Multi-Level Inheritance.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "DashboardPage" class. 
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.create_header("Library Management System Dashboard") # This creates a header label with the specified text.
        self.metrics_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the metrics section of the dashboard.
        self.metrics_frame.pack(pady=20) # This packs the metrics frame with a vertical padding of 20 pixels.
        self.total_borrowers = len(load_borrowers_data()) # This loads the borrower data and gets the total number of borrowers.
        self.total_loans = len(load_loans_data()) # This loads the loan data and gets the total number of loans.
        self.books_data = load_book_data() # This loads the book data.
        self.total_books = len(self.books_data) # This gets the total number of books.
        self.books_card = tk.Frame(self.metrics_frame, bd=2, relief="groove", padx=10, pady=10, bg=self.get_bg_color()) # This creates a frame for the books card in the metrics section.
        self.books_card.grid(row=0, column=0, padx=10) # This places the books card frame in the metrics section.
        books_label = tk.Label(self.books_card, text="Total Books", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the total books in the books card.
        books_label.pack() # This packs the label in the books card frame.
        self.books_value = tk.Label(self.books_card, text=str(self.total_books), font=("Arial", APP_SETTINGS["font_size"], "bold"), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the value of total books in the books card.
        self.books_value.pack() # This packs the value label in the books card frame.
        borrowers_card = tk.Frame(self.metrics_frame, bd=2, relief="groove", padx=10, pady=10, bg=self.get_bg_color()) # This creates a frame for the borrowers card in the metrics section.
        borrowers_card.grid(row=0, column=1, padx=10) # This places the borrowers card frame in the metrics section.
        borrowers_label = tk.Label(borrowers_card, text="Total Borrowers", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the total borrowers in the borrowers card.
        borrowers_label.pack() # This packs the label in the borrowers card frame.
        borrowers_value = tk.Label(borrowers_card, text=str(self.total_borrowers), font=("Arial", APP_SETTINGS["font_size"], "bold"), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the value of total borrowers in the borrowers card.
        borrowers_value.pack() # This packs the value label in the borrowers card frame.
        loans_card = tk.Frame(self.metrics_frame, bd=2, relief="groove", padx=10, pady=10, bg=self.get_bg_color()) # This creates a frame for the loans card in the metrics section.
        loans_card.grid(row=0, column=2, padx=10) # This places the loans card frame in the metrics section.
        loans_label = tk.Label(loans_card, text="Total Loans", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the total loans in the loans card.
        loans_label.pack() # This packs the label in the loans card frame.
        loans_value = tk.Label(loans_card, text=str(self.total_loans), font=("Arial", APP_SETTINGS["font_size"], "bold"), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the value of total loans in the loans card.
        loans_value.pack() # This packs the value label in the loans card frame.
        self.recent_books_label = tk.Label(self, text="Recently Added Books", font=("Arial", APP_SETTINGS["font_size"], "bold"), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the recently added books section.
        self.recent_books_label.pack(pady=10) # This packs the label for the recently added books section with a vertical padding of 10 pixels.
        self.recent_books_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the recently added books section.
        self.recent_books_frame.pack(pady=5) # This packs the frame for the recently added books section with a vertical padding of 5 pixels.
        self.populate_recent_books() # This calls the method to populate the recently added books section.
        refresh_button = tk.Button(self, text="Refresh Dashboard", command=self.refresh_dashboard, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to refresh the dashboard.
        refresh_button.pack(pady=15) # This packs the refresh button with a vertical padding of 15 pixels.
    def populate_recent_books(self): # This method populates the recently added books section with the most recent books.
        for widget in self.recent_books_frame.winfo_children(): # This loops through all the children of the recent books frame.
            widget.destroy() # This destroys the child widgets to clear the frame.
        recent_books = self.books_data[-5:] # This gets the most recent 5 books from the book data.
        for book in recent_books: # This loops through each book in the recent books.
            title = book.get("title", "Untitled") # This gets the title of the book or sets it to "Untitled" if not available.
            book_label = tk.Label(self.recent_books_frame, text=title, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the book title.
            book_label.pack(anchor="w", padx=20) # This packs the book title label with a left alignment and a horizontal padding of 20 pixels.
    def refresh_dashboard(self): # This method refreshes the dashboard by reloading the book data and updating the total number of books.
        self.books_data = load_book_data() # This reloads the book data.
        self.total_books = len(self.books_data) # This gets the total number of books.
        self.books_value.config(text=str(self.total_books)) # This updates the value label for total books.
        self.populate_recent_books() # This calls the method to populate the recently added books section.
class BooksPage(LibraryPage): # This creates a class called "BooksPage" that inherits from the "LibraryPage" class to which utilizes Multi-Level Inheritance. This is the page for managing books in the library.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "BooksPage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.create_header("Books Management") # This creates a header label with the specified text.
        search_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the search section of the books page.
        search_frame.pack(pady=10) # This packs the search frame with a vertical padding of 10 pixels.
        search_label = tk.Label(search_frame, text="Search Books:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the search section.
        search_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the search frame with a left alignment and a horizontal padding of 5 pixels.
        self.search_entry = tk.Entry(search_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the search input.
        self.search_entry.pack(side=tk.LEFT) # This packs the entry field in the search frame.
        self.search_entry.bind("<KeyRelease>", self.on_search_keyrelease) # This binds the key release event to the search entry field to trigger the search function.
        self.books_listbox = tk.Listbox(self, font=("Arial", APP_SETTINGS["font_size"]), width=50, height=10) # This creates a listbox to display the list of books.
        self.books_listbox.pack(pady=10) # This packs the listbox with a vertical padding of 10 pixels.
        add_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the add book section.
        add_frame.pack(pady=5) # This packs the add book frame with a vertical padding of 5 pixels.
        add_label = tk.Label(add_frame, text="New Book Title:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the add book section.
        add_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the add book frame with a left alignment and a horizontal padding of 5 pixels.
        self.add_entry = tk.Entry(add_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the new book title.
        self.add_entry.pack(side=tk.LEFT) # This packs the entry field in the add book frame.
        add_button = tk.Button(add_frame, text="Add Book", command=self.add_book, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to add a new book.
        add_button.pack(side=tk.LEFT, padx=5) # This packs the add book button in the add book frame with a horizontal padding of 5 pixels.
        remove_button = tk.Button(self, text="Remove Selected Book", command=self.remove_book, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to remove the selected book.
        remove_button.pack(pady=10) # This packs the remove book button with a vertical padding of 10 pixels.
        self.books_data = load_book_data() # This loads the book data.
        self.update_books_listbox() # This calls the method to update the books listbox with the loaded book data.
    def on_search_keyrelease(self, event): # This method is called when a key is released in the search entry field.
        self.update_books_listbox() # This calls the method to update the books listbox based on the search input.
    def update_books_listbox(self): # This method updates the books listbox with the filtered book data based on the search input.
        query = self.search_entry.get().strip().lower() # This gets the search query from the entry field and converts it to lowercase.
        self.books_data = load_book_data() # This reloads the book data.
        filtered_books = [book for book in self.books_data if query in book.get("title", "").lower()] # This filters the book data based on the search query.
        filtered_books.sort(key=lambda b: b.get("title", "").lower()) # This sorts the filtered book data alphabetically by title.
        self.books_listbox.delete(0, tk.END) # This clears the current contents of the books listbox.
        for book in filtered_books: # This loops through each book in the filtered book data.
            self.books_listbox.insert(tk.END, book.get("title", "Untitled")) # This inserts the book title into the books listbox.
    def add_book(self): # This method adds a new book to the book data.
        new_title = self.add_entry.get().strip() # This gets the new book title from the entry field and strips any leading or trailing whitespace.
        if new_title: # This checks if the new book title is not empty.
            books = load_book_data() # This reloads the book data.
            books.append({"title": new_title}) # This appends the new book to the book data.
            with open(BOOKS_FILE, "w") as f: # This opens the books file in write mode.
                json.dump(books, f, indent=4) # This writes the updated book data to the file in JSON format with an indentation of 4 spaces.
            self.add_entry.delete(0, tk.END) # This clears the entry field for the new book title.
            self.update_books_listbox() # This calls the method to update the books listbox with the updated book data.
    def remove_book(self): # This method removes the selected book from the book data.
        selection = self.books_listbox.curselection() # This gets the selected book from the books listbox.
        if selection: # This checks if a book is selected.
            selected_title = self.books_listbox.get(selection[0]) # This gets the title of the selected book.
            books = load_book_data() # This reloads the book data.
            books = [book for book in books if book.get("title", "") != selected_title] # This filters the book data to remove the selected book.
            with open(BOOKS_FILE, "w") as f: # This opens the books file in write mode.
                json.dump(books, f, indent=4) # This writes the updated book data to the file in JSON format with an indentation of 4 spaces.
            self.update_books_listbox() # This calls the method to update the books listbox with the updated book data.
class BorrowersPage(LibraryPage): # This creates a class called "BorrowersPage" that inherits from the "LibraryPage" class to which utilizes Multi-Level Inheritance. This is the page for managing borrowers in the library.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "BorrowersPage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.create_header("Borrowers Management") # This creates a header label with the specified text.
        search_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the search section of the borrowers page.
        search_frame.pack(pady=10) # This packs the search frame with a vertical padding of 10 pixels.
        search_label = tk.Label(search_frame, text="Search Borrowers:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the search section.
        search_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the search frame with a left alignment and a horizontal padding of 5 pixels.
        self.search_entry = tk.Entry(search_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the search input.
        self.search_entry.pack(side=tk.LEFT) # This packs the entry field in the search frame.
        self.search_entry.bind("<KeyRelease>", self.on_search_keyrelease) # This binds the key release event to the search entry field to trigger the search function.
        self.borrowers_listbox = tk.Listbox(self, font=("Arial", APP_SETTINGS["font_size"]), width=50, height=10) # This creates a listbox to display the list of borrowers.
        self.borrowers_listbox.pack(pady=10) # This packs the listbox with a vertical padding of 10 pixels.
        add_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the add borrower section.
        add_frame.pack(pady=5) # This packs the add borrower frame with a vertical padding of 5 pixels.
        add_label = tk.Label(add_frame, text="New Borrower Name:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the add borrower section.
        add_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the add borrower frame with a left alignment and a horizontal padding of 5 pixels.
        self.add_entry = tk.Entry(add_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the new borrower name.
        self.add_entry.pack(side=tk.LEFT) # This packs the entry field in the add borrower frame.
        add_button = tk.Button(add_frame, text="Add Borrower", command=self.add_borrower, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to add a new borrower.
        add_button.pack(side=tk.LEFT, padx=5) # This packs the add borrower button in the add borrower frame with a horizontal padding of 5 pixels.
        remove_button = tk.Button(self, text="Remove Selected Borrower", command=self.remove_borrower, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to remove the selected borrower.
        remove_button.pack(pady=10) # This packs the remove borrower button with a vertical padding of 10 pixels.
        self.borrowers_data = load_borrowers_data() # This loads the borrower data.
        self.update_borrowers_listbox() # This calls the method to update the borrowers listbox with the loaded borrower data.
    def on_search_keyrelease(self, event): # This method is called when a key is released in the search entry field.
        self.update_borrowers_listbox() # This calls the method to update the borrowers listbox based on the search input.
    def update_borrowers_listbox(self): # This method updates the borrowers listbox with the filtered borrower data based on the search input.
        query = self.search_entry.get().strip().lower() # This gets the search query from the entry field and converts it to lowercase.
        self.borrowers_data = load_borrowers_data() # This reloads the borrower data.
        filtered = [b for b in self.borrowers_data if query in b.get("name", "").lower()] # This filters the borrower data based on the search query.
        filtered.sort(key=lambda b: b.get("name", "").lower()) # This sorts the filtered borrower data alphabetically by name.
        self.borrowers_listbox.delete(0, tk.END) # This clears the current contents of the borrowers listbox.
        for borrower in filtered: # This loops through each borrower in the filtered borrower data.
            self.borrowers_listbox.insert(tk.END, borrower.get("name", "Unknown")) # This inserts the borrower name into the borrowers listbox.
    def add_borrower(self): # This method adds a new borrower to the borrower data.
        new_name = self.add_entry.get().strip() # This gets the new borrower name from the entry field and strips any leading or trailing whitespace.
        if new_name: # This checks if the new borrower name is not empty.
            borrowers = load_borrowers_data() # This reloads the borrower data.
            borrowers.append({"name": new_name}) # This appends the new borrower to the borrower data.
            with open(BORROWERS_FILE, "w") as f: # This opens the borrowers file in write mode.
                json.dump(borrowers, f, indent=4) # This writes the updated borrower data to the file in JSON format with an indentation of 4 spaces.
            self.add_entry.delete(0, tk.END) # This clears the entry field for the new borrower name.
            self.update_borrowers_listbox() # This calls the method to update the borrowers listbox with the updated borrower data.
    def remove_borrower(self): # This method removes the selected borrower from the borrower data.
        selection = self.borrowers_listbox.curselection() # This gets the selected borrower from the borrowers listbox.
        if selection: # This checks if a borrower is selected.
            selected_name = self.borrowers_listbox.get(selection[0]) # This gets the name of the selected borrower.
            borrowers = load_borrowers_data() # This reloads the borrower data.
            borrowers = [b for b in borrowers if b.get("name", "") != selected_name] # This filters the borrower data to remove the selected borrower.
            with open(BORROWERS_FILE, "w") as f: # This opens the borrowers file in write mode.
                json.dump(borrowers, f, indent=4) # This writes the updated borrower data to the file in JSON format with an indentation of 4 spaces.
            self.update_borrowers_listbox() # This calls the method to update the borrowers listbox with the updated borrower data.
class LoansPage(LibraryPage): # This creates a class called "LoansPage" that inherits from the "LibraryPage" class to which utilizes Multi-Level Inheritance. This is the page for managing loans in the library.
    def __init__(self, parent, *args, **kwargs): # This is the constructor method for the "LoansPage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.create_header("Loans Management") # This creates a header label with the specified text.
        search_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the search section of the loans page.
        search_frame.pack(pady=10) # This packs the search frame with a vertical padding of 10 pixels.
        search_label = tk.Label(search_frame, text="Search Loans:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the search section.
        search_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the search frame with a left alignment and a horizontal padding of 5 pixels.
        self.search_entry = tk.Entry(search_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the search input.
        self.search_entry.pack(side=tk.LEFT) # This packs the entry field in the search frame.
        self.search_entry.bind("<KeyRelease>", self.on_search_keyrelease) # This binds the key release event to the search entry field to trigger the search function.
        self.loans_listbox = tk.Listbox(self, font=("Arial", APP_SETTINGS["font_size"]), width=60, height=10) # This creates a listbox to display the list of loans.
        self.loans_listbox.pack(pady=10) # This packs the listbox with a vertical padding of 10 pixels.
        add_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the add loan section.
        add_frame.pack(pady=5) # This packs the add loan frame with a vertical padding of 5 pixels.
        borrower_label = tk.Label(add_frame, text="Borrower:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the borrower section.
        borrower_label.pack(side=tk.LEFT, padx=(0, 5)) # This packs the label in the add loan frame with a left alignment and a horizontal padding of 5 pixels.
        self.borrower_entry = tk.Entry(add_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the borrower name.
        self.borrower_entry.pack(side=tk.LEFT) # This packs the entry field in the add loan frame.
        book_label = tk.Label(add_frame, text="Book:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the book section.
        book_label.pack(side=tk.LEFT, padx=(10, 5)) # This packs the label in the add loan frame with a left alignment and a horizontal padding of 5 pixels.
        self.book_entry = tk.Entry(add_frame, font=("Arial", APP_SETTINGS["font_size"])) # This creates an entry field for the book title.
        self.book_entry.pack(side=tk.LEFT) # This packs the entry field in the add loan frame.
        add_button = tk.Button(add_frame, text="Add Loan", command=self.add_loan, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to add a new loan.
        add_button.pack(side=tk.LEFT, padx=5) # This packs the add loan button in the add loan frame with a horizontal padding of 5 pixels.
        remove_button = tk.Button(self, text="Remove Selected Loan", command=self.remove_loan, font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to remove the selected loan.
        remove_button.pack(pady=10) # This packs the remove loan button with a vertical padding of 10 pixels.
        self.loans_data = load_loans_data() # This loads the loan data.
        self.update_loans_listbox() # This calls the method to update the loans listbox with the loaded loan data.
    def on_search_keyrelease(self, event): # This method is called when a key is released in the search entry field.
        self.update_loans_listbox() # This calls the method to update the loans listbox based on the search input.
    def update_loans_listbox(self): # This method updates the loans listbox with the filtered loan data based on the search input.
        query = self.search_entry.get().strip().lower() # This gets the search query from the entry field and converts it to lowercase.
        self.loans_data = load_loans_data() # This reloads the loan data.
        filtered = [loan for loan in self.loans_data if query in loan.get("borrower", "").lower() or query in loan.get("book", "").lower()] # This filters the loan data based on the search query.
        self.loans_listbox.delete(0, tk.END) # This clears the current contents of the loans listbox.
        for loan in filtered: # This loops through each loan in the filtered loan data.
            entry = f'{loan.get("borrower", "Unknown")} - {loan.get("book", "Untitled")}' # This creates a string representation of the loan with borrower and book title.
            self.loans_listbox.insert(tk.END, entry) # This inserts the loan entry into the loans listbox.
    def add_loan(self): # This method adds a new loan to the loan data.
        borrower = self.borrower_entry.get().strip() # This gets the borrower name from the entry field and strips any leading or trailing whitespace.
        book = self.book_entry.get().strip() # This gets the book title from the entry field and strips any leading or trailing whitespace.
        if borrower and book: # This checks if both borrower and book title are not empty.
            loans = load_loans_data() # This reloads the loan data.
            loans.append({"borrower": borrower, "book": book}) # This appends the new loan to the loan data.
            with open(LOANS_FILE, "w") as f: # This opens the loans file in write mode.
                json.dump(loans, f, indent=4) # This writes the updated loan data to the file in JSON format with an indentation of 4 spaces.
            self.borrower_entry.delete(0, tk.END) # This clears the entry field for the borrower name.
            self.book_entry.delete(0, tk.END) # This clears the entry field for the book title.
            self.update_loans_listbox() # This calls the method to update the loans listbox with the updated loan data.
    def remove_loan(self): # This method removes the selected loan from the loan data.
        selection = self.loans_listbox.curselection() # This gets the selected loan from the loans listbox.
        if selection: # This checks if a loan is selected.
            selected_entry = self.loans_listbox.get(selection[0]) # This gets the selected loan entry from the loans listbox.
            if " - " in selected_entry: # This checks if the selected entry contains " - " to separate borrower and book title.
                borrower, book = selected_entry.split(" - ", 1) # This splits the selected entry into borrower and book title.
                loans = load_loans_data() # This reloads the loan data.
                loans = [loan for loan in loans if not (loan.get("borrower", "") == borrower and loan.get("book", "") == book)] # This filters the loan data to remove the selected loan.
                with open(LOANS_FILE, "w") as f: # This opens the loans file in write mode.
                    json.dump(loans, f, indent=4) # This writes the updated loan data to the file in JSON format with an indentation of 4 spaces.
                self.update_loans_listbox() # This calls the method to update the loans listbox with the updated loan data.
class SettingsPage(LibraryPage): # This creates a class called "SettingsPage" that inherits from the "LibraryPage" class to which utilizes Multi-Level Inheritance. This is the page for managing settings in the library.
    def __init__(self, parent, update_callback, *args, **kwargs): # This is the constructor method for the "SettingsPage" class.
        super().__init__(parent, *args, **kwargs) # This calls the constructor of the parent class.
        self.update_callback = update_callback # This stores the update callback function passed from the main window.
        self.create_header("Settings") # This creates a header label with the specified text.
        self.settings = load_settings() # This loads the settings data.
        theme_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the theme section of the settings page.
        theme_frame.pack(pady=10) # This packs the theme frame with a vertical padding of 10 pixels.
        theme_label = tk.Label(theme_frame, text="Theme:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the theme section.
        theme_label.pack(side=tk.LEFT, padx=(0,5)) # This packs the label in the theme frame with a left alignment and a horizontal padding of 5 pixels.
        self.theme_var = tk.StringVar(value=self.settings.get("theme", "Light")) # This creates a StringVar to hold the selected theme value.
        theme_menu = tk.OptionMenu(theme_frame, self.theme_var, "Light", "Dark") # This creates an option menu for selecting the theme.
        theme_menu.config(font=("Arial", APP_SETTINGS["font_size"])) # This configures the font of the option menu.
        theme_menu.pack(side=tk.LEFT) # This packs the option menu in the theme frame.
        font_frame = tk.Frame(self, bg=self.get_bg_color()) # This creates a frame for the font size section of the settings page.
        font_frame.pack(pady=10) # This packs the font frame with a vertical padding of 10 pixels.
        font_label = tk.Label(font_frame, text="Font Size:", font=("Arial", APP_SETTINGS["font_size"]), bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a label for the font size section.
        font_label.pack(side=tk.LEFT, padx=(0,5)) # This packs the label in the font frame with a left alignment and a horizontal padding of 5 pixels.
        self.font_size_var = tk.IntVar(value=self.settings.get("font_size", 12)) # This creates an IntVar to hold the selected font size value.
        font_scale = tk.Scale(font_frame, from_=8, to=24, orient=tk.HORIZONTAL, variable=self.font_size_var, bg=self.get_bg_color(), fg=self.get_fg_color(), font=("Arial", APP_SETTINGS["font_size"])) # This creates a scale widget for selecting the font size.
        font_scale.pack(side=tk.LEFT) # This packs the scale widget in the font frame.
        save_button = tk.Button(self, text="Save Settings", font=("Arial", APP_SETTINGS["font_size"]), command=self.save_settings, bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to save the settings.
        save_button.pack(pady=10) # This packs the save settings button with a vertical padding of 10 pixels.
        defaults_button = tk.Button(self, text="Restore Defaults", font=("Arial", APP_SETTINGS["font_size"]), command=self.restore_defaults, bg=self.get_bg_color(), fg=self.get_fg_color()) # This creates a button to restore the default settings.
        defaults_button.pack(pady=5) # This packs the restore defaults button with a vertical padding of 5 pixels.
    def save_settings(self): # This method saves the current settings to the settings file.
        new_settings = { # This creates a dictionary to hold the new settings values.
            "theme": self.theme_var.get(), # This gets the selected theme value from the StringVar.
            "font_size": self.font_size_var.get() # This gets the selected font size value from the IntVar.
        } # This stores the new settings values in the dictionary.
        global APP_SETTINGS # This declares the APP_SETTINGS variable as global to modify it.
        APP_SETTINGS = new_settings # This updates the global APP_SETTINGS variable with the new settings values.
        save_settings_to_file(new_settings) # This calls the function to save the new settings to the settings file.
        self.update_callback() # This calls the update callback function to apply the new settings to all pages.
        self.update_style() # This calls the method to update the style of the settings page with the new settings.
    def restore_defaults(self): # This method restores the default settings.
        default_settings = {"theme": "Light", "font_size": 12} # This creates a dictionary with the default settings values.
        self.theme_var.set(default_settings["theme"]) # This sets the theme variable to the default theme value.
        self.font_size_var.set(default_settings["font_size"]) # This sets the font size variable to the default font size value.
        self.save_settings() # This calls the save settings method to save the default settings.
def create_window(): # This function creates the main window for the library management system.
    window = tk.Tk() # This creates a new Tkinter window.
    window.title("Library Management System") # This sets the title of the window.
    window.geometry("900x800") # This sets the size of the window to 900x800 pixels.
    window.resizable(False, False) # This makes the window non-resizable.
    container = tk.Frame(window) # This creates a frame to hold the pages of the application.
    container.place(x=0, y=50, relwidth=1, relheight=0.95) # This places the container frame at the top of the window with a height of 95% of the window.
    pages = {} # This dictionary will hold the different pages of the application.
    def update_all_styles(): # This function updates the styles of all pages in the application.
        for page in pages.values(): # This loops through all the pages in the pages dictionary.
            page.update_style() # This calls the update style method of each page to apply the new settings.
    for PageClass in (DashboardPage, BooksPage, BorrowersPage, LoansPage): # This loops through the classes for each page in the application.
        page_name = PageClass.__name__ # This gets the name of the page class.
        frame = PageClass(container) # This creates an instance of the page class and passes the container frame as the parent.
        pages[page_name] = frame # This adds the page instance to the pages dictionary with the page name as the key.
        frame.place(relx=0, rely=0, relwidth=1, relheight=1) # This places the page frame in the container with a width and height of 100%.
    settings_page = SettingsPage(container, update_callback=update_all_styles) # This creates an instance of the SettingsPage class and passes the container frame and update callback function as parameters.
    pages["SettingsPage"] = settings_page # This adds the settings page instance to the pages dictionary with the page name as the key.
    settings_page.place(relx=0, rely=0, relwidth=1, relheight=1) # This places the settings page frame in the container with a width and height of 100%.
    def show_page(page_name): # This function shows the specified page in the application.
        pages[page_name].tkraise() # This raises the specified page frame to the top of the stacking order.
    def open_dashboard(): # This function opens the dashboard page.
        show_page("DashboardPage") # This calls the show page function to display the dashboard page.
    def open_books(): # This function opens the books page.
        show_page("BooksPage") # This calls the show page function to display the books page.
    def open_borrowers(): # This function opens the borrowers page.
        show_page("BorrowersPage") # This calls the show page function to display the borrowers page.
    def open_loans(): # This function opens the loans page.
        show_page("LoansPage") # This calls the show page function to display the loans page.
    def open_settings(): # This function opens the settings page.
        show_page("SettingsPage") # This calls the show page function to display the settings page.
    def logout(): # This function logs out the user and closes the application.
        window.quit() # This calls the quit method of the window to close the application.
    menu_width = 200 # This sets the width of the menu frame.
    step = 20 # This sets the step size for the menu animation.
    delay = 10 # This sets the delay in milliseconds for the menu animation.
    menu_frame = tk.Frame(window, width=menu_width, height=800, bg="lightgray") # This creates a frame for the menu with the specified width and height.
    menu_frame.place(x=-menu_width, y=0) # This places the menu frame off-screen to the left.
    menu_visible = [False] # This list holds the visibility state of the menu.
    current_x = [-menu_width] # This list holds the current x position of the menu frame.
    def animate_menu_in(): # This function animates the menu frame sliding in from the left.
        x = current_x[0] # This gets the current x position of the menu frame.
        if x < 0: # This checks if the menu frame is not fully visible.
            x += step # This increments the x position by the step size.
            if x > 0: # This checks if the x position exceeds 0.
                x = 0 # This sets the x position to 0 to fully show the menu frame.
            current_x[0] = x # This updates the current x position of the menu frame.
            menu_frame.place(x=x, y=0) # This places the menu frame at the new x position.
            window.after(delay, animate_menu_in) # This calls the animate menu in function after the specified delay.
        else: # This checks if the menu frame is fully visible.
            menu_visible[0] = True # This sets the visibility state of the menu to True.
            menu_frame.lift() # This raises the menu frame to the top of the stacking order.
    def animate_menu_out(): # This function animates the menu frame sliding out to the left.
        x = current_x[0] # This gets the current x position of the menu frame.
        if x > -menu_width: # This checks if the menu frame is not fully hidden.
            x -= step # This decrements the x position by the step size.
            if x < -menu_width: # This checks if the x position goes below -menu width.
                x = -menu_width # This sets the x position to -menu width to fully hide the menu frame.
            current_x[0] = x # This updates the current x position of the menu frame.
            menu_frame.place(x=x, y=0) # This places the menu frame at the new x position.
            window.after(delay, animate_menu_out) # This calls the animate menu out function after the specified delay.
        else: # This checks if the menu frame is fully hidden.
            menu_visible[0] = False # This sets the visibility state of the menu to False.
    def toggle_menu(): # This function toggles the visibility of the menu frame.
        if not menu_visible[0]: # This checks if the menu is not visible.
            animate_menu_in() # This calls the animate menu in function to show the menu.
        else: # This checks if the menu is visible.
            animate_menu_out() # This calls the animate menu out function to hide the menu.
    def is_descendant(child, parent): # This function checks if the child widget is a descendant of the parent widget.
        while child: # This loops through the parent hierarchy of the child widget.
            if child == parent: # This checks if the child widget is the same as the parent widget.
                return True # This returns True if the child widget is a descendant of the parent widget.
            child = child.master # This sets the child widget to its parent widget.
        return False # This returns False if the child widget is not a descendant of the parent widget.
    def close_menu_if_click_outside(event): # This function closes the menu if a click event occurs outside the menu frame.
        if menu_visible[0]: # This checks if the menu is visible.
            if is_descendant(event.widget, menu_frame) or is_descendant(event.widget, hamburger_btn): # This checks if the clicked widget is a descendant of the menu frame or the hamburger button.
                return # This returns if the clicked widget is inside the menu frame or the hamburger button.
            toggle_menu() # This calls the toggle menu function to hide the menu.
    btn_dashboard = tk.Button(menu_frame, text="Dashboard", command=lambda: [open_dashboard(), toggle_menu()], font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for the dashboard page.
    btn_dashboard.pack(pady=10, fill="x", padx=10) # This packs the dashboard button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    btn_books = tk.Button(menu_frame, text="Books", command=lambda: [open_books(), toggle_menu()], font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for the books page.
    btn_books.pack(pady=10, fill="x", padx=10) # This packs the books button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    btn_borrowers = tk.Button(menu_frame, text="Borrowers", command=lambda: [open_borrowers(), toggle_menu()], font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for the borrowers page.
    btn_borrowers.pack(pady=10, fill="x", padx=10) # This packs the borrowers button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    btn_loans = tk.Button(menu_frame, text="Loans", command=lambda: [open_loans(), toggle_menu()], font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for the loans page.
    btn_loans.pack(pady=10, fill="x", padx=10) # This packs the loans button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    btn_settings = tk.Button(menu_frame, text="Settings", command=lambda: [open_settings(), toggle_menu()], font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for the settings page.
    btn_settings.pack(pady=10, fill="x", padx=10) # This packs the settings button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    btn_logout = tk.Button(menu_frame, text="Logout", command=logout, font=("Arial", APP_SETTINGS["font_size"]), bg="white", bd=2, relief="solid") # This creates a button for logging out.
    btn_logout.pack(pady=10, fill="x", padx=10) # This packs the logout button in the menu frame with a vertical padding of 10 pixels and fills the width of the frame.
    hamburger_btn = tk.Button(window, text="☰", font=("Arial", APP_SETTINGS["font_size"]), command=toggle_menu) # This creates a button for the hamburger menu icon.
    hamburger_btn.place(x=10, y=10) # This places the hamburger button at the top left corner of the window.
    window.bind("<Button-1>", close_menu_if_click_outside) # This binds the left mouse button click event to the close menu if click outside function.
    show_page("DashboardPage") # This calls the show page function to display the dashboard page.
    window.mainloop() # This starts the main event loop of the Tkinter application.
if __name__ == "__main__": # This checks if the script is being run directly.
    APP_SETTINGS.update(load_settings()) # This updates the APP_SETTINGS dictionary with the loaded settings from the settings file.
    create_window() # This calls the create window function to start the application.
