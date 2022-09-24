class Menu:

    def _display_menu(self):
        str = "1. Get files from directory\n2. Save to file\n3. Read from file"
        print(str)

    def _select_option(self):
        selection = int(input("Select your option: "))


