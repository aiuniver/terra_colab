import requests

from argparse import ArgumentParser
from google.colab import drive


def auth():
    parser = ArgumentParser()
    parser.add_argument("--email", type=str)
    parser.add_argument("--token", type=str)
    parser.add_argument("--url", type=str)
    args = parser.parse_args()

    response = requests.post(
        args.url, json={"email": args.email, "user_token": args.token}
    )
    if not response.ok:
        print("Ошибка запроса авторизации! Попробуйте позже...")
        return

    data = response.json()

    if not data.get("success"):
        print(data.get("error"))
        return

    files = data.get("data").get("create")
    for name, info in files.items():
        with open(info.get("name"), "w") as file:
            file.write(info.get("data"))

    with open("/content/terra_gui/.terra-gui.env", "a") as file:
        file.write(f'TERRA_GUI_URL={data.get("data").get("url")}\n')


def gdmount():
    drive.mount("/content/drive")
