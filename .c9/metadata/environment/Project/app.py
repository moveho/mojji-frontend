{"filter":false,"title":"app.py","tooltip":"/Project/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":116,"column":63},"end":{"row":122,"column":1},"action":"remove","lines":["","s3 = boto3.client(","    service_name=\"s3\",","    region_name=S3_BUCKET_REGION,","    aws_access_key_id=S3_ACCESS_KEY,","    aws_secret_access_key=S3_SECRET_ACCESS_KEY",")"],"id":613,"ignore":true}],[{"start":{"row":55,"column":0},"end":{"row":61,"column":15},"action":"remove","lines":["","def find_directory_with_prefix(bucket_name, prefix):","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')","    for common_prefix in response.get('CommonPrefixes', []):","        directory_path = common_prefix['Prefix']","        return directory_path","    return None"],"id":614,"ignore":true},{"start":{"row":55,"column":0},"end":{"row":61,"column":15},"action":"insert","lines":["","def find_directory_with_prefix(bucket_name, prefix):","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')","    for common_prefix in response.get('CommonPrefixes', []):","        directory_path = common_prefix['Prefix']","        return directory_path","    return None"]}],[{"start":{"row":56,"column":0},"end":{"row":61,"column":15},"action":"remove","lines":["def find_directory_with_prefix(bucket_name, prefix):","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')","    for common_prefix in response.get('CommonPrefixes', []):","        directory_path = common_prefix['Prefix']","        return directory_path","    return None"],"id":615,"ignore":true},{"start":{"row":56,"column":0},"end":{"row":69,"column":15},"action":"insert","lines":["# S3 client creation","s3 = boto3.client(","    service_name=\"s3\",","    region_name=S3_BUCKET_REGION,","    aws_access_key_id=S3_ACCESS_KEY,","    aws_secret_access_key=S3_SECRET_ACCESS_KEY",")","","def find_directory_with_prefix(bucket_name, prefix):","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')","    for common_prefix in response.get('CommonPrefixes', []):","        directory_path = common_prefix['Prefix']","        return directory_path","    return None"]}],[{"start":{"row":124,"column":0},"end":{"row":142,"column":21},"action":"remove","lines":["def get_file_names_from_directory(bucket_name, directory_path):","    file_names = []","    ","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)","    for obj in response.get('Contents', []):","        file_name = obj['Key'].split('/')[-1]","        file_names.append(file_name)","    return file_names","","# mojji-output-img 디렉터리와 동일한 디렉터리를 찾음","s3_directory_path = find_directory_with_prefix('mojji-output-img', 'mojji-output-img')","","if s3_directory_path is None:","    print(\"Directory with prefix '{}' not found in the S3 bucket.\".format('mojji-output-img'))","else:","    # 해당 디렉터리 내의 파일 이름 추출","    file_names = get_file_names_from_directory('mojji-output-img', s3_directory_path)","    print(\"File names in the directory '{}':\".format(s3_directory_path))","    print(file_names)"],"id":616,"ignore":true}],[{"start":{"row":124,"column":0},"end":{"row":141,"column":21},"action":"insert","lines":["def get_file_names_from_directory(bucket_name, directory_path):","    file_names = []","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)","    for obj in response.get('Contents', []):","        file_name = obj['Key'].split('/')[-1]","        file_names.append(file_name)","    return file_names","","# mojji-output-img directory and its contents","s3_directory_path = find_directory_with_prefix(S3_BUCKET_NAME, S3_DIRECTORY_PREFIX)","","if s3_directory_path is None:","    print(\"Directory with prefix '{}' not found in the S3 bucket.\".format(S3_DIRECTORY_PREFIX))","else:","    # Extract file names from the directory","    file_names = get_file_names_from_directory(S3_BUCKET_NAME, s3_directory_path)","    print(\"File names in the directory '{}':\".format(s3_directory_path))","    print(file_names)"],"id":617,"ignore":true}],[{"start":{"row":133,"column":47},"end":{"row":133,"column":61},"action":"remove","lines":["S3_BUCKET_NAME"],"id":618,"ignore":true},{"start":{"row":133,"column":47},"end":{"row":133,"column":65},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":133,"column":67},"end":{"row":133,"column":86},"action":"remove","lines":["S3_DIRECTORY_PREFIX"],"id":619,"ignore":true},{"start":{"row":133,"column":67},"end":{"row":133,"column":85},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":136,"column":74},"end":{"row":136,"column":93},"action":"remove","lines":["S3_DIRECTORY_PREFIX"],"id":620,"ignore":true},{"start":{"row":136,"column":74},"end":{"row":136,"column":92},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":139,"column":47},"end":{"row":139,"column":61},"action":"remove","lines":["S3_BUCKET_NAME"],"id":621,"ignore":true},{"start":{"row":139,"column":47},"end":{"row":139,"column":65},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":136,"column":74},"end":{"row":136,"column":92},"action":"remove","lines":["'mojji-output-img'"],"id":622,"ignore":true},{"start":{"row":136,"column":74},"end":{"row":136,"column":93},"action":"insert","lines":["S3_DIRECTORY_PREFIX"]},{"start":{"row":139,"column":47},"end":{"row":139,"column":65},"action":"remove","lines":["'mojji-output-img'"]},{"start":{"row":139,"column":47},"end":{"row":139,"column":61},"action":"insert","lines":["S3_BUCKET_NAME"]}],[{"start":{"row":136,"column":74},"end":{"row":136,"column":93},"action":"remove","lines":["S3_DIRECTORY_PREFIX"],"id":623,"ignore":true},{"start":{"row":136,"column":74},"end":{"row":136,"column":92},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":139,"column":47},"end":{"row":139,"column":61},"action":"remove","lines":["S3_BUCKET_NAME"],"id":624,"ignore":true},{"start":{"row":139,"column":47},"end":{"row":139,"column":65},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "],"id":625,"ignore":true},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["# "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":2},"action":"insert","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":2},"action":"insert","lines":["# "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["# "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["# "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["# "]},{"start":{"row":82,"column":0},"end":{"row":82,"column":2},"action":"insert","lines":["# "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":2},"action":"insert","lines":["# "]},{"start":{"row":85,"column":0},"end":{"row":85,"column":2},"action":"insert","lines":["# "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"insert","lines":["# "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":2},"action":"insert","lines":["# "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["# "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"insert","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["# "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"insert","lines":["# "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["# "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":2},"action":"insert","lines":["# "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["# "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["# "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":2},"action":"insert","lines":["# "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["# "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":2},"action":"insert","lines":["# "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["# "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":2},"action":"insert","lines":["# "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["# "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":2},"action":"insert","lines":["# "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":2},"action":"insert","lines":["# "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":2},"action":"insert","lines":["# "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":2},"action":"insert","lines":["# "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":2},"action":"insert","lines":["# "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":2},"action":"insert","lines":["# "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":2},"action":"insert","lines":["# "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":2},"action":"insert","lines":["# "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":2},"action":"insert","lines":["# "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":2},"action":"insert","lines":["# "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":2},"action":"insert","lines":["# "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":2},"action":"insert","lines":["# "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["# "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"insert","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["# "]},{"start":{"row":128,"column":0},"end":{"row":128,"column":2},"action":"insert","lines":["# "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":2},"action":"insert","lines":["# "]},{"start":{"row":130,"column":0},"end":{"row":130,"column":2},"action":"insert","lines":["# "]},{"start":{"row":132,"column":0},"end":{"row":132,"column":2},"action":"insert","lines":["# "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":2},"action":"insert","lines":["# "]},{"start":{"row":135,"column":0},"end":{"row":135,"column":2},"action":"insert","lines":["# "]},{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["# "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["# "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":2},"action":"insert","lines":["# "]},{"start":{"row":139,"column":0},"end":{"row":139,"column":2},"action":"insert","lines":["# "]},{"start":{"row":140,"column":0},"end":{"row":140,"column":2},"action":"insert","lines":["# "]},{"start":{"row":141,"column":0},"end":{"row":141,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":142,"column":88},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":626,"ignore":true}],[{"start":{"row":143,"column":0},"end":{"row":217,"column":0},"action":"insert","lines":["import os","import boto3","from flask import Flask, render_template, request","","app = Flask(__name__)","","# S3 bucket configuration","S3_BUCKET_REGION = 'your_bucket_region'","S3_ACCESS_KEY = 'your_access_key'","S3_SECRET_ACCESS_KEY = 'your_secret_access_key'","S3_BUCKET_NAME = 'your_bucket_name'","S3_DIRECTORY_PREFIX = 'mojji-output-img'","","# S3 client creation","s3 = boto3.client(","    service_name=\"s3\",","    region_name=S3_BUCKET_REGION,","    aws_access_key_id=S3_ACCESS_KEY,","    aws_secret_access_key=S3_SECRET_ACCESS_KEY",")","","def find_directory_with_prefix(bucket_name, prefix):","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter='/')","    for common_prefix in response.get('CommonPrefixes', []):","        directory_path = common_prefix['Prefix']","        return directory_path","    return None","","def get_file_names_from_directory(bucket_name, directory_path):","    file_names = []","    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)","    for obj in response.get('Contents', []):","        file_name = obj['Key'].split('/')[-1]","        file_names.append(file_name)","    return file_names","","@app.route('/user_check', methods=['GET'])","def user_check():","    # Get the value of identifier from the query parameters","    identifier = request.args.get('identifier', '')","    oauth_code = request.args.get('oauth_code', '')","    directory_name_split = request.args.get('directory_name_split', '')","    image_code = request.args.get('code', '')","    ","    prefix = 'after_detection_'","","    # Define the base directory path","    # base_directory = '/home/ubuntu/environment/efs/mojji-output-img/'","    ","    directory_with_prefix = find_directory_with_prefix(S3_BUCKET_NAME, prefix)","","    if directory_with_prefix is None:","        # If the directory with the prefix is not found, handle the error","        return \"Directory with prefix '{}' not found.\".format(prefix)","","    # Construct the full identifier with the directory name","    full_identifier = os.path.join(directory_with_prefix)","","    object_names = get_file_names_from_directory(S3_BUCKET_NAME, full_identifier)","","    # You can use the code to generate the S3 URL for the uploaded image","    result_url = s3.generate_presigned_url(","        'get_object',","        Params={'Bucket': \"resultimg\", 'Key': image_code},","        ExpiresIn=3600  # URL's expiration time in seconds","    )","    ","    # Pass the object names, directory name, and identifier to the template","    return render_template('page5.html', code=image_code, object_names=object_names,","                           directory_name=directory_name_split, identifier=identifier,","                           oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier)","","if __name__ == '__main__':","    app.run(debug=True)",""],"id":627,"ignore":true}],[{"start":{"row":216,"column":13},"end":{"row":217,"column":0},"action":"remove","lines":["ebug=True)",""],"id":628,"ignore":true}],[{"start":{"row":214,"column":0},"end":{"row":216,"column":13},"action":"remove","lines":["","if __name__ == '__main__':","    app.run(d"],"id":629,"ignore":true}],[{"start":{"row":143,"column":0},"end":{"row":155,"column":0},"action":"remove","lines":["import os","import boto3","from flask import Flask, render_template, request","","app = Flask(__name__)","","# S3 bucket configuration","S3_BUCKET_REGION = 'your_bucket_region'","S3_ACCESS_KEY = 'your_access_key'","S3_SECRET_ACCESS_KEY = 'your_secret_access_key'","S3_BUCKET_NAME = 'your_bucket_name'","S3_DIRECTORY_PREFIX = 'mojji-output-img'",""],"id":630,"ignore":true}],[{"start":{"row":180,"column":55},"end":{"row":180,"column":69},"action":"remove","lines":["S3_BUCKET_NAME"],"id":631,"ignore":true},{"start":{"row":180,"column":55},"end":{"row":180,"column":73},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":189,"column":49},"end":{"row":189,"column":63},"action":"remove","lines":["S3_BUCKET_NAME"],"id":632,"ignore":true},{"start":{"row":189,"column":49},"end":{"row":189,"column":67},"action":"insert","lines":["'mojji-output-img'"]}],[{"start":{"row":202,"column":0},"end":{"row":250,"column":0},"action":"insert","lines":["","# @app.route('/user_check', methods=['GET'])","# def user_check():","#     # Get the value of identifier from the query parameters","#     identifier = request.args.get('identifier', '')","#     oauth_code = request.args.get('oauth_code', '')","#     directory_name_split = request.args.get('directory_name_split', '')","#     image_code = request.args.get('code', '')","#     file_names = request.args.get('file_names', '')","    ","#     prefix = 'after_detection_'","","#     # Define the base directory path","#     # base_directory = '/home/ubuntu/environment/efs/mojji-output-img/'","    ","#     directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)","","#     if directory_with_prefix is None:","#         # If the directory with the prefix is not found, handle the error","#         return \"Directory with prefix '{}' not found.\".format(prefix)","","#     # Construct the full identifier with the directory name","#     full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)","","#     # full_identifier = os.path.join(base_directory, directory_name_split)","","#     object_names = []  # List to store the object names","    ","#     # Iterate over the files in the directory","#     for file_name in os.listdir(full_identifier):","#         object_names.append(file_name)","        ","#     # You can use the code to generate the S3 URL for the uploaded image","#     s3 = boto3.client(","#         service_name=\"s3\",","#         region_name=S3_BUCKET_REGION,","#         aws_access_key_id=S3_ACCESS_KEY,","#         aws_secret_access_key=S3_SECRET_ACCESS_KEY","#     )","","#     result_url = s3.generate_presigned_url(","#         'get_object',","#         Params={'Bucket': \"resultimg\", 'Key': image_code},","#         ExpiresIn=3600  # URL's expiration time in seconds","#     )","    ","#     # Pass the object names, directory name, and identifier to the template","#     return render_template('page5.html',code=image_code, object_names=object_names, directory_name=directory_name_split, identifier=identifier, oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier, file_names=file_names)",""],"id":633,"ignore":true}],[{"start":{"row":203,"column":0},"end":{"row":203,"column":2},"action":"remove","lines":["# "],"id":634,"ignore":true},{"start":{"row":204,"column":0},"end":{"row":204,"column":2},"action":"remove","lines":["# "]},{"start":{"row":205,"column":0},"end":{"row":205,"column":2},"action":"remove","lines":["# "]},{"start":{"row":206,"column":0},"end":{"row":206,"column":2},"action":"remove","lines":["# "]},{"start":{"row":207,"column":0},"end":{"row":207,"column":2},"action":"remove","lines":["# "]},{"start":{"row":208,"column":0},"end":{"row":208,"column":2},"action":"remove","lines":["# "]},{"start":{"row":209,"column":0},"end":{"row":209,"column":2},"action":"remove","lines":["# "]},{"start":{"row":210,"column":0},"end":{"row":210,"column":2},"action":"remove","lines":["# "]},{"start":{"row":212,"column":0},"end":{"row":212,"column":2},"action":"remove","lines":["# "]},{"start":{"row":214,"column":0},"end":{"row":214,"column":2},"action":"remove","lines":["# "]},{"start":{"row":215,"column":0},"end":{"row":215,"column":2},"action":"remove","lines":["# "]},{"start":{"row":217,"column":0},"end":{"row":217,"column":2},"action":"remove","lines":["# "]},{"start":{"row":219,"column":0},"end":{"row":219,"column":2},"action":"remove","lines":["# "]},{"start":{"row":220,"column":0},"end":{"row":220,"column":2},"action":"remove","lines":["# "]},{"start":{"row":221,"column":0},"end":{"row":221,"column":2},"action":"remove","lines":["# "]},{"start":{"row":223,"column":0},"end":{"row":223,"column":2},"action":"remove","lines":["# "]},{"start":{"row":224,"column":0},"end":{"row":224,"column":2},"action":"remove","lines":["# "]},{"start":{"row":226,"column":0},"end":{"row":226,"column":2},"action":"remove","lines":["# "]},{"start":{"row":228,"column":0},"end":{"row":228,"column":2},"action":"remove","lines":["# "]},{"start":{"row":230,"column":0},"end":{"row":230,"column":2},"action":"remove","lines":["# "]},{"start":{"row":231,"column":0},"end":{"row":231,"column":2},"action":"remove","lines":["# "]},{"start":{"row":232,"column":0},"end":{"row":232,"column":2},"action":"remove","lines":["# "]},{"start":{"row":234,"column":0},"end":{"row":234,"column":2},"action":"remove","lines":["# "]},{"start":{"row":235,"column":0},"end":{"row":235,"column":2},"action":"remove","lines":["# "]},{"start":{"row":236,"column":0},"end":{"row":236,"column":2},"action":"remove","lines":["# "]},{"start":{"row":237,"column":0},"end":{"row":237,"column":2},"action":"remove","lines":["# "]},{"start":{"row":238,"column":0},"end":{"row":238,"column":2},"action":"remove","lines":["# "]},{"start":{"row":239,"column":0},"end":{"row":239,"column":2},"action":"remove","lines":["# "]},{"start":{"row":240,"column":0},"end":{"row":240,"column":2},"action":"remove","lines":["# "]},{"start":{"row":242,"column":0},"end":{"row":242,"column":2},"action":"remove","lines":["# "]},{"start":{"row":243,"column":0},"end":{"row":243,"column":2},"action":"remove","lines":["# "]},{"start":{"row":244,"column":0},"end":{"row":244,"column":2},"action":"remove","lines":["# "]},{"start":{"row":245,"column":0},"end":{"row":245,"column":2},"action":"remove","lines":["# "]},{"start":{"row":246,"column":0},"end":{"row":246,"column":2},"action":"remove","lines":["# "]},{"start":{"row":248,"column":0},"end":{"row":248,"column":2},"action":"remove","lines":["# "]},{"start":{"row":249,"column":0},"end":{"row":249,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":203,"column":0},"end":{"row":222,"column":0},"action":"remove","lines":["@app.route('/user_check', methods=['GET'])","def user_check():","    # Get the value of identifier from the query parameters","    identifier = request.args.get('identifier', '')","    oauth_code = request.args.get('oauth_code', '')","    directory_name_split = request.args.get('directory_name_split', '')","    image_code = request.args.get('code', '')","    file_names = request.args.get('file_names', '')","    ","    prefix = 'after_detection_'","","    # Define the base directory path","    # base_directory = '/home/ubuntu/environment/efs/mojji-output-img/'","    ","    directory_with_prefix = find_directory_with_prefix('/home/ubuntu/environment/efs/mojji-output-img/', prefix)","","    if directory_with_prefix is None:","        # If the directory with the prefix is not found, handle the error","        return \"Directory with prefix '{}' not found.\".format(prefix)",""],"id":635,"ignore":true}],[{"start":{"row":202,"column":0},"end":{"row":203,"column":0},"action":"remove","lines":["",""],"id":636,"ignore":true}],[{"start":{"row":213,"column":0},"end":{"row":230,"column":0},"action":"remove","lines":["        ","    # You can use the code to generate the S3 URL for the uploaded image","    s3 = boto3.client(","        service_name=\"s3\",","        region_name=S3_BUCKET_REGION,","        aws_access_key_id=S3_ACCESS_KEY,","        aws_secret_access_key=S3_SECRET_ACCESS_KEY","    )","","    result_url = s3.generate_presigned_url(","        'get_object',","        Params={'Bucket': \"resultimg\", 'Key': image_code},","        ExpiresIn=3600  # URL's expiration time in seconds","    )","    ","    # Pass the object names, directory name, and identifier to the template","    return render_template('page5.html',code=image_code, object_names=object_names, directory_name=directory_name_split, identifier=identifier, oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier, file_names=file_names)",""],"id":637,"ignore":true}],[{"start":{"row":203,"column":0},"end":{"row":212,"column":38},"action":"remove","lines":["    # Construct the full identifier with the directory name","    full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)","","    # full_identifier = os.path.join(base_directory, directory_name_split)","","    object_names = []  # List to store the object names","    ","    # Iterate over the files in the directory","    for file_name in os.listdir(full_identifier):","        object_names.append(file_name)"],"id":638,"ignore":true}],[{"start":{"row":201,"column":105},"end":{"row":203,"column":0},"action":"remove","lines":["","",""],"id":639,"ignore":true}],[{"start":{"row":184,"column":69},"end":{"row":185,"column":8},"action":"insert","lines":["","        "],"id":640,"ignore":true}],[{"start":{"row":185,"column":8},"end":{"row":195,"column":38},"action":"insert","lines":["","        # Construct the full identifier with the directory name","    full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)","","    # full_identifier = os.path.join(base_directory, directory_name_split)","","    object_names = []  # List to store the object names","    ","    # Iterate over the files in the directory","    for file_name in os.listdir(full_identifier):","        object_names.append(file_name)"],"id":641,"ignore":true}],[{"start":{"row":186,"column":0},"end":{"row":186,"column":4},"action":"remove","lines":["    "],"id":642,"ignore":true}],[{"start":{"row":186,"column":0},"end":{"row":196,"column":0},"action":"remove","lines":["    # Construct the full identifier with the directory name","    full_identifier = os.path.join('/home/ubuntu/environment/efs/mojji-output-img/', directory_with_prefix)","","    # full_identifier = os.path.join(base_directory, directory_name_split)","","    object_names = []  # List to store the object names","    ","    # Iterate over the files in the directory","    for file_name in os.listdir(full_identifier):","        object_names.append(file_name)",""],"id":643,"ignore":true}],[{"start":{"row":185,"column":8},"end":{"row":186,"column":0},"action":"remove","lines":["",""],"id":644,"ignore":true}],[{"start":{"row":187,"column":35},"end":{"row":187,"column":56},"action":"remove","lines":["directory_with_prefix"],"id":645,"ignore":true},{"start":{"row":187,"column":35},"end":{"row":187,"column":55},"action":"insert","lines":["directory_name_split"]}],[{"start":{"row":187,"column":56},"end":{"row":188,"column":19},"action":"insert","lines":["","    full_identifier"],"id":646,"ignore":true}],[{"start":{"row":188,"column":10},"end":{"row":188,"column":19},"action":"remove","lines":["dentifier"],"id":647,"ignore":true}],[{"start":{"row":188,"column":9},"end":{"row":188,"column":10},"action":"remove","lines":["i"],"id":648,"ignore":true}],[{"start":{"row":188,"column":9},"end":{"row":188,"column":10},"action":"insert","lines":["d"],"id":649,"ignore":true}],[{"start":{"row":188,"column":9},"end":{"row":188,"column":10},"action":"remove","lines":["d"],"id":650,"ignore":true},{"start":{"row":188,"column":9},"end":{"row":188,"column":10},"action":"insert","lines":["d"]}],[{"start":{"row":188,"column":10},"end":{"row":188,"column":11},"action":"insert","lines":["i"],"id":651,"ignore":true}],[{"start":{"row":188,"column":11},"end":{"row":188,"column":12},"action":"insert","lines":["r"],"id":652,"ignore":true}],[{"start":{"row":188,"column":12},"end":{"row":188,"column":13},"action":"insert","lines":["e"],"id":653,"ignore":true}],[{"start":{"row":188,"column":13},"end":{"row":188,"column":14},"action":"insert","lines":["c"],"id":654,"ignore":true}],[{"start":{"row":188,"column":14},"end":{"row":188,"column":15},"action":"insert","lines":["t"],"id":655,"ignore":true}],[{"start":{"row":188,"column":15},"end":{"row":188,"column":16},"action":"insert","lines":["o"],"id":656,"ignore":true}],[{"start":{"row":188,"column":16},"end":{"row":188,"column":17},"action":"insert","lines":["r"],"id":657,"ignore":true}],[{"start":{"row":188,"column":17},"end":{"row":188,"column":18},"action":"insert","lines":["y"],"id":658,"ignore":true}],[{"start":{"row":188,"column":18},"end":{"row":188,"column":20},"action":"insert","lines":[" ="],"id":659,"ignore":true}],[{"start":{"row":188,"column":20},"end":{"row":188,"column":21},"action":"insert","lines":[" "],"id":660,"ignore":true}],[{"start":{"row":188,"column":21},"end":{"row":188,"column":22},"action":"insert","lines":["p"],"id":661,"ignore":true}],[{"start":{"row":188,"column":22},"end":{"row":188,"column":23},"action":"insert","lines":["r"],"id":662,"ignore":true}],[{"start":{"row":188,"column":23},"end":{"row":188,"column":25},"action":"insert","lines":["ef"],"id":663,"ignore":true}],[{"start":{"row":188,"column":25},"end":{"row":188,"column":26},"action":"insert","lines":["i"],"id":664,"ignore":true}],[{"start":{"row":188,"column":26},"end":{"row":188,"column":27},"action":"insert","lines":["x"],"id":665,"ignore":true}],[{"start":{"row":188,"column":27},"end":{"row":188,"column":28},"action":"insert","lines":[" "],"id":666,"ignore":true}],[{"start":{"row":188,"column":28},"end":{"row":188,"column":45},"action":"insert","lines":["+ full_identifier"],"id":667,"ignore":true}],[{"start":{"row":190,"column":69},"end":{"row":190,"column":84},"action":"remove","lines":["full_identifier"],"id":668,"ignore":true},{"start":{"row":190,"column":69},"end":{"row":190,"column":83},"action":"insert","lines":["full_directory"]}],[{"start":{"row":202,"column":104},"end":{"row":202,"column":105},"action":"insert","lines":[","],"id":669,"ignore":true}],[{"start":{"row":202,"column":105},"end":{"row":202,"column":121},"action":"insert","lines":[" full_directory="],"id":670,"ignore":true}],[{"start":{"row":202,"column":121},"end":{"row":202,"column":135},"action":"insert","lines":["full_directory"],"id":671,"ignore":true}],[{"start":{"row":203,"column":0},"end":{"row":205,"column":0},"action":"insert","lines":["","",""],"id":672,"ignore":true}],[{"start":{"row":204,"column":0},"end":{"row":213,"column":0},"action":"insert","lines":["def map_korean_to_english(category):","    if category in [\"short_sleeved_shirt\", \"long_sleeved_shirt\", \"vest\", \"sling\"]:","        return \"top\"","    elif category in [\"shorts\", \"trousers\", \"skirt\"]:","        return \"bottom\"","    elif category in [\"short_sleeved_outwear\", \"long_sleeved_outwear\"]:","        return \"outwear\"","    else:","        return \"dress\"",""],"id":673,"ignore":true}],[{"start":{"row":213,"column":0},"end":{"row":223,"column":0},"action":"insert","lines":["","def map_english_to_string(english_category):","    if english_category == \"top\":","        return \"상 의\"","    elif english_category == \"bottom\":","        return \"하 의\"","    elif english_category == \"outwear\":","        return \"아우터\"","    else:","        return \"드레스\"",""],"id":674,"ignore":true}],[{"start":{"row":223,"column":0},"end":{"row":224,"column":0},"action":"insert","lines":["",""],"id":675,"ignore":true}],[{"start":{"row":222,"column":20},"end":{"row":224,"column":0},"action":"remove","lines":["","",""],"id":676,"ignore":true}],[{"start":{"row":199,"column":0},"end":{"row":203,"column":0},"action":"remove","lines":["    # Pass the object names, directory name, and identifier to the template","    return render_template('page5.html', code=image_code, object_names=object_names,","                           directory_name=directory_name_split, identifier=identifier,","                           oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier, full_directory=full_directory)",""],"id":677,"ignore":true}],[{"start":{"row":199,"column":0},"end":{"row":214,"column":0},"action":"insert","lines":["@app.route('/user_check', methods=['GET'])","def user_check():","    # ... (your existing code)","","    # Mapping Korean categories to English categories for each file_name","    english_categories = [map_korean_to_english(file_name) for file_name in object_names]","","    # Mapping English categories to Korean strings for each English category","    korean_strings = [map_english_to_string(english_category) for english_category in english_categories]","","    # Pass the object names, directory name, and identifier to the template","    return render_template('page5.html', code=image_code, object_names=object_names,","                           directory_name=directory_name_split, identifier=identifier,","                           oauth_code=oauth_code, result_url=result_url, full_identifier=full_identifier,","                           english_categories=english_categories, korean_strings=korean_strings)",""],"id":678,"ignore":true}],[{"start":{"row":198,"column":4},"end":{"row":202,"column":0},"action":"remove","lines":["","@app.route('/user_check', methods=['GET'])","def user_check():","    # ... (your existing code)",""],"id":679,"ignore":true}],[{"start":{"row":197,"column":5},"end":{"row":203,"column":5},"action":"insert","lines":["","    ","        result_url = s3.generate_presigned_url(","        'get_object',","        Params={'Bucket': \"resultimg\", 'Key': image_code},","        ExpiresIn=3600  # URL's expiration time in seconds","    )"],"id":680,"ignore":true}],[{"start":{"row":199,"column":47},"end":{"row":202,"column":58},"action":"remove","lines":["","        'get_object',","        Params={'Bucket': \"resultimg\", 'Key': image_code},","        ExpiresIn=3600  # URL's expiration time in seconds"],"id":681,"ignore":true},{"start":{"row":199,"column":47},"end":{"row":200,"column":1},"action":"insert","lines":["","ㅋ"]}],[{"start":{"row":200,"column":0},"end":{"row":200,"column":1},"action":"remove","lines":["ㅋ"],"id":682,"ignore":true},{"start":{"row":200,"column":0},"end":{"row":200,"column":2},"action":"insert","lines":["ㅋㅋ"]}],[{"start":{"row":200,"column":2},"end":{"row":200,"column":3},"action":"insert","lines":["ㅋ"],"id":683,"ignore":true}],[{"start":{"row":200,"column":3},"end":{"row":200,"column":4},"action":"insert","lines":["ㅋ"],"id":684,"ignore":true}],[{"start":{"row":199,"column":4},"end":{"row":201,"column":5},"action":"remove","lines":["    result_url = s3.generate_presigned_url(","ㅋㅋㅋㅋ","    )"],"id":685,"ignore":true}],[{"start":{"row":199,"column":4},"end":{"row":203,"column":5},"action":"insert","lines":["    result_url = s3.generate_presigned_url(","        'get_object',","        Params={'Bucket': \"resultimg\", 'Key': image_code},","        ExpiresIn=3600  # URL's expiration time in seconds","    )"],"id":686,"ignore":true}],[{"start":{"row":199,"column":0},"end":{"row":199,"column":4},"action":"remove","lines":["    "],"id":687,"ignore":true},{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"remove","lines":["    "]},{"start":{"row":201,"column":0},"end":{"row":201,"column":4},"action":"remove","lines":["    "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":201,"column":23},"end":{"row":201,"column":32},"action":"remove","lines":["resultimg"],"id":688,"ignore":true},{"start":{"row":201,"column":23},"end":{"row":201,"column":39},"action":"insert","lines":["mojji-output-img"]}],[{"start":{"row":201,"column":49},"end":{"row":201,"column":50},"action":"insert","lines":["p"],"id":689,"ignore":true}],[{"start":{"row":201,"column":50},"end":{"row":201,"column":51},"action":"insert","lines":["r"],"id":690,"ignore":true}],[{"start":{"row":201,"column":51},"end":{"row":201,"column":52},"action":"insert","lines":["e"],"id":691,"ignore":true}],[{"start":{"row":201,"column":52},"end":{"row":201,"column":53},"action":"insert","lines":["f"],"id":692,"ignore":true}],[{"start":{"row":201,"column":53},"end":{"row":201,"column":54},"action":"insert","lines":["i"],"id":693,"ignore":true}],[{"start":{"row":201,"column":54},"end":{"row":201,"column":55},"action":"insert","lines":["x"],"id":694,"ignore":true}],[{"start":{"row":201,"column":55},"end":{"row":201,"column":56},"action":"insert","lines":["|"],"id":695,"ignore":true}],[{"start":{"row":201,"column":55},"end":{"row":201,"column":56},"action":"remove","lines":["|"],"id":696,"ignore":true},{"start":{"row":201,"column":55},"end":{"row":201,"column":56},"action":"insert","lines":["+"]}],[{"start":{"row":199,"column":8},"end":{"row":199,"column":10},"action":"remove","lines":["lt"],"id":697,"ignore":true}],[{"start":{"row":199,"column":4},"end":{"row":199,"column":8},"action":"remove","lines":["resu"],"id":698,"ignore":true},{"start":{"row":199,"column":4},"end":{"row":199,"column":10},"action":"insert","lines":["output"]}],[{"start":{"row":215,"column":95},"end":{"row":215,"column":96},"action":"insert","lines":[","],"id":699,"ignore":true}],[{"start":{"row":215,"column":96},"end":{"row":215,"column":108},"action":"insert","lines":[" output_url="],"id":700,"ignore":true}],[{"start":{"row":215,"column":108},"end":{"row":215,"column":118},"action":"insert","lines":["output_url"],"id":701,"ignore":true}],[{"start":{"row":215,"column":102},"end":{"row":215,"column":118},"action":"remove","lines":["t_url=output_url"],"id":702,"ignore":true}],[{"start":{"row":215,"column":95},"end":{"row":215,"column":102},"action":"remove","lines":[", outpu"],"id":703,"ignore":true}],[{"start":{"row":215,"column":94},"end":{"row":215,"column":95},"action":"remove","lines":["s"],"id":704,"ignore":true}],[{"start":{"row":215,"column":94},"end":{"row":215,"column":118},"action":"insert","lines":["s, output_url=output_url"],"id":705,"ignore":true}],[{"start":{"row":215,"column":112},"end":{"row":215,"column":118},"action":"remove","lines":["ut_url"],"id":706,"ignore":true}],[{"start":{"row":215,"column":97},"end":{"row":215,"column":112},"action":"remove","lines":["output_url=outp"],"id":707,"ignore":true}],[{"start":{"row":215,"column":95},"end":{"row":215,"column":97},"action":"remove","lines":[", "],"id":708,"ignore":true}],[{"start":{"row":198,"column":0},"end":{"row":203,"column":5},"action":"remove","lines":["    ","    output_url = s3.generate_presigned_url(","    'get_object',","    Params={'Bucket': \"mojji-output-img\", 'Key': prefix+image_code},","    ExpiresIn=3600  # URL's expiration time in seconds","    )"],"id":709,"ignore":true}],[{"start":{"row":197,"column":5},"end":{"row":198,"column":0},"action":"remove","lines":["",""],"id":710,"ignore":true}],[{"start":{"row":961,"column":0},"end":{"row":961,"column":2},"action":"insert","lines":["# "],"id":712},{"start":{"row":962,"column":0},"end":{"row":962,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":962,"column":0},"end":{"row":962,"column":2},"action":"remove","lines":["# "],"id":713}],[{"start":{"row":961,"column":0},"end":{"row":961,"column":2},"action":"remove","lines":["# "],"id":714}]]},"ace":{"folds":[],"scrolltop":13296.5,"scrollleft":0,"selection":{"start":{"row":962,"column":50},"end":{"row":962,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1690168153835,"hash":"93ae39fc6fee379032cec1bc52157e3216644d7c"}