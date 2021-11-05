# Copyright 2021 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Type hints for common dimod inputs.
"""

from typing import Collection, Hashable, Tuple, Union

import numpy as np

from dimod.vartypes import VartypeLike

__all__ = ['Bias',
           'GraphLike',
           'Variable',
           'VartypeLike',
           ]


Variable = Hashable  # todo: exclude None
Bias = Union[int, float, np.number]

# todo: SamplesLike

try:
    import networkx as nx
except ImportError:
    GraphLike = Union[
        int,  # number of nodes
        Tuple[Collection[Variable], Collection[Tuple[Variable, Variable]]],  # nodes/edges
        Collection[Tuple[Variable, Variable]],  # edges
        ]
else:
    GraphLike = Union[
        int,  # number of nodes
        Tuple[Collection[Variable], Collection[Tuple[Variable, Variable]]],  # nodes/edges
        Collection[Tuple[Variable, Variable]],  # edges
        nx.Graph,
        ]
