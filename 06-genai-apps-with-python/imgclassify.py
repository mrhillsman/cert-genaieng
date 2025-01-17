import torch, requests
from PIL import Image
from torchvision import transforms
import gradio as gr

model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()

response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")

def predict(inp):
    """
    The function converts the input image into a PIL Image and subsequently into a PyTorch tensor.
    After processing the tensor through the model, it returns the predictions in the form of a dictionary
    named confidences. The dictionary's keys are the class labels, and its values are the
    corresponding confidence probabilities.
    """
    inp = transforms.ToTensor()(inp).unsqueeze(0) # Convert image to PyTorch tensor
    with torch.no_grad():
        # Pass the tensor through the model
        # and use softmax to get the probabilities
        # softmax normalizes the values to sum up to 1
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
    return confidences

# inputs=gr.Image(type="pil") handles pre-processing and conversion to PIL
gr.Interface(fn=predict, inputs=gr.Image(type="pil"), outputs=gr.Label(num_top_classes=3),
             examples=["content/lion.jpg", "content/cheetah.jpg"]).launch()