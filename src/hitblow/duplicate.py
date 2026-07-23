"""重複あり/なしを選べる機能。"""
import random


def ask_allow_duplicates(default=False) -> bool:
    ans = input("数字の重複を許可しますか？(y/n、Enterでなし) > ").strip().lower()
    return ans in ("y", "yes")


def make_secret_with_duplicates(digits: int) -> str:
    return "".join(random.choices("0123456789", k=digits))