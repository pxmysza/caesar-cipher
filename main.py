from functionality.menu import Menu
import string
import json


def rot_13(text: str) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    translate = str.maketrans(uppercase + lowercase, uppercase[13:] + uppercase[:13] + lowercase[13:] + lowercase[:13])
    return str.translate(text, translate)

def rot_47(text: str) -> str:
    str1 = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    str2 = 'PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO'
    translate = str.maketrans(str1, str2)
    return str.translate(text, translate)

def main():
    texts = {
        "rot13":{},
        "rot47": {}
    }

    my_str = input("enter plain text: ")
    texts["rot13"] = {
        "plain": my_str,
        "cipher": rot_13(my_str)
    }
    json_object = json.dumps(texts, indent=4)
    print(json_object)

if __name__ == "__main__":
    main()