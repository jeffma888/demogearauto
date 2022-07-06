''' Example client sending POST request to server (localhost:8000/detect/)and printing the YOLO results

The send_request() function has a couple options demonstrating all the ways you can interact 
with the /detect endpoint
'''

import cv2
import numpy as np


import torch


import json
from pprint import pprint

import base64
from io import BytesIO
from PIL import Image
import streamlit as st
from pathlib import Path
import os
import sys
import argparse



FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative




def send_request(file_list):

	#upload multiple files as list of tuples
	st.json({'detection': "Oring"})
	a =st.json({'detection': "Oring"})
	return a






	json_data = json_results.json()

	for img_data in json_data:
		for bbox_data in img_data:
				#parse json to detect if the dict contains image data (base64) or bbox data
			if 'image_base64' in bbox_data.keys():
					#decode and show base64 encoded image
				img = Image.open(BytesIO(base64.b64decode(str(bbox_data['image_base64']))))
				img.show()
			else:
					#otherwise print json bbox data
				pprint(bbox_data)

	else:
		#if no images were downloaded, just display json response
		pprint(json.loads(json_results.text))
		st.json(json.loads(json_results.text))




if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--weights', nargs='+', type=str, default=ROOT / 'last.pt', help='model path(s)')
	parser.add_argument('--source', type=str, default=ROOT / 'test1.png', help='file/dir/URL/glob, 0 for webcam')
	# parser.add_argument('--data', type=str, default=ROOT / 'data/coco128.yaml', help='(optional) dataset.yaml path')
	parser.add_argument('--imgsz', '--img', '--img-size', nargs='+', type=int, default=[640], help='inference size h,w')
	parser.add_argument('--conf-thres', type=float, default=0.25, help='confidence threshold')
	parser.add_argument('--iou-thres', type=float, default=0.45, help='NMS IoU threshold')
	parser.add_argument('--max-det', type=int, default=1000, help='maximum detections per image')
	parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
	parser.add_argument('--view-img', action='store_true', help='show results')
	parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
	parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
	parser.add_argument('--save-crop', action='store_true', help='save cropped prediction boxes')
	parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
	parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --classes 0, or --classes 0 2 3')
	parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
	parser.add_argument('--augment', action='store_true', help='augmented inference')
	parser.add_argument('--visualize', action='store_true', help='visualize features')
	parser.add_argument('--update', action='store_true', help='update all models')
	parser.add_argument('--project', default=ROOT / 'runs/detect', help='save results to project/name')
	parser.add_argument('--name', default='exp', help='save results to project/name')
	parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
	parser.add_argument('--line-thickness', default=3, type=int, help='bounding box thickness (pixels)')
	parser.add_argument('--hide-labels', default=False, action='store_true', help='hide labels')
	parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
	parser.add_argument('--half', action='store_true', help='use FP16 half-precision inference')
	parser.add_argument('--dnn', action='store_true', help='use OpenCV DNN for ONNX inference')
	opt = parser.parse_args(args=[])
	opt.imgsz *= 2 if len(opt.imgsz) == 1 else 1  # expand
	# print_args(FILE.stem, opt)
	print(opt)

	st.write("AI")
	UploadFile = st.file_uploader("update pic")
	with st.spinner(text='AI识别中...'):
		st.image(UploadFile)
		picture = Image.open(UploadFile)
		picture = picture.save(f'data/images/{UploadFile.name}')
		opt.source = f'data/images/{UploadFile.name}'
		st.write(type(opt.source))
		st.write(opt.source)
		file_list =[opt.source]
		st.write(file_list)

		a = send_request(file_list=file_list)

			#img_str = base64.b64encode(f.read())
			#st.write(type(img_str))


	#example uploading image and receiving bbox json + image with bboxes drawn
	#send_request(file_list=['./images/zidane.jpg'], download_image = True)
