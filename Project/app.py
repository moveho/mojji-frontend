from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, session, g
from flask_session import Session ##
from werkzeug.utils import secure_filename
from datetime import datetime
from urllib.parse import urljoin

import os
import flask
import boto3
import csv
import glob
import urllib.parse

from m_config import S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, S3_BUCKET_REGION
import pymysql

app = Flask(__name__, template_folder='template')

##
# 세션 설정
# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)
##

@app.route('/mojji')
def home():
    return render_template('index_mojji.html')

# @app.route('/user_check')
# def user_check():
    # code = request.args.get('code', '')
    # image_url = request.args.get('image_url', '')
    # directory_name_split = request.args.get('directory_name_split', '')
    # oauth_code = request.args.get('oauth_code', '')

#     # Generate the dropdown options for the selected directory
#     dropdown_options = generate_dropdown_options(directory_name_split)

#     return render_template('page5.html', code=code, image_url=image_url, directory_name_split=directory_name_split, oauth_code=oauth_code, dropdown_options=dropdown_options)

# def find_directory_with_prefix(directory_path, prefix):
#     for dir_name in os.listdir(directory_path):
#         # Check if the directory name starts with the given prefix
#         if dir_name.startswith(prefix):
#             return dir_name
#     return None


# def find_directory_with_prefix(directory_path, prefix):
#     for dir_name in os.listdir(directory_path):
#         # Check if the directory name starts with the given prefix
#         if dir_name.startswith(prefix):
#             return dir_name
#     return None

# S3 client creation
# s3 = boto3.client(
#     service_name="s3",
#     region_name=S3_BUCKET_REGION,
#     aws_access_key_id=S3_ACCESS_KEY,
#     aws_secret_access_key=S3_SECRET_ACCESS_KEY
# )

# def find_directory_with_prefix(bucket_name, prefix):
#     response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
#     for common_prefix in response.get('CommonPrefixes', []):
#         directory_path = common_prefix['Prefix']
#         return directory_path
#     return None

# @app.route('/user_check', methods=['GET'])
# def user_check():
#     # Get the value of identifier from the query parameters
#     identifier = request.args.get('identifier', '')
#     oauth_code = request.args.get('oauth_code', '')
#     directory_name_split = request.args.get('directory_name_split', '')
#     image_code = request.args.get('code', '')
#     file_names = request.args.get('file_names', '')
    
#     prefix = 'after_detection_'

#     # Define the base directory path
#     # base_directory = '/home/ubuntu/environment/efs/mojji-output-img/'
    
#     directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)

#     if directory_with_prefix is None:
#         # If the directory with the prefix is not found, handle the error
#         return "Directory with prefix '{}' not found.".format(prefix)

#     # Construct the full identifier with the directory name
#     full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)

#     # full_identifier = os.path.join(base_directory, directory_name_split)

#     object_names = []  # List to store the object names
    
#     # Iterate over the files in the directory
#     for file_name in os.listdir(full_identifier):
#         object_names.append(file_name)
        
#     # You can use the code to generate the S3 URL for the uploaded image
#     s3 = boto3.client(
#         service_name="s3",
#         region_name=S3_BUCKET_REGION,
#         aws_access_key_id=S3_ACCESS_KEY,
#         aws_secret_access_key=S3_SECRET_ACCESS_KEY
#     )

#     result_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': "resultimg", 'Key': image_code},
#         ExpiresIn=3600  # URL's expiration time in seconds
#     )
    
#     # Pass the object names, directory name, and identifier to the template
#     return render_template('page5.html',code=image_code, object_names=object_names, directory_name=directory_name_split, identifier=identifier, oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier, file_names=file_names)

# # Function to extract file names from a directory
# # def get_file_names_from_directory(directory_path):
# #     file_names = os.listdir(directory_path)
# #     return redirect(url_for('/user_check', file_names=file_names))

# def get_file_names_from_directory(bucket_name, directory_path):
#     file_names = []
#     response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)
#     for obj in response.get('Contents', []):
#         file_name = obj['Key'].split('/')[-1]
#         file_names.append(file_name)
#     return file_names

