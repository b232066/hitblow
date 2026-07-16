"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

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
        # play()からFalseが返れば
        # ゲーム途中でrが押された
        # -------------------------------
        if result is False:

            print("新しいゲームを開始します。\n")

            continue

        # -------------------------------
        # 正常終了
        # -------------------------------
        restart = input(
            "\nrで新しいゲーム\n"
            "Enterで終了\n> "
        ).strip().lower()

        if restart != "r":

            print("ゲームを終了します。")

            break