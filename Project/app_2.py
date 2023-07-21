from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, session ##
from flask_session import Session ##
from werkzeug.utils import secure_filename
from datetime import datetime

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
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
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
########################################################################################

# 이미지 URL들을 담을 리스트 변수
image_urls = []


@app.route('/result')
def result():
    # Get the value of identifier from the query parameters
    # identifier = request.args.get('identifier', '')
    # 세션으로부터 identifier 값을 가져옴
    identifier = session.get('identifier', '')
    
    s3 = boto3.client(
        service_name="s3",
        region_name=S3_BUCKET_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_ACCESS_KEY
    )

    image_urls.clear()  # 기존 데이터를 모두 지우고 새로 읽어옴

    # 식별자 예시
    #### 식별자 어떻게 받을지,,
    # identifier = '4_20230718182949142448_3333'

    get_images_from_s3(s3, "musinsa-codishop-bucket", identifier)

    return render_template('page4.html', image_urls=image_urls, identifier=identifier)

def get_images_from_s3(s3_client, bucket_name, identifier):
    # S3 버킷에서 디렉터리 목록을 가져오기
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="result_codi/")

    # 해당 디렉터리 안에 있는 파일들 중에서 식별자를 포함하는 파일들의 이미지 URL들을 생성
    if 'Contents' in response:
        for obj in response['Contents']:
            image_key = obj['Key']
            if identifier in image_key:
                url = s3_client.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': bucket_name, 'Key': image_key},
                    ExpiresIn=3600  # URL의 만료 시간 (예: 3600초 = 1시간)
                )
                image_urls.append(url)

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
        
        # Save the file to the desired directory
        file.save('/home/ubuntu/environment/efs/coai-original-images/' + unique_filename)
        
        # Increment the current number for the next upload
        current_number += 1

        # Generate the URL for the uploaded image
        url = '/coai-original-images/' + unique_filename
        
        ##
        # 세션에 identifier 저장
        session['identifier'] = unique_filename
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
    
        return redirect(url_for('get_direc_name', identifier=unique_filename, image_url=load_url))
    else:
        return '업로드할 파일을 선택하세요.'


###############################################################
###############################################################

# 분석 후 사용자 선택페이지
def find_directory_with_prefix(directory_path, prefix):
    for dir_name in os.listdir(directory_path):
        # Check if the directory name starts with the given prefix
        if dir_name.startswith(prefix):
            return dir_name
    return None

@app.route('/check_user', methods=['GET'])
def check_user():
    # Get the value of identifier from the query parameters
    identifier = request.args.get('identifier', '')

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
            image_names.append(file_name)
    
    return render_template('page5.html', image_names=image_names, directory_path=full_identifier, identifier=url_with_identifier)

########################################################################################
########################################################################################

@app.route('/get_direc_name')
def get_direc_name():
    # Get the value of identifier from the query parameters
    identifier = request.args.get('identifier', '')
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

    return render_template('page6.html', directory=url, image_url=load_url)

########################################################################################
########################################################################################

import csv
from urllib.parse import unquote

@app.route('/save-csv-new', methods=['POST'])
def save_csv():
    identifier = request.args.get('identifier', '')
    data = request.get_json()
    encoded_uri = data.get('data')

    directory = '/home/ubuntu/environment/efs/crawling_csv'  # Replace with the desired directory path on your EC2 instance

    if not os.path.exists(directory):
        os.makedirs(directory)

    # Use the `identifier` to generate the CSV filename with the .csv extension
    csv_filename = f"{identifier}.csv"
    csv_path = os.path.join(directory, csv_filename)

    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        decoded_uri = unquote(encoded_uri)  # Decode the URI-encoded values
        rows = decoded_uri.splitlines()  # Split the decoded URI into rows
        rows = [row.replace('data:text/csv;charset=utf-8,', '') for row in rows]  # Remove the prefix
        for row in rows:
            values = row.split(',')  # Split each row by the comma character
            writer.writerow(values)  # Write the values to the CSV file

    return redirect('result')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)