# # mojji-output-img directory and its contents
# s3_directory_path = find_directory_with_prefix('mojji-output-img', 'mojji-output-img')

# if s3_directory_path is None:
#     print("Directory with prefix '{}' not found in the S3 bucket.".format('mojji-output-img'))
# else:
#     # Extract file names from the directory
#     file_names = get_file_names_from_directory('mojji-output-img', s3_directory_path)
#     print("File names in the directory '{}':".format(s3_directory_path))
#     print(file_names)
########################################################################################

# S3 client creation
s3 = boto3.client(
    service_name="s3",
    region_name=S3_BUCKET_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_ACCESS_KEY
)

def find_directory_with_prefix(bucket_name, prefix):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')
    for common_prefix in response.get('CommonPrefixes', []):
        directory_path = common_prefix['Prefix']
        return directory_path
    return None

def get_file_names_from_directory(bucket_name, directory_path):
    file_names = []
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)
    for obj in response.get('Contents', []):
        file_name = obj['Key'].split('/')[-1]
        file_names.append(file_name)
    return file_names

@app.route('/user_check', methods=['GET'])
def user_check():
    # Get the value of identifier from the query parameters
    identifier = request.args.get('identifier', '')
    oauth_code = request.args.get('oauth_code', '')
    directory_name_split = request.args.get('directory_name_split', '')
    image_code = request.args.get('code', '')
    
    prefix = 'after_detection_'

    # Define the base directory path
    # base_directory = '/home/ubuntu/environment/efs/mojji-output-img/'
    
    directory_with_prefix = find_directory_with_prefix('mojji-output-img', prefix)

    if directory_with_prefix is None:
        # If the directory with the prefix is not found, handle the error
        return "Directory with prefix '{}' not found.".format(prefix)
        
    # Construct the full identifier with the directory name
    full_identifier = os.path.join(directory_name_split)
    full_directory = prefix + full_identifier

    object_names = get_file_names_from_directory('mojji-output-img', full_directory)

    # You can use the code to generate the S3 URL for the uploaded image
    result_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': "resultimg", 'Key': image_code},
        ExpiresIn=3600  # URL's expiration time in seconds
    )
    
    # Mapping Korean categories to English categories for each file_name
    english_categories = [map_korean_to_english(file_name) for file_name in object_names]

    # Mapping English categories to Korean strings for each English category
    korean_strings = [map_english_to_string(english_category) for english_category in english_categories]

    # Pass the object names, directory name, and identifier to the template
    return render_template('page5.html', code=image_code, object_names=object_names,
                           directory_name=directory_name_split, identifier=identifier,
                           oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier,
                           english_categories=english_categories, korean_strings=korean_strings)

def map_korean_to_english(category):
    if category in ["short_sleeved_shirt", "long_sleeved_shirt", "vest", "sling"]:
        return "top"
    elif category in ["shorts", "trousers", "skirt"]:
        return "bottom"
    elif category in ["short_sleeved_outwear", "long_sleeved_outwear"]:
        return "outwear"
    else:
        return "dress"

def map_english_to_string(english_category):
    if english_category == "top":
        return "상 의"
    elif english_category == "bottom":
        return "하 의"
    elif english_category == "outwear":
        return "아우터"
    else:
        return "드레스"

###############################Result 초기#########################################################

# image_urls = []

# @app.route('/result', methods=['GET'])
# def result():
#     identifier = request.args.get('identifier', '')
#     print(f"Received identifier: {identifier}")

#     s3 = boto3.client(
#         service_name="s3",
#         region_name=S3_BUCKET_REGION,
#         aws_access_key_id=S3_ACCESS_KEY,
#         aws_secret_access_key=S3_SECRET_ACCESS_KEY
#     )

#     # Clear the image_urls list before adding new images
#     image_urls.clear()

#     # Get images from S3 and append them to the image_urls list
#     folder_name = "3_20230721094142865156_2022110317125200000004364"
#     get_images_from_s3(s3, "resultimg", folder_name)

#     # Print image URLs for debugging
#     print(f"Image URLs: {image_urls}")

#     return render_template('page4.html', image_urls=image_urls, identifier=identifier)
    
        
########################################################################################

#######################################rResult 테스트#################################################
image_urls = []

