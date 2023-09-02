import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    byte = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

    if re.search(f"^{byte}\.{byte}\.{byte}\.{byte}$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()