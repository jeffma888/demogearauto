''' Example client sending POST request to server (localhost:8000/detect/)and printing the YOLO results

The send_request() function has a couple options demonstrating all the ways you can interact 
with the /detect endpoint
'''

import requests as r
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

def send_request(file_list = ['./images/zidane.jpg'],
					model_name = 'last',
					img_size = 640,
					download_image = False):

	#upload multiple files as list of tuples
	files = [('file_list', open(file,"rb")) for file in file_list]

	#pass the other form data here
	other_form_data = {'model_name': model_name,
					'img_size': img_size,
					'download_image': download_image}

	res = r.post("http://localhost:8000/detect/",
					data = other_form_data, 
					files = files)

	if download_image:
		json_data = res.json()

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
		pprint(json.loads(res.text))
		st.json(json.loads(res.text))




if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--weights', nargs='+', type=str,
						default=ROOT / 'weights/last.pt', help='model.pt path(s)')
	# parser.add_argument('--source', type=str,
	# default='data/images', help='source')
	parser.add_argument('--img-size', type=int, default=640,
						help='inference size (pixels)')

	opt = parser.parse_args(args=[])


	#example uploading image batch
	#send_request(file_list=['./images/bus.jpg','./images/zidane.jpg'])
	st.write("AI")
	UploadFile = st.file_uploader("update pic")
	with st.spinner(text='AI识别中...'):
		st.sidebar.image(UploadFile)
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