@app.route('/result', methods=['GET'])
def result():
    oauth_code = session.get('oauth_code', '')
    image_code = request.args.get('code', '')
    identifier = request.args.get('identifier', '')
    print(f"Received identifier: {identifier}")

    s3 = boto3.client(
        service_name="s3",
        region_name=S3_BUCKET_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY
    )

    # Clear the image_urls list before adding new images
    image_urls.clear()

    # Fetch images from S3 based on the identifier
    folder_name = f"{identifier.rsplit('_', 1)[0]}"
    objects = get_objects_from_s3(s3, "resultimg", folder_name)

    # Get the URLs of the objects and append them to the image_urls list
    for obj in objects:
        image_url = f"https://resultimg.s3.ap-northeast-2.amazonaws.com/{obj['Key']}"
        image_urls.append(image_url)

    return render_template('page4.html', image_urls=image_urls, identifier=identifier, image_code=image_code)

def get_objects_from_s3(s3_client, bucket_name, folder_name):
    # Retrieve objects from the specified folder in the S3 bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    objects = response.get('Contents', [])
    return objects

########################################################################################
####################################원본####################################################

# Global variable to keep track of the current number
current_number = 1

# @app.route('/upload', methods=['POST'])
# def upload():
#     global current_number  # Access the global variable
#     file = request.files['file']
#     if file:
#         # Generate the unique filename using number, timestamp, and original filename
#         timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Add timestamp to ensure uniqueness
#         filename = secure_filename(file.filename)  # Get the original filename
#         number = 1  # Replace with the desired number
#         extension = os.path.splitext(filename)[1]
        
#         filename_without_extension = os.path.splitext(filename)[0]  # Get the filename without extension
#         unique_filename = f"{current_number}_{timestamp}_{filename_without_extension}{extension}"  # Format: number_timestamp_filename.extension
#         unique_filename_split = f"{current_number}_{timestamp}_{filename_without_extension}"  # Format: number_timestamp_filename.extension
#         # Save the file to the desired directory
#         file.save('/home/ubuntu/environment/efs/coai-original-images/' + unique_filename)
        
#         # Increment the current number for the next upload
#         current_number += 1

#         # Generate the URL for the uploaded image
#         url = '/coai-original-images/' + unique_filename
        
#         ##
#         # 세션에 identifier 저장
#         # session['identifier'] = unique_filename
#         ##
        
        # s3 = boto3.client(service_name="s3",
        #                   region_name=S3_BUCKET_REGION,
        #                   aws_access_key_id=S3_ACCESS_KEY,
        #                   aws_secret_access_key=S3_SECRET_ACCESS_KEY)
        
        # load_url = s3.generate_presigned_url(
        #     'get_object',
        #     Params={'Bucket': S3_BUCKET, 'Key': unique_filename},
        #     ExpiresIn=3600  # URL's expiration time in seconds
        # )

#         # full_url = urljoin(url_for('get_direc_name', identifier=unique_filename), load_url)
    
#         # return redirect(full_url)    
        
#         return redirect(url_for('get_direc_name', identifier=unique_filename, image_url=load_url, directory_name_split=unique_filename_split))
#     else:
#         return '���로드할 파일을 선택하세요.'

#############테스트#########
@app.route('/upload', methods=['POST'])
def upload():
    oauth_code = session.get('oauth_code', '')
    
    # global current_number  # Access the global variable
    file = request.files['file']
    if file:
        # Generate the unique filename using number, timestamp, and original filename
        # timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Add timestamp to ensure uniqueness
        filename = secure_filename(file.filename)  # Get the original filename
        # number = 1  # Replace with the desired number
        extension = os.path.splitext(filename)[1]
        
        filename_without_extension = os.path.splitext(filename)[0]  # Get the filename without extension
        unique_filename = f"{oauth_code}_{filename_without_extension}{extension}"  # Format: number_timestamp_filename.extension
        unique_filename_split = f"{oauth_code}_{filename_without_extension}"  # Format: number_timestamp_filename.extension
        # Save the file to the desired directory
        file.save('/home/ubuntu/environment/efs/coai-original-images/' + unique_filename)
        
        # Increment the current number for the next upload
        # current_number += 1

        # Generate the URL for the uploaded image
        url = '/coai-original-images/' + unique_filename
        
        s3 = boto3.client(service_name="s3",
                          region_name=S3_BUCKET_REGION,
                          aws_access_key_id=S3_ACCESS_KEY,
                          aws_secret_access_key=S3_SECRET_ACCESS_KEY)
        
        load_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': "coai-original-images", 'Key': unique_filename},
            ExpiresIn=3600  # URL's expiration time in seconds
        )

        # Pass oauth_code as a query parameter in url_for
        return redirect(url_for('get_direc_name', code=unique_filename, image_url=load_url, directory_name_split=unique_filename_split, oauth_code=oauth_code))
    else:
        return '업로드할 파일을 선택하세요.'


