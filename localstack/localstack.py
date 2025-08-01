# import subprocess, time


# subprocess.run(["docker-compose", "up", "-d"], cwd="/home/test/demo-1/localstack")


# time.sleep(30)


# subprocess.run([
#     "awslocal", "--endpoint-url=http://localhost:4566", "s3api", "create-bucket", 
#     "--bucket", "notes-bucket"
# ])


# subprocess.run([
#     "awslocal", "--endpoint-url=http://localhost:4566", "lambda", "create-function",
#     "--function-name", "notesHandler", 
#     "--runtime", "python3.10",
#     "--handler", "handler.main",
#     "--zip-file", "fileb://function.zip",
#     "--role", "arn:aws:iam::123456789012:role/lambda"
# ])


# print("Deployed")





import subprocess
import time
import os

# Lấy chính xác thư mục đang chứa file này:
compose_dir = os.path.dirname(os.path.abspath(__file__))

# 1) Nếu bạn vẫn muốn dùng docker-compose:
subprocess.run(
    ["docker-compose", "up", "-d"],
    cwd=compose_dir,
    check=True
)

# Chờ LocalStack khởi động (bạn có thể điều chỉnh thời gian hoặc dùng health-check)
time.sleep(30)

# 2) Deploy S3 bucket
subprocess.run([
    "awslocal", "--endpoint-url=http://localhost:4566", "s3api", "create-bucket",
    "--bucket", "notes-bucket"
], check=True)

# 3) Deploy Lambda
subprocess.run([
    "awslocal", "--endpoint-url=http://localhost:4566", "lambda", "create-function",
    "--function-name", "notesHandler",
    "--runtime", "python3.10",
    "--handler", "handler.main",
    "--zip-file", "fileb://function.zip",
    "--role", "arn:aws:iam::123456789012:role/lambda"
], check=True)
