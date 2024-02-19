import torch
import torchvision

from torch import nn

def create_vit_model(num_classes:int=3,
                    seed:int=42):
    """Creates an feature extractor model and transforms"""
    
    # Create weights, transforms and model
    weights = torchvision.models.ViT_B_16_Weights.DEFAULT
    transforms = weights.transforms()
    model = torchvision.models.vit_b_16(weights=weights)
    
    # Freeze all layers in model
    for param in model.parameters():
        param.requires_grad = False
        
    # Change classifier head to suit needs
    torch.manual_seed(seed)
    model.heads = nn.Sequential(nn.Linear(in_features=768,
                                         out_features=num_classes))
    
    return model, transform