################정상###############################################

@app.route('/check_user', methods=['POST'])
def check_user():
    oauth_code = session.get('oauth_code', '')
    code = request.args.get('code', '')
    image_url = urllib.parse.unquote(request.args.get('image_url', ''))
    directory_name_split = request.args.get('directory_name_split', '')
    image_filename = request.args.get('unique_filename', '')

    # Generate the URL for the uploaded image
    url = '/mojji-output-img/after_detection_' + directory_name_split

    s3 = boto3.client(service_name="s3",
                      region_name=S3_BUCKET_REGION,
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_ACCESS_KEY)

    # You can use the code to generate the S3 URL for the uploaded image
    load_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': "mojji-output-img", 'Key': f'after_detection_{directory_name_split}/{image_filename}'},
        ExpiresIn=3600  # URL's expiration time in seconds
    )

    # Pass oauth_code as a query parameter in url_for
    return redirect(url_for('check_user_url', code=code, image_url=load_url, directory_name_split=directory_name_split, oauth_code=oauth_code))


# @app.route('/check_user', methods=['GET'])
# def check_user():
#     # Get the value of identifier from the query parameters
#     identifier = request.args.get('identifier', '')
#     print(f"Received identifier: {identifier}")
#     # Find the directory with the 'after_detection_' prefix
#     prefix = "after_detection_"
    # directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)

    # if directory_with_prefix is None:
    #     # If the directory with the prefix is not found, handle the error
    #     return "Directory with prefix '{}' not found.".format(prefix)

    # # Construct the full identifier with the directory name
    # full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)

#     # Append the identifier to the URL
#     url_with_identifier = "/check_user?identifier=" + identifier

#     image_names = []  # List to store the image names
    
#     # Iterate over the files in the directory
#     for file_name in os.listdir(full_identifier):
#         if file_name.endswith('.jpg') or file_name.endswith('.png'):
#             # bottom = ['trousers', 'skirt', 'shorts']
#             # top = ['shirt','vest','sling']
            
#             # if any(keyword in file_name for keyword in top):
#             # 	search = 'top'
#             # 	image_names.append(search)
#             # if any(keyword in file_name for keyword in bottom):
#             # 	search = 'bottom'
#             # 	image_names.append(search)
#             # if any('dress' in file_name):
#             # 	search = 'dress'
#             # 	image_names.append(search)
#             # if any('outwear' in file_name):
#             # 	search = 'outwear'
#             # 	image_names.append(search)
#             image_names.append(file_name)
    
#     # Pass the directory name and identifier to the template
#     return render_template('page5.html', image_names=image_names, directory_name=directory_with_prefix, identifier=identifier)

###############################################################
from flask import url_for
import urllib.parse

# @app.route('/check_user', methods=['POST'])
# def check_user():
#     oauth_code = session.get('oauth_code', '')
#     code = request.args.get('code', '')
#     image_url = urllib.parse.unquote(request.args.get('image_url', ''))
#     directory_name_split = request.args.get('directory_name_split', '')
#     image_filename = request.args.get('unique_filename', '')

#     # Generate the URL for the uploaded image
#     url = '/mojji-output-img/after_detection_' + directory_name_split

