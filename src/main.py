"""
main
"""
from __future__ import annotations

import asyncio

from src.modules.chapter01.chapter01 import chapter01


async def main() -> None:
    """
    main
    """
    # prefix_directory: Path = Path(__file__).parent.parent
    # data_directory: Path = prefix_directory / "data"
    try:
        chapter01()

    except KeyboardInterrupt:
        exit(1)
    except TypeError as error:
        print(error.args[0])
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
