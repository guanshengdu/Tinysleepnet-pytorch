import torch
import torch.nn as nn

# Simple test model
class TestModel(nn.Module):
    def __init__(self):
        super(TestModel, self).__init__()
        self.fc = nn.Linear(10, 10)

    def forward(self, x):
        return self.fc(x)

# Instantiate the model and move it to the GPU
model = TestModel().to('cuda' if torch.cuda.is_available() else 'cpu')

# Create some dummy input and pass it through the model
x = torch.randn(5, 10).to('cuda' if torch.cuda.is_available() else 'cpu')
output = model(x)
print(output)
