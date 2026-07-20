# Pleadly Docker 镜像
FROM python:3.11-slim

WORKDIR /app

# 系统依赖
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python 依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 应用代码
COPY . .

# Hugging Face Spaces 需要 Gradio 监听 0.0.0.0:7860
EXPOSE 7860

CMD ["python", "app/main.py"]
