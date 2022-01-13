import os


def sandwich_or_bust(bread: str) -> str:
    jam = os.getenv("JAM")
    if not jam:
        raise ValueError("There is no jam. Sad bread.")
    return bread + str(jam) + bread


s = sandwich_or_bust("\U0001F35E")
print(s)
