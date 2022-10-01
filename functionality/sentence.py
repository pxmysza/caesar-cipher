from typing import Optional

class Sentence:
    def __init__(self, cipher_type: str, text: str, status: Optional[str] = "decrypted"):
        self.cipher_type = cipher_type
        self.text = text
        self.status = status

    def __str__(self):
        return f"Cipher type: {self.cipher_type}, text: {self.text}, status: {self.status}"

