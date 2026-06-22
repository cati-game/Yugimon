import os
import json

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".gif")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def scan(folder_name):
    folder_path = os.path.join(BASE_DIR, folder_name)

    cards = []

    if not os.path.exists(folder_path):
        print("Missing:", folder_path)
        return cards

    for file in os.listdir(folder_path):
        if file.lower().endswith(IMAGE_EXTS):
            cards.append(folder_name + "/" + file)  # store relative path

    return cards


def main():
    data = {
        "main": scan("Main"),
        "extra": scan("Extra")
    }

    with open("cards.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Exported:")
    print("Main:", len(data["main"]))
    print("Extra:", len(data["extra"]))


if __name__ == "__main__":
    main()