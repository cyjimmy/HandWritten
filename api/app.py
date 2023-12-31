import json
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# Load the local model
MODEL_PATH = "./handwrittenmodel" 
processor = TrOCRProcessor.from_pretrained(MODEL_PATH)
model = VisionEncoderDecoderModel.from_pretrained(MODEL_PATH)
model.eval()

def handler(event, context):
    body = json.loads(event['body'])
    url = body['url']
    try:
        # Process image
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values

        # Generate text
        generated_ids = model.generate(pixel_values, max_length=128)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        # Return the response
        response = {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'result': generated_text})
        }
    except Exception as e:
        # Error handling
        response = {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
    return response