# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

# Autogenerated By   : src/main/python/generator/generator.py
# Autogenerated From : scripts/builtin/img_transform_linearized.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.utils.consts import VALID_INPUT_TYPES


def img_transform_linearized(img_in: Matrix,
                             out_w: int,
                             out_h: int,
                             a: float,
                             b: float,
                             c: float,
                             d: float,
                             e: float,
                             f: float,
                             fill_value: float,
                             s_cols: int,
                             s_rows: int):
    """
     The Linearized Image Transform function applies an affine transformation to linearized images.
     Optionally resizes the image (without scaling).
     Uses nearest neighbor sampling.
    
    
    
    :param img_in: Linearized input images as 2D matrix with top left corner at [1, 1]
    :param out_w: Width of the output matrix
    :param out_h: Height of the output matrix
    :param a,b,c,d,e,f: The first two rows of the affine matrix in row-major order
    :param fill_value: The background of an image
    :return: Output images in linearized form as 2D matrix with top left corner at [1, 1]
    """

    params_dict = {'img_in': img_in, 'out_w': out_w, 'out_h': out_h, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'fill_value': fill_value, 's_cols': s_cols, 's_rows': s_rows}
    return Matrix(img_in.sds_context,
        'img_transform_linearized',
        named_input_nodes=params_dict)
