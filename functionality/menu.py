class Menu:
    def _display_menu(self):
        str = "1. Read from file\n2. Save to file\n3. Read from file"
        print(str)

    def _select_option(self):
        selection = int(input())

