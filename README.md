# Deep Sort with PyTorch

![](Town.gif)

## Introduction

This repository is the checkblock for the deepsort algorithm with pytorch integration.
Deep Sort algorithm (https://github.com/ZQPei/deep_sort_pytorch) which tracks persons.

## Description

The implementation is based on two papers:

- Simple Online and Realtime Tracking with a Deep Association Metric
https://arxiv.org/abs/1703.07402

## Requirements

Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7. To install run:

`pip install -U -r requirements.txt`
pip install checkblock_deepsort@testdata.git

- download the deep sort weights from https://drive.google.com/drive/folders/1xhG0kRH1EX5B9_Iz8gQJb7UNnn_riXi6. Place ckpt.t7 file under`deep_sort/deep/checkpoint/`
