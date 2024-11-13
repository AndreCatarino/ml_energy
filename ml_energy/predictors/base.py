from abc import ABC, abstractmethod
from typing import List, Union

import torch
import torch.utils


class PrecictorBase(ABC):
    """
    Some cool example for Andre

    Attributes
    ----------
    None
    """

    @abstractmethod
    def __init__(self):
        """
        Raises
        ------
        NotImplementedError
            If the subclass does not implement this method.
        """
        raise NotImplementedError

    @classmethod
    def __str__(cls):
        """
        This method provides the class name as a string when the class is printed.

        Returns
        -------
        str
            The name of the class.
        """
        return cls.__name__

