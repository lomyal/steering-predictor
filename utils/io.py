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


def read_image_file(file_name, file_path='/media/blade/road_hackers/training_images/'):
    return h5py.File(file_path + file_name, 'r')


def read_attribute_file(file_name, file_path='/media/blade/road_hackers/training_attribute/'):
    attribute_object = h5py.File(file_path + file_name, 'r')
    return attribute_object['attrs']
