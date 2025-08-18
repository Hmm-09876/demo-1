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



#########################################################################################

# import subprocess
# import time
# import os

# compose_dir = os.path.dirname(os.path.abspath(__file__))

# subprocess.run(
#     ["docker-compose", "up", "-d"],
#     cwd=compose_dir,
#     check=True
# )

# time.sleep(30)

# subprocess.run([
#     "awslocal", "--endpoint-url=http://localhost:4566", "s3api", "create-bucket",
#     "--bucket", "notes-bucket"
# ], check=True)

# subprocess.run([
#     "awslocal", "--endpoint-url=http://localhost:4566", "lambda", "create-function",
#     "--function-name", "notesHandler",
#     "--runtime", "python3.10",
#     "--handler", "handler.main",
#     "--zip-file", "fileb://function.zip",
#     "--role", "arn:aws:iam::123456789012:role/lambda"
# ], check=True)




import subprocess
import time
import os

compose_dir = os.path.dirname(os.path.abspath(__file__))



time.sleep(30)

subprocess.run([
    "awslocal", "--endpoint-url=http://localhost:4566", "s3api", "create-bucket",
    "--bucket", "notes-bucket"
], check=True)


subprocess.run([
    "awslocal", "--endpoint-url=http://localhost:4566", "lambda", "create-function",
    "--function-name", "notesHandler",
    "--runtime", "python3.10",
    "--handler", "handler.main",
    "--zip-file", f"fileb://{os.path.join(compose_dir, 'function.zip')}",
    "--role", "arn:aws:iam::123456789012:role/lambda"
], check=True)
