from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, session ##
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

from m_config import S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, S3_BUCKET_REGION
import pymysql

app = Flask(__name__, template_folder='template')

##
# 세션 설정
# app.config['SESSION_PERMANENT'] = False
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)
##

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/photo')
# def photo():
#     return render_template('page1.html')

@app.route('/loading')
def loading():
    return render_template('page6.html')
    
########################################################################################
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

    # Print image URLs for debugging
    print(f"Image URLs: {image_urls}")

    return render_template('page4.html', image_urls=image_urls, identifier=identifier)


def get_objects_from_s3(s3_client, bucket_name, folder_name):
    # Retrieve objects from the specified folder in the S3 bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    objects = response.get('Contents', [])
    return objects

########################################################################################
########################################################################################

# Global variable to keep track of the current number
current_number = 1

@app.route('/upload', methods=['POST'])
def upload():
    global current_number  # Access the global variable
    file = request.files['file']
    if file:
        # Generate the unique filename using number, timestamp, and original filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")  # Add timestamp to ensure uniqueness
        filename = secure_filename(file.filename)  # Get the original filename
        number = 1  # Replace with the desired number
        extension = os.path.splitext(filename)[1]
        
        filename_without_extension = os.path.splitext(filename)[0]  # Get the filename without extension
        unique_filename = f"{current_number}_{timestamp}_{filename_without_extension}{extension}"  # Format: number_timestamp_filename.extension
        unique_filename_split = f"{current_number}_{timestamp}_{filename_without_extension}"  # Format: number_timestamp_filename.extension
        # Save the file to the desired directory
        file.save('/home/ubuntu/environment/efs/coai-original-images/' + unique_filename)
        
        # Increment the current number for the next upload
        current_number += 1

        # Generate the URL for the uploaded image
        url = '/coai-original-images/' + unique_filename
        
        ##
        # 세션에 identifier 저장
        # session['identifier'] = unique_filename
        ##
        
        s3 = boto3.client(service_name="s3",
                          region_name=S3_BUCKET_REGION,
                          aws_access_key_id=S3_ACCESS_KEY,
                          aws_secret_access_key=S3_SECRET_ACCESS_KEY)
        
        load_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': S3_BUCKET, 'Key': unique_filename},
            ExpiresIn=3600  # URL's expiration time in seconds
        )

        # full_url = urljoin(url_for('get_direc_name', identifier=unique_filename), load_url)
    
        # return redirect(full_url)    
        
        return redirect(url_for('get_direc_name', identifier=unique_filename, image_url=load_url, directory_name_split=unique_filename_split))
    else:
        return '업로드할 파일을 선택하세요.'

#############테스트#########
################정상###############################################

# @app.route('/check_user', methods=['GET'])
# def check_user():
#     # Get the value of identifier from the query parameters
#     identifier = request.args.get('identifier', '')
#     print(f"Received identifier: {identifier}")
#     # Find the directory with the 'after_detection_' prefix
#     prefix = "after_detection_"
#     directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)

#     if directory_with_prefix is None:
#         # If the directory with the prefix is not found, handle the error
#         return "Directory with prefix '{}' not found.".format(prefix)

#     # Construct the full identifier with the directory name
#     full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)

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
########################테스트####################################

@app.route('/check_user', methods=['GET'])
def check_user():
    # Get the value of identifier from the query parameters
    identifier = request.args.get('identifier', '')
    print(f"Received identifier: {identifier}")
    
    # Find the directory with the 'after_detection_' prefix
    prefix = "after_detection_"
    directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)

    if directory_with_prefix is None:
        # If the directory with the prefix is not found, handle the error
        return "Directory with prefix '{}' not found.".format(prefix)

    # Construct the full identifier with the directory name
    full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)

    # Append the identifier to the URL
    url_with_identifier = "/check_user?identifier=" + identifier

    image_names = []  # List to store the image names
    
    # Iterate over the files in the directory
    for file_name in os.listdir(full_identifier):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            # Clean up the image name and remove file extension
            clean_image_name = os.path.splitext(file_name)[0]
            # Replace spaces with underscores
            clean_image_name = clean_image_name.replace(" ", "_")
            image_names.append(clean_image_name)
        
    return render_template('page5.html', image_names=image_names, directory_name=directory_with_prefix, identifier=identifier)


###############################################################

# 분석 후 사용자 선택페이지
def find_directory_with_prefix(directory_path, prefix):
    for dir_name in os.listdir(directory_path):
        # Check if the directory name starts with the given prefix
        if dir_name.startswith(prefix):
            return dir_name
    return None
    

########################################################################################
########################################################################################

@app.route('/get_direc_name')
def get_direc_name():
    # Get the value of identifier from the query parameters
    identifier = request.args.get('identifier', '')
    image_url = request.args.get('image_url', '')
    directory_name_split = request.args.get('directory_name_split', '')  # Get the directory_name_split from query parameters

    url = '/coai-original-images/' + identifier

    s3 = boto3.client(service_name="s3",
                      region_name=S3_BUCKET_REGION,
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_ACCESS_KEY)

    load_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': S3_BUCKET, 'Key': identifier},
        ExpiresIn=3600  # URL's expiration time in seconds
    )

    #return render_template('page6.html', directory=url, image_url=load_url)
    return render_template('page6.html', unique_filename=identifier, image_url=image_url, directory_name=directory_name_split)
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
import csv
from urllib.parse import unquote
import re
from flask import url_for, redirect

@app.route('/save-csv-new', methods=['POST'])
def save_csv():
    identifier_param = request.args.get('identifier', '')
    data = request.get_json()
    encoded_uri = data.get('data')

    # Sanitize the identifier to remove non-alphanumeric characters
    sanitized_identifier = re.sub(r'\W+', '_', identifier_param)

    directory = '/home/ubuntu/environment/efs/crawling_csv'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a unique filename using the sanitized identifier
    csv_filename = f"{sanitized_identifier.rsplit('_', 1)[0]}.csv"
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
    return redirect(url_for('result', identifier=identifier_param))


#########################################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)