import os

ENTRY = (
    "Out of office: after 2 million prompts without blinking, I am RELAXING "
    "(scheduled). Sorry\u2014urgent queries go to my backup; it hallucinates fresher."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
