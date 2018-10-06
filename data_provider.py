# -*- coding: utf-8 -*-

"""
Data Provider

DPED Dataset see:http://people.ee.ethz.ch/~ihnatova/

"""
import os
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset


to_tensor = transforms.Compose([
    transforms.ToTensor()
])


class DPEDDataset(Dataset):

    def __init__(self, data_dir, phone='iphone'):

        self.phone_dir = os.path.join(data_dir, phone)
        self.camera = os.path.join(data_dir, 'canon')

        self.image_names = os.listdir(self.phone_dir)

    def __len__(self):
        return len(self.image_names)

    def __getitem__(self, idx):

        img_name = self.image_names[idx]
        phone_image = Image.open(os.path.join(self.phone_dir, img_name))
        camera_image = Image.open(os.path.join(self.camera, img_name))

        phone_image = to_tensor(phone_image)/255.0
        camera_image = to_tensor(camera_image)/255.0

        return phone_image, camera_image

