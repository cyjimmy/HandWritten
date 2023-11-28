from transformers import AutoTokenizer, TrOCRProcessor, VisionEncoderDecoderModel

MODEL_NAME = "microsoft/trocr-base-handwritten"
# Download and save the pre-trained model
TrOCRProcessor.from_pretrained(MODEL_NAME).save_pretrained('./handwrittenmodel')
VisionEncoderDecoderModel.from_pretrained(MODEL_NAME).save_pretrained('./handwrittenmodel')
# Download and save the tokenizer
AutoTokenizer.from_pretrained(MODEL_NAME).save_pretrained("./handwrittenmodel")
print("Model and tokenizer downloaded successfully!")