#     s3 = boto3.client(service_name="s3",
#                       region_name=S3_BUCKET_REGION,
#                       aws_access_key_id=S3_ACCESS_KEY,
#                       aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#     # You can use the code to generate the S3 URL for the uploaded image
#     load_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': "mojji-output-img", 'Key': f'after_detection_{directory_name_split}/{image_filename}'},
#         ExpiresIn=3600  # URL's expiration time in seconds
#     )

#     # Pass oauth_code as a query parameter in url_for
    # return redirect(url_for('check_user_url', code=code, image_url=load_url, directory_name_split=directory_name_split, oauth_code=oauth_code))


import boto3
from flask import url_for, redirect, request, render_template

# '/check_user_url' 엔드포인트
@app.route('/check_user_url', methods=['GET'])
def check_user_url():
    code = request.args.get('code', '')
    oauth_code = session.get('oauth_code')
    image_url = request.args.get('image_url', '')
    directory_name_split = request.args.get('directory_name_split', '')  # Query parameters로부터 directory_name_split을 가져옴

    # image_url에서 이미지 파일명 추출
    image_filename = image_url.split('/')[-1].split('?')[0]
    
    identifier = request.form.get('identifier')
    selected_value = request.form.get('selectedValue')

    # 'boto3'를 이용해 S3 버킷에 접근하여 이미지 URL 생성
    s3 = boto3.client(
        service_name="s3",
        region_name=S3_BUCKET_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY
    )

    # 수정된 'load_url' 생성
    load_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': "mojji-output-img", 'Key': f'{code}/{image_filename}'},
        ExpiresIn=3600  # URL의 만료 시간 (초 단위)
    )

    # Return the imageURL as a JSON response
    # response = {'imageURL': directory_name_split}
    # return jsonify(response)
    
    response = {
        'unique_filename': code,
        'image_url': load_url,
        'image_filename': image_filename,
        'oauth_code': oauth_code,
        'directory_name_split': directory_name_split
    }

    # Return the JSON response
    return jsonify(response)
    
    # return render_template('page5.html', unique_filename=code, image_url=load_url, image_filename=image_filename, oauth_code=oauth_code, directory_name_split=directory_name_split)

########################테스트 경린####################################

# from flask import request, redirect, url_for, session
# from werkzeug.utils import secure_filename
# import os
# import urllib.parse
# import boto3

# @app.route('/check_user', methods=['POST'])
# def check_user():
#     oauth_code = session.get('oauth_code', '')
#     code = request.args.get('code', '')
#     image_url = urllib.parse.unquote(request.args.get('image_url', ''))
#     directory_name_split = request.args.get('directory_name_split', '')
#     image_filename = request.args.get('unique_filename', '')
    
#     file = request.files['file']
#     if file:
#         filename = secure_filename(file.filename)
#         extension = os.path.splitext(filename)[1]
#         filename_without_extension = os.path.splitext(filename)[0]
#         unique_filename = f"{oauth_code}_{filename_without_extension}{extension}"
#         unique_filename_split = f"{oauth_code}_{filename_without_extension}"
        
#         # Save the file to the desired directory
#         file.save('/home/ubuntu/environment/efs/mojji-output-img/' + unique_filename)

#     # Generate the URL for the uploaded image
#     url = '/mojji-output-img/after_detection_' + directory_name_split

#     s3 = boto3.client(service_name="s3",
#                       region_name=S3_BUCKET_REGION,
#                       aws_access_key_id=S3_ACCESS_KEY,
#                       aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#     load_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': "mojji-output-img", 'Key': f'after_detection_{directory_name_split}',
#                 'ExpiresIn': 3600})  # 콜론이 추가된 부분
    
#     # Pass oauth_code as a query parameter in url_for
#     return redirect(url_for('check_user_url', code=unique_filename, image_url=load_url, directory_name_split=directory_name_split, oauth_code=oauth_code))


# ##########################테스트2#####################################
# import urllib.parse

# @app.route('/check_user_url', methods=['GET'])
# def check_user_url():
#     code = request.args.get('code', '')
#     oauth_code = session.get('oauth_code')
#     image_url = request.args.get('image_url', '')
#     directory_name_split = request.args.get('directory_name_split', '')  # Get the directory_name_split from query parameters

#     # Extract the image filename from the 'image_url'
#     image_filename = image_url.split('/')[-1].split('?')[0]

