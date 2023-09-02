"""
main
"""
from __future__ import annotations

import asyncio


async def main() -> None:
    """
    main
    """
    # prefix_directory: Path = Path(__file__).parent.parent
    # data_directory: Path = prefix_directory / "data"
    try:
        chaoter01()

    except KeyboardInterrupt:
        exit(1)
    except TypeError as error:
        print(error.args[0])
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
