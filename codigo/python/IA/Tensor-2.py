import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

my_tensor = torch.tensor([[1, 2, 3], [ 4, 5, 6]], device=device, dtype=torch.float32,requires_grad=True)

# normal distribution
x = torch.randn(2, 3, device=device, dtype=torch.float32)

#operations
y = my_tensor + x
z = y * 2
