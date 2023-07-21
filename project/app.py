from flask import Flask, render_template, request

import os
import flask
import boto3

from m_config import S3_BUCKET, S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, S3_BUCKET_REGION
import uuid
import pymysql

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/photo')
def photo():
    return render_template('page1.html')

@app.route('/loading')
def loading():
    return render_template('page6.html')

@app.route('/result')
def result():
    return render_template('page4.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     if file:
#         s3 = boto3.client(service_name="s3",
#                           region_name=S3_BUCKET_REGION,
#                           aws_access_key_id=S3_ACCESS_KEY,
#                           aws_secret_access_key=S3_SECRET_ACCESS_KEY)
#         filename = str(uuid.uuid4())
#         s3.upload_fileobj(file, S3_BUCKET, filename)

#         url = s3.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': S3_BUCKET, 'Key': filename},
#             ExpiresIn=3600  # URL의 유효 기간 설정 (초 단위)
#         )
    
#         return render_template('page6.html', image_url=url)
#     else:
#         return '업로드할 파일을 선택하세요.'
        
##############################################################
##############################################################
# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     if file:
#         s3 = boto3.client(service_name="s3",
#                           region_name=S3_BUCKET_REGION,
#                           aws_access_key_id=S3_ACCESS_KEY,
#                           aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#         # Get the original filename and extension
#         filename = file.filename
#         extension = os.path.splitext(filename)[1]

#         # Generate a unique filename
#         unique_filename = str(uuid.uuid4()) + extension
#         s3.upload_fileobj(file, S3_BUCKET, unique_filename)

#         url = s3.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': S3_BUCKET, 'Key': unique_filename},
#             ExpiresIn=3600  # URL's expiration time in seconds
#         )

#         return render_template('page6.html', image_url=url)
#     else:
#         return '업로드할 파일을 선택하세요.'
##############################################################
##############################################################
# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     if file:
#         s3 = boto3.client(service_name="s3",
#                           region_name=S3_BUCKET_REGION,
#                           aws_access_key_id=S3_ACCESS_KEY,
#                           aws_secret_access_key=S3_SECRET_ACCESS_KEY)

#         # Get the original filename
#         filename = file.filename

#         # Upload the file to S3 with the original filename
#         s3.upload_fileobj(file, S3_BUCKET, filename)

#         url = s3.generate_presigned_url(
#             'get_object',
#             Params={'Bucket': S3_BUCKET, 'Key': filename},
#             ExpiresIn=3600  # URL's expiration time in seconds
#         )

#         return render_template('page6.html', image_url=url)
#     else:
#         return '업로드할 파일을 선택하세요.'
########################################################
########################################################
@app.route('/uploads/<filename>')
def get_uploaded_file(filename):
    return send_from_directory('/home/ubuntu/environment/project/coai-original-images-ec2', filename)

# EC2로 이미지 저장
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        # Save the file to a local directory on the EC2 instance
        file.save('/home/ubuntu/environment/project/coai-original-images/' + file.filename)

        url = f'/home/ubuntu/environment/project/coai-original-images/{file.filename}'

        return render_template('page6.html', image_url=url)
    else:
        return '업로드할 파일을 선택하세요.'

# AWS RDS(MariaDB) 연결 정보
config = {
    'user': 'admin',
    'password': 'pass123#',
    'host': 'database-test-coai-1.ch4wa8d8qhxt.ap-northeast-2.rds.amazonaws.com',
    'database': 'coaiDBtest',
    'port': 3306,
}

# RDS 연결 생성 함수
def create_db_connection():
    connection = pymysql.connect(**config)
    return connection

# Flask 애플리케이션에서 RDS 연결 사용
@app.route('/rdstest')
def rdstest():
    connection = create_db_connection()

    # 커서 생성
    cursor = connection.cursor()

    # 쿼리 실행
    query = "SELECT * FROM table_name"
    cursor.execute(query)

    # 결과 가져오기
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 커넥션과 커서 닫기
    cursor.close()
    connection.close()

    return 'Finish!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)