# Deep Sort 

This is the implemention of deep sort with pytorch.


The DeepSort checkblock repository can be used via a config file.
Config file example:
cfg.deepsort:
    model_path: ./weights/ckpt.t7
    max_dist: 0.2
    min_confidence: 0.3
    nms_max_overlap: 0.5
    max_iou_distance: 0.7
    max_age: 70
    n_init: 3
    nn_budget: 100
    use_cuda: True

from deep_sort_pytorch.deep_sort import DeepSort
deep_sort_tracker = DeepSort(cfg.deepsort, hydra.utils.get_original_cwd())

Adjusted 