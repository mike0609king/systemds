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
# Autogenerated From : scripts/builtin/sherlockPredict.dml

from typing import Dict, Iterable

from systemds.operator import OperationNode, Matrix, Frame, List, MultiReturn, Scalar
from systemds.utils.consts import VALID_INPUT_TYPES


def sherlockPredict(X: Matrix,
                    cW1: Matrix,
                    cb1: Matrix,
                    cW2: Matrix,
                    cb2: Matrix,
                    cW3: Matrix,
                    cb3: Matrix,
                    wW1: Matrix,
                    wb1: Matrix,
                    wW2: Matrix,
                    wb2: Matrix,
                    wW3: Matrix,
                    wb3: Matrix,
                    pW1: Matrix,
                    pb1: Matrix,
                    pW2: Matrix,
                    pb2: Matrix,
                    pW3: Matrix,
                    pb3: Matrix,
                    sW1: Matrix,
                    sb1: Matrix,
                    sW2: Matrix,
                    sb2: Matrix,
                    sW3: Matrix,
                    sb3: Matrix,
                    fW1: Matrix,
                    fb1: Matrix,
                    fW2: Matrix,
                    fb2: Matrix,
                    fW3: Matrix,
                    fb3: Matrix):
    """
     This function implements prediction and evaluation phase of Sherlock:
     Split feature matrix into four different feature categories and predicting the class probability
     on the respective features. Then combine all predictions for final predicted probabilities.
     A Deep Learning Approach to Semantic Data Type Detection.
     [Hulsebos, Madelon, et al. "Sherlock: A deep learning approach to semantic data type detection."
     Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining.
     2019.]
    
    
    
    :param X: matrix of values which are to be classified
    :param cW: weights (parameters) matrices for character distribtions
    :param cb: biases vectors for character distribtions
    :param wW: weights (parameters) matrices for word embeddings
    :param wb: biases vectors for word embeddings
    :param pW: weights (parameters) matrices for paragraph vectors
    :param pb: biases vectors for paragraph vectors
    :param sW: weights (parameters) matrices for global statistics
    :param sb: biases vectors for global statistics
    :param fW: weights (parameters) matrices for  combining all trained features (final)
    :param fb: biases vectors for combining all trained features (final)
    :return: class probabilities of shape (N, K)
    """

    params_dict = {'X': X, 'cW1': cW1, 'cb1': cb1, 'cW2': cW2, 'cb2': cb2, 'cW3': cW3, 'cb3': cb3, 'wW1': wW1, 'wb1': wb1, 'wW2': wW2, 'wb2': wb2, 'wW3': wW3, 'wb3': wb3, 'pW1': pW1, 'pb1': pb1, 'pW2': pW2, 'pb2': pb2, 'pW3': pW3, 'pb3': pb3, 'sW1': sW1, 'sb1': sb1, 'sW2': sW2, 'sb2': sb2, 'sW3': sW3, 'sb3': sb3, 'fW1': fW1, 'fb1': fb1, 'fW2': fW2, 'fb2': fb2, 'fW3': fW3, 'fb3': fb3}
    return Matrix(X.sds_context,
        'sherlockPredict',
        named_input_nodes=params_dict)
