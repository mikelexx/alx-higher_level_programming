#!/usr/bin/python3
"""
This modules contains a function that does \
matrix multiplication with help of numpy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices and returns the answer.
    Args:
        m_a (int, float): first matrix
        m_b (int, float): second matrix
    Returns:
            m_a x m_b
    """
    return np.matmul(m_a, m_b)
