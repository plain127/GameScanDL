import torch
import torch.nn as nn
import torch.optim as optim
import tqdm
import time
from torchvision.models.vgg import vgg16
from vgg_game_model import VggGameModel
from preprocessing import Preprocessing
from sklearn.metrics import precision_recall_fscore_support, confusion_matrix

train_path = './dataset/train/'
test_path = './dataset/test/'
pre = Preprocessing(train_path, test_path, 12)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = VggGameModel(12).forward()
model.to(device)
model.train()

optimizer = optim
criterion = nn.CrossEntropyLoss()
epochs = 50

loss_list = []

for epoch in range(epochs):
    start_time = time.time()

    epoch_loss = 0.0
    num_batchs = 0
    
    for data, target in tqdm.tqdm(pre.run_train_preprocess()):
        optimizer.zero_grad()
        pred = model(data.to(device))
        loss = criterion(pred, target.to(device))
        
        epoch_loss += loss.item()
        num_batchs += 1
        
        loss.backward()
        optimizer.step()
        
    avg_loss =  epoch_loss / num_batchs
    loss_list.append(avg_loss)
    
model.eval()
correct = 0
total = 0

all_preds = []
all_labels = []

with torch.no_grad():
    for img, label in pre.test_dataloader_load():
        img, label = img.to(device), label.to(device)
        pred = model(img)
        result = pred.max(1)[1]
        
        all_preds.extend(result.cpu().numpy())
        all_labels.extend(label.cpu().numpy())
        
        correct += result.eq(label).sum().item()
        total += label.size(0)
        
accuracy = correct / total
precision, recall, f1, _ = precision_recall_fscore_support(all_labels, all_preds, average='weighted')

print(f'Accuracy : {accuracy}')
print(f'Precision : {precision}')
print(f'Recall : {recall}')
print(f'F1 Score : {f1}')

torch.save(model.state_dict(), 'game_shot_model.pth')