import io
import torch
from torchvision import transforms
from PIL import Image
from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok  

app = Flask(__name__)
run_with_ngrok(app)
# Load the pre-trained CNN model
model_path = "/content/entire_model1.pt"
model = torch.load(model_path, map_location=torch.device('cpu'))
model.eval()

# Define a transformation for input images
transform = transforms.Compose([transforms.Resize((160, 160)),
                                transforms.ToTensor(),
                                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

# Define a function to make predictions
def predict_image(image):
    img = Image.open(io.BytesIO(image.read()))
    img = transform(img).unsqueeze(0)  # Add a batch dimension
    with torch.no_grad():
        output = model(img)
        xpredicted = (output > 0.5).float()
        _, predicted = output.max(1)
    return _.item()

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        prediction = predict_image(image)
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
