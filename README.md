# Handwritten Text Recognition Model Hosting

## Instructions:

### 1. **Download model:**
Execute the "download_model.py" script to download the required model.

### 2. **Create Docker Image:**
Build the Docker image for the project.

```bash
docker build -t your-docker-image-name .
```

### 3. **Create ECR Repository:**
```bash
aws ecr create-repository --repository-name your-repository-name
```

### 4. **Tag the Docker Image:**
```bash
docker tag your-docker-image-name:latest your-ecr-repository-uri/your-repository-name:latest
```

### 5. **Push the Docker Image to ECR:**
```bash
docker push your-ecr-repository-uri/your-repository-name:latest
```

### 6. **Create AWS Lambda Function Using Image:**
Set up an AWS Lambda function using the Docker image.

### 7. **Create Lambda Function URL:**
Create URL for the Lambda function.
