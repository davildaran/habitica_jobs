import yagmail


receiver = "davildaran@gmail.com"
body = "do you have issues committing to things?"
attachment = ""


def send_email():
    yag = yagmail.SMTP("davildaran@gmail.com")
    yag.send(
        to=receiver,
        subject="habitica jobs commit",
        contents=body,
    )


if __name__ == "__main__":
    send_email()