#     # You can use the code to generate the S3 URL for the uploaded image
#     s3 = boto3.client(
#         service_name="s3",
#         region_name=S3_BUCKET_REGION,
#         aws_access_key_id=S3_ACCESS_KEY,
#         aws_secret_access_key=S3_SECRET_ACCESS_KEY
#     )

#     load_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': "mojji-output-img", 'Key': image_url},
#         ExpiresIn=3600  # URL's expiration time in seconds
#     )
    
#     return render_template('page5.html', unique_filename=code, image_url=load_url, image_filename=image_filename,directory_name_split=directory_name_split, oauth_code=oauth_code)


###############################################################

# 분석 후 사용자 선택페이지
# def find_directory_with_prefix(directory_path, prefix):
#     for dir_name in os.listdir(directory_path):
#         # Check if the directory name starts with the given prefix
#         if dir_name.startswith(prefix):
#             return dir_name
#     return None
    

############################################테스트############################################
import csv
from urllib.parse import unquote
import re
from flask import url_for, redirect

@app.route('/get_direc_name')
def get_direc_name():
    # Get the value of 'code' and 'image_url' from the query parameters
    code = request.args.get('code', '')
    oauth_code = session.get('oauth_code')
    image_url = urllib.parse.unquote(request.args.get('image_url', ''))
    
    directory_name_split = request.args.get('directory_name_split', '')

    # Extract the image filename from the 'image_url'
    image_filename = image_url.split('/')[-1].split('?')[0]

    # You can use the code to generate the S3 URL for the uploaded image
    s3 = boto3.client(
        service_name="s3",
        region_name=S3_BUCKET_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY
    )

    load_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': "coai-original-images", 'Key': code},
        ExpiresIn=3600  # URL's expiration time in seconds
    )
    
    load_url_check = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': "mojji-output-img", 'Key': f'after_detection_{code}/{image_filename}'},
        ExpiresIn=3600  # URL의 만료 시간 (초 단위)
    )
    
    return render_template('page6.html', unique_filename=code, image_url=load_url, image_filename=image_filename, oauth_code=oauth_code, directory_name_split=directory_name_split, load_url_check=load_url_check)


# @app.route('/get_direc_name')
# def get_direc_name():
#     # Get the value of identifier from the query parameters
#     identifier = request.args.get('identifier', '')
#     image_url = request.args.get('image_url', '')
#     directory_name_split = request.args.get('directory_name_split', '')
#     code = request.args.get('code', '')  # Retrieve the code from query parameters

#     url = '/coai-original-images/' + identifier

#     s3 = boto3.client(service_name="s3",
#                       region_name=S3_BUCKET_REGION,
#                       aws_access_key_id=S3_ACCESS_KEY,
#                       aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#     load_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': S3_BUCKET, 'Key': identifier},
#         ExpiresIn=3600  # URL's expiration time in seconds
#     )

#     return render_template('page6.html', unique_filename=identifier, image_url=image_url, directory_name=directory_name_split, code=code)

#######################################원본#################################################

# @app.route('/get_direc_name')
# def get_direc_name():
#     # Get the value of identifier from the query parameters
#     identifier = request.args.get('identifier', '')
#     image_url = request.args.get('image_url', '')
#     directory_name_split = request.args.get('directory_name_split', '')  # Get the directory_name_split from query parameters

#     url = '/coai-original-images/' + identifier

#     s3 = boto3.client(service_name="s3",
#                       region_name=S3_BUCKET_REGION,
#                       aws_access_key_id=S3_ACCESS_KEY,
#                       aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#     load_url = s3.generate_presigned_url(
#         'get_object',
#         Params={'Bucket': S3_BUCKET, 'Key': identifier},
#         ExpiresIn=3600  # URL's expiration time in seconds
#     )

#     #return render_template('page6.html', directory=url, image_url=load_url)
#     return render_template('page6.html', unique_filename=identifier, image_url=image_url, directory_name=directory_name_split)
    #return render_template('page6.html', image_names=image_names, directory_name_split=directory_name_split, identifier=identifier)

##############CSV 파일 저장 초기값##########################################
# import csv
# from urllib.parse import unquote

