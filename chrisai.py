import torch
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import cv2
import pyautogui

model = torch.hub.load('yolov5', 'yolov5s', source='local')

img = 'https://ultralytics.com/images/zidane.jpg'

results = model(img)
results.print()

plt.imshow(np.squeeze(results.render()))
plt.show()
