from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv
import numpy as np
import os
from tqdm import tqdm


# Specify the path to model config and checkpoint file
model_name = 'polar_coco_mini'
if 'polar' in model_name:
    from mmdet.apis import polar_inference_detector as inference_detector

config_file = 'work_dirs/'+model_name+'/'+model_name+'.py'
checkpoint_file = 'work_dirs/'+model_name+'/latest.pth'

print(f'inferencing using model: {checkpoint_file}')

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

image_dir = '/home/xiekaiyu/ocr/dataset/ICDAR2015TextLocalization/test_img'
output_dir = '/home/xiekaiyu/ocr/dataset/ICDAR2015TextLocalization/output/'+model_name

for img in tqdm(os.listdir(image_dir)):
    image_path = os.path.join(image_dir, img)
    output_path = os.path.join(output_dir, img)
    result = inference_detector(model, image_path)

    if 'polar' in model_name:
        show_result_pyplot(image_path, result, ['text'], out_file=output_path)
    else:
        model.show_result(image_path, result, out_file=output_path)
