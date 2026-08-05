import asyncio
from daily_bits.wiki import get_random_article


def main():
    title, text = asyncio.run(get_random_article())
    print(title)
    print()
    print(text)


if __name__ == "__main__":
    main()
