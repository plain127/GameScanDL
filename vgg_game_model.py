import torch
import torch.nn as nn
from torchvision.models.vgg import vgg16

class VggGameModel(nn.Module):
    def __init__(self, num_classes):
        super(VggGameModel, self).__init__()
        self.num_classes = num_classes
        self.vgg = vgg16(pretrained=True)
    
    def forward(self, x):
        self.vgg.classifier = nn.Sequential(
            nn.Linear(25088, 4096),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(4096, self.num_classes)
        )
        
        return self.vgg(x)
    