# @app.route('/save-csv-new', methods=['POST'])
# def save_csv():
#     identifier = request.args.get('identifier', '')
#     data = request.get_json()
#     encoded_uri = data.get('data')

#     directory = '/home/ubuntu/environment/efs/crawling_csv'  # Replace with the desired directory path on your EC2 instance

#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     # Use the `identifier` to generate the CSV filename with the .csv extension
#     csv_filename = f"{identifier}.csv"
#     csv_path = os.path.join(directory, csv_filename)

#     with open(csv_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         decoded_uri = unquote(encoded_uri)  # Decode the URI-encoded values
#         rows = decoded_uri.splitlines()  # Split the decoded URI into rows
#         rows = [row.replace('data:text/csv;charset=utf-8,', '') for row in rows]  # Remove the prefix
#         for row in rows:
#             values = row.split(',')  # Split each row by the comma character
#             writer.writerow(values)  # Write the values to the CSV file

#     return redirect('result')

####################################CSV TEST#####################################################

# import csv
# from urllib.parse import unquote
# import re
# from flask import url_for, redirect

# @app.route('/save-csv-new', methods=['POST'])
# def save_csv():
#     identifier_param = request.args.get('identifier', '')
#     data = request.get_json()
#     encoded_uri = data.get('data')
#     directory_name_split = request.args.get('directory_name_split', '')

#     # Sanitize the identifier to remove non-alphanumeric characters
#     sanitized_identifier = re.sub(r'\W+', '_', identifier_param)

#     directory = '/home/ubuntu/environment/efs/crawling_csv'
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     # Generate a unique filename using the sanitized identifier
#     csv_filename = directory_name_split + '.csv'
#     csv_path = os.path.join(directory, csv_filename)

#     with open(csv_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         decoded_uri = unquote(encoded_uri)
#         rows = decoded_uri.splitlines()
#         rows = [row.replace('data:text/csv;charset=utf-8,', '') for row in rows]
#         for row in rows:
#             values = row.split(',')
#             writer.writerow(values)

#     # Use the sanitized identifier for redirection
#     return redirect(url_for('result', identifier=identifier_param))



#########################################################################

import os
import csv
from urllib.parse import unquote
import re
from flask import Flask, request, url_for, redirect

@app.route('/save-csv-new', methods=['POST'])
def save_csv():
    identifier_param = request.args.get('identifier', '')
    data = request.get_json()
    encoded_uri = data.get('data')
    directory_name_split = request.args.get('directory_name_split', '')

    # Sanitize the identifier to remove non-alphanumeric characters
    sanitized_identifier = re.sub(r'\W+', '_', identifier_param)

    directory = '/home/ubuntu/environment/efs/crawling_csv'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a unique filename using the sanitized identifier and directory_name_split
    csv_filename = f'{directory_name_split}.csv'
    csv_path = os.path.join(directory, csv_filename)

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        decoded_uri = unquote(encoded_uri)
        rows = decoded_uri.splitlines()
        rows = [row.replace('data:text/csv;charset=utf-8,', '') for row in rows]
        for row in rows:
            values = row.split(',')
            writer.writerow(values)

    # Use the sanitized identifier for redirection
    return redirect(url_for('result', identifier=sanitized_identifier))

# =====================================테스트=============================================

# const fs = require("fs");
# const express = require("express");
# const app = express();
# const port = 5001; // 원하는 포트 번호로 변경

# // 서버 측의 /save-csv-new 엔드포인트를 생성하여 CSV 파일 생성과 권�� 설정을 처리합니다.
# app.post("/save-csv-new", (req, res) => {
#   const { identifier } = req.query;
#   const selectedEnglishClothingType = koreanToEnglishClothing(selectedClothingType);
#   const selectedClothingWithoutExtension = selectedClothingType.replace(/\.[^.]+$/, "");
#   const selectedClothingWithoutSuffix = selectedClothingWithoutExtension.replace(/_\d+$/, "");
#   const selectedEnglishClothingType = getCategoryAndEnglishTerm(selectedClothingWithoutSuffix);

#   const data = [
#     ["Clothing Type", "Color", "Category"],
#     [selectedEnglishClothingType, selectedColor, selectedCategory]
#   ];

