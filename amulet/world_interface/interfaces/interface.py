from __future__ import annotations

from typing import Tuple, Any

import numpy

from ...api.block import BlockManager
from ...api.chunk import Chunk


class Interface:
    def decode(self, data: Any) -> Tuple[Chunk, numpy.ndarray]:
        """
        Create an amulet.api.chunk.Chunk object from raw data given by the format.

        :param data: Raw chunk data provided by the format.
        :return: Chunk object that matches the data, along with the palette for that chunk.
        """
        raise NotImplementedError()

    def encode(self, chunk: Chunk, palette: BlockManager):
        """
        Create raw data for the format to store given a translated chunk.

        :param chunk: The version-specific chunk to encode.
        :param palette: The palette the ids in the chunk correspond to.
        :return: Raw data to be stored by the format.
        """
        raise NotImplementedError()

    def get_translator(self, data: Any) -> Tuple:
        """
        Return the translator key given chunk coordinates.

        :param data: The data passed in to translate.
        :return: The translator key for the identify method.
        """
        raise NotImplementedError()

    @staticmethod
    def is_valid(key: Tuple) -> bool:
        """
        Returns whether this interface is able to interface with the chunk type with a given identifier key,
        generated by the format.

        :param key: The key who's decodability needs to be checked.
        :return: True if this interface can interface with the chunk version associated with the key, False otherwise.
        """
        raise NotImplementedError()
