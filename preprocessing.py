import torch
from torchvision import transforms, datasets
from torchvision.transforms import Compose, ToTensor, Resize, RandomHorizontalFlip, Normalize
from torch.utils.data.dataloader import DataLoader

class Preprocessing:
    def __init__(self, train_path, test_path, batch_size):
        self.train_path = train_path
        self.test_path = test_path
        self.batch_size = batch_size
        
    def transform_train(self):
        transform_train = transforms.Compose(
            [
                transforms.Resize((224,224)),
                transforms.RandomHorizontalFlip(p=0.5),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
            ]
        )
        
        return transform_train
    
    def transform_test(self):
        transform_test = transforms.Compose(
            [
                transforms.Resize((224,224)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
            ]
        )
        
        return transform_test
    
    def train_dataset_load(self):
        train_dataset = datasets.ImageFolder(root=self.train_path, transform=self.transform_train())
        return train_dataset
    
    def test_dataset_load(self):
        test_dataset = datasets.ImageFolder(root=self.test_path, transform=self.transform_test())
        return test_dataset
    
    def train_dataloader_load(self):
        train_dataloader = DataLoader(self.train_dataset_load(), batch_size=self.batch_size, shuffle=True)
        return train_dataloader
    
    def test_dataloader_load(self):
        test_dataloader = DataLoader(self.test_dataset_load(), batch_size=self.batch_size, shuffle=True)
        return test_dataloader
    
    def run_train_preprocess(self):
        data, target = next(iter(self.train_dataloader_load()))
        
        return data, target
        