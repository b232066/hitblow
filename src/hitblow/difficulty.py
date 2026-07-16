"""難易度選択：遊ぶ前に桁数を選んでもらう。"""


def select_digits(default=3, min_digits=3, max_digits=6):
    ans = input(f"桁数を選んでね（{min_digits}〜{max_digits}、Enterで{default}）> ").strip()
    if ans.isdigit() and min_digits <= int(ans) <= max_digits:
        return int(ans)
    print(f"デフォルトの{default}桁で始めます。")
    return default
