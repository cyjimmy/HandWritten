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

### 6. **Create a seperate Lambda Function for authentication:**
Set up a seperate Lambda function using AWS console. Copy and paste the code from authentication.py to the new function.

### 7. **Create Lambda Function URL:**
Create URL for the authentication lambda function. This function will check API key and invoke the processing function if request is authorized.

## Others:
Refer to AWS documentation on how to use docker image to create lambda function.
https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions