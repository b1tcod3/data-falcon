from torch.utils.data import DataLoader
from dataset import CustomCSCDataset

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"

dataset = CustomCSCDataset(url)

BATCH_SIZE = 32

train_loader = DataLoader(
    dataset=dataset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=4
)