#   const csvContent = data.map(row => row.join(",")).join("\r\n");
#   const filePath = "/home/ubuntu/environment/efs/crawling_csv"; // 실제 파일 경로로 변경

#   // 파일 생성
#   fs.writeFileSync(filePath, csvContent);

#   // 권한 설정 (chmod 666)
#   fs.chmodSync(filePath, 0o666);

#   // 응답 보내기
#   res.sendStatus(200);
# });

# app.listen(port, () => {
#   console.log(`Server is running on port ${port}`);
# });

################################카카오 로그인################################
from flask import Flask, render_template, request, jsonify, make_response
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    get_jwt_identity, jwt_required,
    set_access_cookies, set_refresh_cookies, 
    unset_jwt_cookies, create_refresh_token,
    jwt_refresh_token_required,
)
from config import CLIENT_ID, REDIRECT_URI, CLIENT_SECRET
from controller import Oauth
from model import UserModel, UserData

app.config['SECRET_KEY'] = 'your_generated_secret_key_here'  # Replace 'your_generated_secret_key_here' with the secret key you

app.config['JWT_SECRET_KEY'] = "I'M IML."
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 30
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 100
jwt = JWTManager(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/oauth")
def oauth_api():
    """
    # OAuth API [GET]
    사용자로부터 authorization code를 인자로 받은 후,
    아래의 과정 수행함
    1. 전달받은 authorization code를 통해서
        access_token, refresh_token을 발급.
    2. access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    3. 해당 식별 정보를 서비스 DB에 저장 (회원가입)
    3-1. 만약 이미 있을 경우, (3) 과정 스킵
    4. 사용자 식별 id를 바탕으로 서비스 전용 access_token 생성
    """
    code = str(request.args.get('code'))
    session['oauth_code'] = code
    
    oauth = Oauth()
    auth_info = oauth.auth(code)
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    user = UserData(user)
    UserModel().upsert_user(user)

    resp = make_response(render_template('index_mojji.html'))
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    resp.set_cookie("logined", "true")
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp


@app.route('/token/refresh')
@jwt_refresh_token_required
def token_refresh_api():
    """
    Refresh Token을 이용한 Access Token 재발급
    """
    user_id = get_jwt_identity()
    resp = jsonify({'result': True})
    access_token = create_access_token(identity=user_id)
    set_access_cookies(resp, access_token)
    return resp


@app.route('/token/remove')
def token_remove_api():
    """
    Cookie에 등록된 Token 제거
    """
    resp = jsonify({'result': True})
    unset_jwt_cookies(resp)
    resp.delete_cookie('logined')
    return resp


@app.route("/userinfo")
@jwt_required
def userinfo():
    """
    Access Token을 이용한 DB에 저장된 사용자 정보 가져오기
    """
    user_id = get_jwt_identity()
    userinfo = UserModel().get_user(user_id).serialize()
    return jsonify(userinfo)


@app.route('/oauth/url')
def oauth_url_api():
    """
    Kakao OAuth URL 가져오기
    """
    return jsonify(
        kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
        % (CLIENT_ID, REDIRECT_URI)
    )


@app.route("/oauth/refresh", methods=['POST'])
def oauth_refesh_api():
    """
    # OAuth Refresh API
    refresh token을 인자로 받은 후,
    kakao에서 access_token 및 refresh_token을 재발급.
    (% refresh token의 경우, 
    유효기간이 1달 이상일 경우 결과에서 제외됨)
    """
    refresh_token = request.get_json()['refresh_token']
    result = Oauth().refresh(refresh_token)
    return jsonify(result)


@app.route("/oauth/userinfo", methods=['POST'])
def oauth_userinfo_api():
    """
    # OAuth Userinfo API
    kakao access token을 인자로 받은 후,
    kakao에서 해당 유저의 실제 Userinfo를 가져옴
    """
    access_token = request.get_json()['access_token']
    result = Oauth().userinfo("Bearer " + access_token)
    return jsonify(result)








##################CICD###############
import signal

def stop_server(signal, frame):
    print("Stopping server...")
    # Add any cleanup code here if necessary
    exit(0)

# Register the signal handler
######################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)