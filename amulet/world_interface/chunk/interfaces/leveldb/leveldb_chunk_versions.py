from typing import Tuple

# this is a dictionary of the first and last times each chunk version was written by a game version
chunk_version_to_max_version = {
    0: ((0, 9, 0, 0), (0, 9, 1, 9999)),
    1: ((0, 9, 2, 0), (0, 9, 4, 9999)),
    2: ((0, 9, 5, 0), (0, 16, 999, 9999)),
    3: ((0, 17, 0, 0), (0, 17, 999, 9999)),
    4: ((0, 18, 0, 0), (0, 18, 0, 0)),
    5: ((0, 18, 0, 0), (1, 1, 999, 9999)),
    6: ((1, 2, 0, 0), (1, 2, 0, 0)),
    7: ((1, 2, 0, 0), (1, 2, 999, 9999)),
    8: ((1, 3, 0, 0), (1, 7, 999, 9999)),
    9: ((1, 8, 0, 0), (1, 8, 999, 9999)),
    10: ((1, 9, 0, 0), (1, 9, 999, 9999)),
    11: ((1, 10, 0, 0), (1, 10, 999, 9999)),
    12: ((1, 11, 0, 0), (1, 11, 0, 9999)),
    13: ((1, 11, 1, 0), (1, 11, 1, 9999)),
    14: ((1, 11, 2, 0), (1, 11, 999, 999)),
    15: ((1, 12, 0, 0), (999, 999, 999, 9999)),
    # 15: ((1, 12, 0, 0), (1, 13, 999, 999)),
    # 16: ((1, 14, 0, 0), (999, 999, 999, 9999)),  # this was apparently going to be added in 1.14 but I can't find it
}  # TODO: fill this list with the actual last game version number each chunk version was last used in


def chunk_to_game_version(
    max_game_version: Tuple[int, int, int], chunk_version: int
) -> Tuple[int, int, int]:
    return min(chunk_version_to_max_version[chunk_version][1], max_game_version)


def game_to_chunk_version(max_game_version: Tuple[int, int, int]) -> int:
    for chunk_version, (first, last) in chunk_version_to_max_version.items():
        if first <= max_game_version <= last:
            return chunk_version
