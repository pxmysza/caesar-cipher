class Menu:
    @staticmethod
    def display_menu():
        """Static method that displays menu items only"""
        menu_str = "#################\n" \
                   "1. Display all files from directory\n" \
                   "2. Add text to buffer\n" \
                   "3. Save buffer to file\n" \
                   "4. Read file content\n" \
                   "5. Display buffer\n" \
                   "6. Clear buffer\n" \
                   "7. Load text from file to buffer\n" \
                   "8. Display decrypted file content\n" \
                   "9. Display encrypted/decrypted buffer\n" \
                   "99. Quit\n" \
                   "#################"
        print(menu_str)
