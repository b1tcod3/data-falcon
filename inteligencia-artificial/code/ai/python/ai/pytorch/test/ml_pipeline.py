#!/usr/bin/env python3
"""
PyTorch Binary Classifier - Complete ML Pipeline Menu
==================================================

This script provides a menu-driven interface for a complete machine learning pipeline
using PyTorch for binary classification on the Pima Indians Diabetes dataset.

Features:
- Generate new models
- Load existing models
- Train models
- Evaluate models
- Use models for production predictions
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import os
import sys
from pathlib import Path

# ============================================================================
# DATASET CLASS
# ============================================================================

class CustomCSCDataset(Dataset):
    """Custom dataset for loading CSV data and converting to PyTorch tensors."""
    
    def __init__(self, csv_file):
        # Use pandas to read the CSV file
        dataframe = pd.read_csv(csv_file)
        # Convert DataFrame to PyTorch tensors
        # .iloc[:, :-1] selects all rows and all columns except the last one
        X = dataframe.iloc[:, :-1].values
        self.features = torch.tensor(X, dtype=torch.float32)
        
        # Convert labels (Y) to PyTorch tensors
        Y = dataframe.iloc[:, -1].values
        # .unsqueeze(1) adds an extra dimension so labels have the correct shape (N,1)
        self.labels = torch.tensor(Y, dtype=torch.float32).unsqueeze(1)

    def __len__(self):
        # Return the number of samples in the dataset
        return len(self.labels)
    
    def __getitem__(self, idx):
        # Return a sample (features and label) at the given index
        return self.features[idx], self.labels[idx]

# ============================================================================
# MODEL CLASS
# ============================================================================

class SimpleClassifier(nn.Module):
    """Simple neural network for binary classification."""
    
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleClassifier, self).__init__()
        # Input layer to first hidden layer
        self.fc1 = nn.Linear(input_size, hidden_size)
        # First hidden layer to second hidden layer
        self.fc2 = nn.Linear(hidden_size, hidden_size // 2)
        # Second hidden layer to output layer
        self.fc3 = nn.Linear(hidden_size // 2, output_size)
    
    def forward(self, x):
        # Apply first linear layer and ReLU activation
        x = F.relu(self.fc1(x))
        # Apply second linear layer and ReLU activation
        x = F.relu(self.fc2(x))
        # Apply final output layer
        x = self.fc3(x)
        # Apply sigmoid activation to get probabilities
        x = torch.sigmoid(x)
        
        return x

# ============================================================================
# MODEL MANAGER CLASS
# ============================================================================

class ModelManager:
    """Manages model operations including training, evaluation, and inference."""
    
    def __init__(self, model_path='modelo_clasificador_binario.pth'):
        self.model_path = model_path
        self.model = None
        self.dataset = None
        self.train_loader = None
        self.optimizer = None
        self.criterion = None
        self.learning_rate = 0.001
        self.epochs = 100
        self.batch_size = 32
        
    def setup_dataset(self, csv_url=None, local_file=None):
        """Setup the dataset and data loader."""
        try:
            if local_file and os.path.exists(local_file):
                dataset = CustomCSCDataset(local_file)
                print(f"✓ Dataset loaded from local file: {local_file}")
            elif csv_url:
                dataset = CustomCSCDataset(csv_url)
                print(f"✓ Dataset loaded from URL: {csv_url}")
            else:
                # Default to Pima Indians Diabetes dataset
                url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
                dataset = CustomCSCDataset(url)
                print(f"✓ Dataset loaded from default URL: {url}")
            
            self.dataset = dataset
            self.train_loader = DataLoader(
                dataset=dataset,
                batch_size=self.batch_size,
                shuffle=True,
                num_workers=2
            )
            print(f"✓ DataLoader created with {len(dataset)} samples, batch size: {self.batch_size}")
            return True
            
        except Exception as e:
            print(f"✗ Error setting up dataset: {e}")
            return False
    
    def create_model(self, input_size=8, hidden_size=16, output_size=1):
        """Create a new model."""
        try:
            self.model = SimpleClassifier(input_size, hidden_size, output_size)
            print(f"✓ New model created with architecture:")
            print(f"  Input size: {input_size}")
            print(f"  Hidden size: {hidden_size}")
            print(f"  Output size: {output_size}")
            return True
        except Exception as e:
            print(f"✗ Error creating model: {e}")
            return False
    
    def load_model(self):
        """Load an existing model."""
        try:
            if not os.path.exists(self.model_path):
                print(f"✗ Model file not found: {self.model_path}")
                print("  Please create or train a model first.")
                return False
            
            if self.model is None:
                # Create model architecture first
                self.create_model()
            
            # Load the saved state dict
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            self.model.eval()  # Set to evaluation mode
            print(f"✓ Model loaded successfully from: {self.model_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error loading model: {e}")
            return False
    
    def setup_training(self):
        """Setup optimizer and loss function."""
        if self.model is None:
            print("✗ No model available. Please create or load a model first.")
            return False
        
        if self.train_loader is None:
            print("✗ No dataset available. Please setup the dataset first.")
            return False
        
        try:
            self.criterion = nn.BCELoss()
            self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)
            print(f"✓ Training setup completed:")
            print(f"  Learning rate: {self.learning_rate}")
            print(f"  Epochs: {self.epochs}")
            print(f"  Batch size: {self.batch_size}")
            return True
        except Exception as e:
            print(f"✗ Error setting up training: {e}")
            return False
    
    def train_model(self, epochs=None):
        """Train the model."""
        if self.model is None:
            print("✗ No model available. Please create or load a model first.")
            return False
        
        if self.train_loader is None:
            print("✗ No dataset available. Please setup the dataset first.")
            return False
        
        if self.optimizer is None or self.criterion is None:
            if not self.setup_training():
                return False
        
        if epochs is not None:
            self.epochs = epochs
        
        try:
            print(f"\n🚀 Starting training for {self.epochs} epochs...")
            print("-" * 50)
            
            # Training loop
            for epoch in range(self.epochs):
                total_loss = 0
                num_batches = 0
                
                # Iterate over batches
                for batch_idx, (inputs, labels) in enumerate(self.train_loader):
                    # Reset gradients
                    self.optimizer.zero_grad()
                    
                    # Forward pass
                    outputs = self.model(inputs)
                    
                    # Calculate loss
                    loss = self.criterion(outputs, labels)
                    
                    # Backward pass
                    loss.backward()
                    
                    # Update parameters
                    self.optimizer.step()
                    
                    total_loss += loss.item()
                    num_batches += 1
                
                avg_loss = total_loss / num_batches
                print(f'Epoch [{epoch+1}/{self.epochs}], Average Loss: {avg_loss:.4f}')
            
            print("-" * 50)
            print("✓ Training completed successfully!")
            return True
            
        except Exception as e:
            print(f"✗ Error during training: {e}")
            return False
    
    def save_model(self):
        """Save the trained model."""
        if self.model is None:
            print("✗ No model to save. Please create or train a model first.")
            return False
        
        try:
            torch.save(self.model.state_dict(), self.model_path)
            print(f"✓ Model saved successfully as: {self.model_path}")
            return True
        except Exception as e:
            print(f"✗ Error saving model: {e}")
            return False
    
    def evaluate_model(self):
        """Evaluate the model on the dataset."""
        if self.model is None:
            print("✗ No model available. Please create or load a model first.")
            return False
        
        if self.train_loader is None:
            print("✗ No dataset available. Please setup the dataset first.")
            return False
        
        try:
            self.model.eval()  # Set to evaluation mode
            
            all_predictions = []
            all_labels = []
            
            with torch.no_grad():
                for inputs, labels in self.train_loader:
                    # Forward pass
                    outputs = self.model(inputs)
                    
                    # Convert probabilities to binary labels
                    predicted_classes = torch.round(outputs)
                    
                    all_predictions.append(predicted_classes)
                    all_labels.append(labels)
            
            # Calculate accuracy
            pred_tensor = torch.cat(all_predictions)
            label_tensor = torch.cat(all_labels)
            
            correct_predictions = (pred_tensor == label_tensor).float()
            accuracy = correct_predictions.sum() / len(correct_predictions)
            
            print(f"\n📊 Model Evaluation Results:")
            print(f"  Accuracy: {accuracy.item():.4f} ({accuracy.item()*100:.2f}%)")
            print(f"  Correct predictions: {int(correct_predictions.sum())}/{len(correct_predictions)}")
            
            return True
            
        except Exception as e:
            print(f"✗ Error during evaluation: {e}")
            return False
    
    def predict_single(self, features):
        """Make a prediction for a single sample."""
        if self.model is None:
            print("✗ No model available. Please create or load a model first.")
            return None
        
        try:
            self.model.eval()  # Set to evaluation mode
            
            with torch.no_grad():
                if isinstance(features, (list, tuple)):
                    features = torch.tensor([features], dtype=torch.float32)
                elif isinstance(features, np.ndarray):
                    features = torch.tensor([features], dtype=torch.float32)
                
                output = self.model(features)
                probability = output.item()
                prediction = round(probability)
                
                return {
                    'probability': probability,
                    'prediction': int(prediction),
                    'class': 'Positive' if prediction == 1 else 'Negative'
                }
                
        except Exception as e:
            print(f"✗ Error during prediction: {e}")
            return None
    
    def get_dataset_info(self):
        """Display information about the dataset."""
        if self.dataset is None:
            print("✗ No dataset loaded. Please setup the dataset first.")
            return
        
        print(f"\n📊 Dataset Information:")
        print(f"  Total samples: {len(self.dataset)}")
        print(f"  Features shape: {self.dataset.features.shape}")
        print(f"  Labels shape: {self.dataset.labels.shape}")
        
        # Show sample data
        if len(self.dataset) > 0:
            sample_features, sample_label = self.dataset[0]
            print(f"  Sample features: {sample_features[:5].numpy()}...")
            print(f"  Sample label: {sample_label.item()}")
    
    def show_model_architecture(self):
        """Display the model architecture."""
        if self.model is None:
            print("✗ No model available. Please create or load a model first.")
            return
        
        print(f"\n🏗️ Model Architecture:")
        print(self.model)
        
        # Count parameters
        total_params = sum(p.numel() for p in self.model.parameters())
        trainable_params = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        
        print(f"\n📈 Model Statistics:")
        print(f"  Total parameters: {total_params:,}")
        print(f"  Trainable parameters: {trainable_params:,}")

# ============================================================================
# MENU SYSTEM
# ============================================================================

def print_header():
    """Print the application header."""
    print("\n" + "="*60)
    print("🤖 PYTORCH BINARY CLASSIFIER - ML PIPELINE")
    print("="*60)
    print("Dataset: Pima Indians Diabetes (Binary Classification)")
    print("Model: Simple Neural Network (8 → 16 → 8 → 1)")
    print("="*60)

def print_menu():
    """Print the main menu options."""
    print("\n📋 MAIN MENU:")
    print("="*30)
    print("1. 📊 Dataset Management")
    print("2. 🤖 Model Management")
    print("3. 🎯 Training")
    print("4. 📈 Evaluation")
    print("5. 🚀 Production Use")
    print("6. ⚙️  Settings")
    print("7. 📖 Help")
    print("0. 🚪 Exit")
    print("="*30)

def print_dataset_menu():
    """Print the dataset management menu."""
    print("\n📊 DATASET MANAGEMENT:")
    print("="*30)
    print("1. Load dataset from URL")
    print("2. Load dataset from local file")
    print("3. Load default dataset")
    print("4. Show dataset information")
    print("5. Show sample data")
    print("0. Back to main menu")
    print("="*30)

def print_model_menu():
    """Print the model management menu."""
    print("\n🤖 MODEL MANAGEMENT:")
    print("="*30)
    print("1. Create new model")
    print("2. Load existing model")
    print("3. Save current model")
    print("4. Show model architecture")
    print("5. Model statistics")
    print("0. Back to main menu")
    print("="*30)

def print_training_menu():
    """Print the training menu."""
    print("\n🎯 TRAINING:")
    print("="*30)
    print("1. Setup training parameters")
    print("2. Start training")
    print("3. Quick train (10 epochs)")
    print("4. Full train (100 epochs)")
    print("0. Back to main menu")
    print("="*30)

def print_evaluation_menu():
    """Print the evaluation menu."""
    print("\n📈 EVALUATION:")
    print("="*30)
    print("1. Evaluate model accuracy")
    print("2. Test with sample data")
    print("0. Back to main menu")
    print("="*30)

def print_production_menu():
    """Print the production use menu."""
    print("\n🚀 PRODUCTION USE:")
    print("="*30)
    print("1. Single prediction")
    print("2. Batch prediction")
    print("3. Interactive prediction")
    print("0. Back to main menu")
    print("="*30)

def print_settings_menu():
    """Print the settings menu."""
    print("\n⚙️  SETTINGS:")
    print("="*30)
    print(f"1. Learning rate (current: {manager.learning_rate})")
    print(f"2. Epochs (current: {manager.epochs})")
    print(f"3. Batch size (current: {manager.batch_size})")
    print("0. Back to main menu")
    print("="*30)

def print_help():
    """Print help information."""
    print("\n📖 HELP:")
    print("="*30)
    print("This is a complete PyTorch ML pipeline for binary classification.")
    print("")
    print("QUICK START:")
    print("1. Load dataset (option 1)")
    print("2. Create model (option 2)")
    print("3. Train model (option 3)")
    print("4. Evaluate model (option 4)")
    print("5. Use in production (option 5)")
    print("")
    print("DATASET FORMAT:")
    print("- CSV file with features in all columns except the last")
    print("- Last column should contain binary labels (0 or 1)")
    print("- For the default dataset: 8 features + 1 binary label")
    print("")
    print("FEATURES FOR PREDICTION:")
    print("- 8 numerical values representing:")
    print("  1. Pregnancies")
    print("  2. Glucose")
    print("  3. Blood Pressure")
    print("  4. Skin Thickness")
    print("  5. Insulin")
    print("  6. BMI")
    print("  7. Diabetes Pedigree Function")
    print("  8. Age")
    print("="*30)

def get_numeric_input(prompt, min_val=None, max_val=None, default=None):
    """Get numeric input from user with validation."""
    while True:
        try:
            if default is not None:
                user_input = input(f"{prompt} (default: {default}): ").strip()
                if not user_input:
                    return default
            else:
                user_input = input(f"{prompt}: ").strip()
            
            value = float(user_input)
            
            if min_val is not None and value < min_val:
                print(f"Please enter a value >= {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"Please enter a value <= {max_val}")
                continue
            
            return value
            
        except ValueError:
            print("Please enter a valid number")

def get_features_input():
    """Get features input from user for prediction."""
    print("\n📝 Please enter 8 feature values (comma-separated):")
    print("   1. Pregnancies")
    print("   2. Glucose")
    print("   3. Blood Pressure")
    print("   4. Skin Thickness")
    print("   5. Insulin")
    print("   6. BMI")
    print("   7. Diabetes Pedigree Function")
    print("   8. Age")
    print("   Example: 2,120,80,0,0,25.1,0.5,30")
    
    try:
        features_str = input("\nEnter features: ").strip()
        features = [float(x.strip()) for x in features_str.split(',')]
        
        if len(features) != 8:
            print(f"✗ Please enter exactly 8 values, got {len(features)}")
            return None
        
        return features
        
    except ValueError:
        print("✗ Please enter valid numerical values")
        return None

def handle_dataset_menu(manager):
    """Handle dataset management menu."""
    while True:
        print_dataset_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            url = input("Enter dataset URL: ").strip()
            if url:
                manager.setup_dataset(csv_url=url)
        elif choice == '2':
            file_path = input("Enter local file path: ").strip()
            if file_path:
                manager.setup_dataset(local_file=file_path)
        elif choice == '3':
            manager.setup_dataset()
        elif choice == '4':
            manager.get_dataset_info()
        elif choice == '5':
            if manager.dataset:
                print("\nSample data from dataset:")
                for i in range(min(3, len(manager.dataset))):
                    features, label = manager.dataset[i]
                    print(f"Sample {i+1}:")
                    print(f"  Features: {features.numpy()}")
                    print(f"  Label: {label.item()}")
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def handle_model_menu(manager):
    """Handle model management menu."""
    while True:
        print_model_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            print("\nCreate new model with default architecture:")
            manager.create_model()
        elif choice == '2':
            custom_path = input(f"Model path (default: {manager.model_path}): ").strip()
            if custom_path:
                manager.model_path = custom_path
            manager.load_model()
        elif choice == '3':
            manager.save_model()
        elif choice == '4':
            manager.show_model_architecture()
        elif choice == '5':
            if manager.model:
                total_params = sum(p.numel() for p in manager.model.parameters())
                print(f"\n📊 Model Statistics:")
                print(f"Total parameters: {total_params:,}")
                if os.path.exists(manager.model_path):
                    file_size = os.path.getsize(manager.model_path)
                    print(f"Model file size: {file_size:,} bytes")
            else:
                print("No model loaded.")
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def handle_training_menu(manager):
    """Handle training menu."""
    while True:
        print_training_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            print("\n🎯 Setup Training Parameters:")
            lr = get_numeric_input("Learning rate", 0.0001, 1.0, manager.learning_rate)
            epochs = int(get_numeric_input("Epochs", 1, 1000, manager.epochs))
            batch_size = int(get_numeric_input("Batch size", 1, 128, manager.batch_size))
            
            manager.learning_rate = lr
            manager.epochs = epochs
            manager.batch_size = batch_size
            
            print(f"✓ Parameters updated:")
            print(f"  Learning rate: {manager.learning_rate}")
            print(f"  Epochs: {manager.epochs}")
            print(f"  Batch size: {manager.batch_size}")
            
            # Recreate dataloader if batch size changed
            if manager.dataset:
                manager.setup_dataset()
                
        elif choice == '2':
            if manager.model is None:
                manager.create_model()
            if manager.dataset is None:
                manager.setup_dataset()
            
            epochs = int(get_numeric_input("Number of epochs", 1, 1000, manager.epochs))
            manager.train_model(epochs)
            
        elif choice == '3':
            if manager.model is None:
                manager.create_model()
            if manager.dataset is None:
                manager.setup_dataset()
            
            manager.train_model(10)
            
        elif choice == '4':
            if manager.model is None:
                manager.create_model()
            if manager.dataset is None:
                manager.setup_dataset()
            
            manager.train_model(100)
            
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def handle_evaluation_menu(manager):
    """Handle evaluation menu."""
    while True:
        print_evaluation_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            manager.evaluate_model()
        elif choice == '2':
            if manager.model is None:
                print("No model available. Loading default model...")
                manager.load_model()
            
            if manager.model is None:
                print("No model available. Creating new model...")
                manager.create_model()
                manager.train_model(10)  # Quick training for demo
            
            features = get_features_input()
            if features:
                result = manager.predict_single(features)
                if result:
                    print(f"\n🎯 PREDICTION RESULT:")
                    print(f"  Probability: {result['probability']:.4f}")
                    print(f"  Prediction: {result['class']} ({result['prediction']})")
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def handle_production_menu(manager):
    """Handle production use menu."""
    while True:
        print_production_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            if manager.model is None:
                if os.path.exists(manager.model_path):
                    manager.load_model()
                else:
                    print("No model available. Creating and training a quick model...")
                    manager.create_model()
                    manager.setup_dataset()
                    manager.train_model(10)  # Quick training
            
            features = get_features_input()
            if features:
                result = manager.predict_single(features)
                if result:
                    print(f"\n🎯 PREDICTION RESULT:")
                    print(f"  Probability: {result['probability']:.4f}")
                    print(f"  Prediction: {result['class']} ({result['prediction']})")
                    
                    if result['prediction'] == 1:
                        print("  ⚠️  High risk of diabetes")
                    else:
                        print("  ✅ Low risk of diabetes")
                        
        elif choice == '2':
            if manager.model is None:
                print("No model available. Please train a model first.")
                continue
            
            print("\nBatch prediction from CSV file:")
            file_path = input("Enter CSV file path: ").strip()
            try:
                import pandas as pd
                df = pd.read_csv(file_path)
                
                # Assume all columns are features except possibly the last one
                if len(df.columns) == 8:
                    features = df.values
                elif len(df.columns) > 8:
                    features = df.iloc[:, :8].values
                else:
                    print("Error: Need at least 8 feature columns")
                    continue
                
                results = []
                for i, feature_row in enumerate(features):
                    result = manager.predict_single(feature_row)
                    if result:
                        results.append(result)
                        print(f"Sample {i+1}: {result['class']} (prob: {result['probability']:.4f})")
                
                print(f"\n✓ Processed {len(results)} predictions")
                
            except Exception as e:
                print(f"Error processing file: {e}")
                
        elif choice == '3':
            if manager.model is None:
                if os.path.exists(manager.model_path):
                    manager.load_model()
                else:
                    print("No model available. Creating a demo model...")
                    manager.create_model()
                    manager.setup_dataset()
                    manager.train_model(10)
            
            print("\n🔄 Interactive Prediction Mode")
            print("Enter feature values to make predictions (type 'quit' to exit)")
            
            while True:
                print("\n" + "-"*40)
                features_input = input("Enter features (or 'quit'): ").strip()
                
                if features_input.lower() in ['quit', 'q', 'exit']:
                    break
                
                try:
                    features = [float(x.strip()) for x in features_input.split(',')]
                    if len(features) != 8:
                        print("Please enter exactly 8 values")
                        continue
                    
                    result = manager.predict_single(features)
                    if result:
                        print(f"🎯 Result: {result['class']} (probability: {result['probability']:.4f})")
                        
                except ValueError:
                    print("Please enter valid numerical values")
                    
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

def handle_settings_menu(manager):
    """Handle settings menu."""
    while True:
        print_settings_menu()
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            lr = get_numeric_input("Learning rate", 0.0001, 1.0, manager.learning_rate)
            manager.learning_rate = lr
        elif choice == '2':
            epochs = int(get_numeric_input("Epochs", 1, 1000, manager.epochs))
            manager.epochs = epochs
        elif choice == '3':
            batch_size = int(get_numeric_input("Batch size", 1, 128, manager.batch_size))
            manager.batch_size = batch_size
        elif choice == '0':
            break
        else:
            print("Invalid option. Please try again.")

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application loop."""
    global manager
    manager = ModelManager()
    
    # Import numpy for feature handling
    try:
        import numpy as np
        globals()['np'] = np
    except ImportError:
        print("Warning: numpy not available. Some features may not work.")
    
    print_header()
    
    # Setup default dataset
    print("\n🔄 Setting up default dataset...")
    manager.setup_dataset()
    
    # Create default model
    print("\n🔄 Creating default model...")
    manager.create_model()
    
    while True:
        try:
            print_menu()
            choice = input("\nSelect an option (0-7): ").strip()
            
            if choice == '1':
                handle_dataset_menu(manager)
            elif choice == '2':
                handle_model_menu(manager)
            elif choice == '3':
                handle_training_menu(manager)
            elif choice == '4':
                handle_evaluation_menu(manager)
            elif choice == '5':
                handle_production_menu(manager)
            elif choice == '6':
                handle_settings_menu(manager)
            elif choice == '7':
                print_help()
            elif choice == '0':
                print("\n👋 Thank you for using PyTorch Binary Classifier!")
                print("Goodbye! 🚀")
                break
            else:
                print("Invalid option. Please select a number between 0-7.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\n✗ An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()