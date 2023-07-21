#!/bin/bash

# 디렉토리 경로 설정
efs_dir="/home/ubuntu/environment/efs/coai-original-images"
target_ip="ip-172-31-58-31"
target_username="ubuntu"
target_directory="/home/ubuntu/environment/scp"

# inotifywait로 디렉토리 감지 및 처리
inotifywait -m -e create,move -r --format "%w%f" "$efs_dir" |
while read -r file; do
    # 파일 처리 로직을 여기에 작성
    echo "New image detected: $file"
    
    # 이미지 파일을 Target EC2 인스턴스로 전송
    scp -i /home/ubuntu/.ssh/Mojji-key.pem "$file" "$target_username@$target_ip:$target_directory"
    
    # 전송 완료 후 파일 삭제 (선택적)
    # rm "$file"
    
    echo "Image transferred: $file"
done &