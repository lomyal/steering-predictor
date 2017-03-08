#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#
# Copyright (c) 2016 All Rights Reserved
#
################################################################################
"""
IO functions

Authors: Wang Shijun
Date:  2017/03/01 22:39:00
"""

import h5py


def read_image_file(file_path):
    return h5py.File(file_path, 'r')


def read_attribute_file(file_path):
    attribute_object = h5py.File(file_path, 'r')
    return attribute_object['attrs']