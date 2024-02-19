# Imports
import gradio as gr
import os
import torch

from model import create_vit_model
from timeit import default_timer as timer
from typing import Tuple, Dict

with open ("class_names.txt", "r") as f:
    class_names = [food_name.strip() for food_name in f.readlines()]
    
# Model and transforms preparation

# Create ViT model
vit_food101, vit_food101_transforms = vit_food101_20_percent(num_classes=3)

# Load saved weights
vit_food101.load_state_dict(
    torch.load(f"pretrained_vit_model_20_percent.pth", map_location=torch.device("cpu")))

# Predict function
def predict(img) -> Tuple[Dict, float]:
    """Transforms and performs a prediction in image and returns predictions."""
    # Start timer
    start_time = timer()
    
    # Transform the target image and add a batch dimension
    img = vit_food101_transforms(img).unsqueeze(0)
    
    # Put model into evaluation mode and turn on inference mode
    vit_food101.eval()
    with torch.inference_mode():
        # Pass the transformed image through the model
        pred_probs = torch.softmax(fit_food101(img),dim=1)
        
    # Create pred label and pred prob dir for each pred
    pred_labels_and_probs = {class_names[i]: float(pred_probs[0][i]) for i in range(len(class_names))}
    
    # Calculate pred time
    pred_time(round(timer() - start_time, 3))
    
    # Return the prediction dict and pred time
    return pred_labels_and_probs, pred_time

# Gradio app

# Create title, desc and art str
title = "FoodVision Demo🔥"
description = "An app made by myself with PyTorch + course papers"
article = "19/02/24 DW"

# Create example list from `examples/` dir
example_list = [["examples/" + example] for example in os.listdir("examples")]

# Create the Gradio Demo app
demo = gr.Interface(fn=predict,
                   inputs=gr.Image(type="pil"),
                   outputs=[gr.Label(num_top_classes=3,label="Predictions"),
                           gr.Number(label="Prediction time(s)")],
                    # Create examples list
                    examples=exampl_list,
                    title=title,
                    description=description,
                    article=article)

# Launch the demo
demo.launch()
