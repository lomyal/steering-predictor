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
import numpy as np


class IO(object):

    def __init__(self, file_name):
        self.training_image_path = '/media/blade/road_hackers/training_images/'
        self.training_attribute_path = '/media/blade/road_hackers/training_attribute/'
        self.file_name = file_name
        self.training_images = self.read_image_file(self.file_name)
        self.training_attribute = self.read_attribute_file(self.file_name)

        self.returned_batch_count = 0
        self.training_attribute_count = 0

        # self._pre_process_data()

    def read_image_file(self, file_name):
        return h5py.File(self.training_image_path + file_name, 'r')

    def read_attribute_file(self, file_name):
        attribute_object = h5py.File(self.training_attribute_path + file_name, 'r')
        return attribute_object['attrs']

    def next_batch(self, batch_size):
        """
        返回下一块数据
        :param batch_size:
        :return:
        """
        images = np.ndarray(shape=(batch_size, 320, 320, 3,))
        labels = np.ndarray(shape=(batch_size, 1,))
        data_count = 0
        while data_count < batch_size:
            label_data = self.training_attribute[self.training_attribute_count]
            utc_time = "{0:.3f}".format(label_data[0])
            if utc_time in self.training_images:
                images[data_count] = self.training_images[utc_time]
                labels[data_count] = label_data[1]
                data_count += 1
                self.returned_batch_count += 1
        return [images, labels]

    # def _pre_process_data(self):
    #     """
    #     将原始数据组装成
    #     :return:
    #     """
    #     pass
