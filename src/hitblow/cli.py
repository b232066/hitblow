"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

from unittest import result

from .game import play


def main():
    """
    Hit & Blow の開始地点。

    play() が返した値によって
    リスタートか終了かを決定する。
    """

    while True:

        result = play()

        # -------------------------------
        # play()からrestartが返れば
        # ゲーム途中でrが押された
        # -------------------------------
        if result == "restart":
            print("新しいゲームを開始します。\n")
            continue

        # -------------------------------
        # ゲームをクリア、またはリタイアした
        # -------------------------------
        if result == "clear":
            print("ゲームクリア！")

        if result == "quit":
            print("ゲームをリタイアしました。")

        # -------------------------------
        # もう一度遊ぶか確認
        # -------------------------------    
        again = input(
            "\nrで新しいゲーム\n"
            "Enterで終了\n> "
        ).strip().lower()

        if again == "r":
            continue

        print("ゲームを終了します。")
        break

