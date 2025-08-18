[![CI](https://github.com/Hmm-09876/demo-1/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmm-09876/demo-1/actions)

# Mục tiêu demo-1
1. Hiểu cách dùng Git và GitHub

2. Biết cách tạo các script để sinh tự động cấu trúc dự án

3. Hiểu CRUD cơ bản trong ứng dụng web/API

4. Biết cách kiểm thử sản phẩm bằng Pytest

5. Hiểu rõ hơn về CI
***
# Những gì cần cài ban đầu
```
ssh-keygen -t ed25519 -C "your_email@example.com"
apt install git zip
apt install build-essential python3-dev libyaml-dev
install python3 python3-venv python3-pip
apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
***
# Cấu hình thông tin người dùng cho git

`git config --global user.name "Your Name"`

`git config --global user.email "you@example.com"`
***
# Sử dụng và test nhanh
```
git clone https://github.com/Hmm-09876/demo-1.git
cd demo-1/localstack
```

`docker compose up -d`

```
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
pytest
```



