# PyTorch Binary Classifier - Complete ML Pipeline

🎯 **A comprehensive menu-driven interface for training, evaluating, and using PyTorch binary classification models**

This project provides a complete machine learning pipeline for binary classification using PyTorch, featuring a user-friendly menu interface and all the tools you need for ML model development.

## 🚀 Quick Start

### Option 1: Easy Launch
```bash
cd code/ai/python/AI/pytorch/test/
python run_pipeline.py
```

### Option 2: Direct Launch
```bash
cd code/ai/python/AI/pytorch/test/
python ml_pipeline.py
```

## 📁 Project Structure

```
code/ai/python/AI/pytorch/test/
├── ml_pipeline.py          # Main menu-driven interface
├── run_pipeline.py         # Launcher script with dependency check
├── README.md               # This file
├── dataloader.py           # Original data loading (reference)
├── dataset.py              # Original dataset class (reference)
├── model.py                # Original model definition (reference)
├── optimizador.py          # Original training script (reference)
├── eval.py                 # Original evaluation script (reference)
└── modelo_clasificador_binario.pth  # Saved trained model (generated)
```

## 🎯 Features

### 📊 **Dataset Management**
- Load datasets from URL
- Load datasets from local CSV files
- Use default Pima Indians Diabetes dataset
- View dataset information and sample data

### 🤖 **Model Management**
- Create new neural network models
- Load existing trained models
- Save trained models to disk
- View model architecture and statistics

### 🎯 **Training**
- Configurable learning rate, epochs, and batch size
- Full training with progress monitoring
- Quick training (10 epochs) for testing
- Comprehensive training (100 epochs) for production

### 📈 **Evaluation**
- Calculate model accuracy on dataset
- Test predictions with sample data
- Detailed performance metrics

### 🚀 **Production Use**
- Single prediction for individual samples
- Batch prediction from CSV files
- Interactive prediction mode
- Risk assessment with probability scores

## 🔧 Technical Details

### Model Architecture
- **Input Layer**: 8 features (Pima Indians Diabetes dataset)
- **Hidden Layer 1**: 16 neurons
- **Hidden Layer 2**: 8 neurons  
- **Output Layer**: 1 neuron (binary classification)
- **Activation Functions**: ReLU (hidden layers), Sigmoid (output)

### Dataset Format
- **CSV format** with features in all columns except the last
- **Last column**: Binary labels (0 or 1)
- **Default dataset**: Pima Indians Diabetes dataset with 8 features

### Training Configuration
- **Default Learning Rate**: 0.001
- **Default Epochs**: 100
- **Default Batch Size**: 32
- **Optimizer**: Adam
- **Loss Function**: Binary Cross-Entropy Loss

## 📋 Menu Options Guide

### 1. 📊 Dataset Management
- **Option 1**: Load dataset from URL
- **Option 2**: Load dataset from local file
- **Option 3**: Load default dataset
- **Option 4**: Show dataset information
- **Option 5**: Show sample data

### 2. 🤖 Model Management
- **Option 1**: Create new model
- **Option 2**: Load existing model
- **Option 3**: Save current model
- **Option 4**: Show model architecture
- **Option 5**: Model statistics

### 3. 🎯 Training
- **Option 1**: Setup training parameters
- **Option 2**: Start training
- **Option 3**: Quick train (10 epochs)
- **Option 4**: Full train (100 epochs)

### 4. 📈 Evaluation
- **Option 1**: Evaluate model accuracy
- **Option 2**: Test with sample data

### 5. 🚀 Production Use
- **Option 1**: Single prediction
- **Option 2**: Batch prediction
- **Option 3**: Interactive prediction

### 6. ⚙️ Settings
- **Option 1**: Learning rate
- **Option 2**: Epochs
- **Option 3**: Batch size

## 🎯 Quick Workflow

### For Beginners:
1. **Start** → Run the pipeline
2. **Load default dataset** → Option 1 → Option 3
3. **Create model** → Option 2 → Option 1
4. **Quick training** → Option 3 → Option 3
5. **Evaluate** → Option 4 → Option 1
6. **Use in production** → Option 5 → Try Option 3 (Interactive)

### For Advanced Users:
1. **Configure settings** → Option 6
2. **Load custom dataset** → Option 1 → Option 1/2
3. **Full training** → Option 3 → Option 4
4. **Batch predictions** → Option 5 → Option 2

## 🔍 Prediction Guide

### Input Format for Predictions
Enter 8 numerical values representing:
1. **Pregnancies** - Number of pregnancies
2. **Glucose** - Plasma glucose concentration
3. **Blood Pressure** - Diastolic blood pressure (mm Hg)
4. **Skin Thickness** - Triceps skinfold thickness (mm)
5. **Insulin** - 2-Hour serum insulin (mu U/ml)
6. **BMI** - Body mass index (weight in kg/(height in m)²)
7. **Diabetes Pedigree Function** - Diabetes pedigree function
8. **Age** - Age (years)

### Example Prediction:
```
Enter features: 2,120,80,0,0,25.1,0.5,30

Result:
🎯 Result: Low risk of diabetes (probability: 0.1234)
```

## 🛠️ Installation & Dependencies

### Required Packages
```bash
pip install torch pandas numpy
```

### System Requirements
- Python 3.6+
- PyTorch
- Pandas
- NumPy

## 🚨 Important Notes

### Model Persistence
- Models are saved as `modelo_clasificador_binario.pth`
- Models load with CPU compatibility by default
- Training progress is not saved (full retraining required)

### Data Safety
- Original scripts are preserved in reference files
- New pipeline doesn't modify existing files
- Dataset downloads are handled safely

### Performance
- Default dataset: 768 samples, trains in ~30 seconds (10 epochs)
- Full training: ~3-5 minutes (100 epochs)
- Batch predictions: Near real-time

## 🆘 Troubleshooting

### Common Issues:

**Import Error**: Run `python run_pipeline.py` to auto-install dependencies

**No Model Error**: The pipeline will automatically create/train a model when needed

**Slow Training**: Reduce epochs in settings or use quick training mode

**Memory Issues**: Reduce batch size in settings menu

**Dataset Download Issues**: Check internet connection or use local file

## 📞 Support

For issues or questions:
1. Check the help menu (Option 7 in main menu)
2. Review the troubleshooting section above
3. Examine the original reference scripts for implementation details

## 🎓 Learning Resources

This pipeline demonstrates:
- PyTorch neural network implementation
- Data loading and preprocessing
- Training loop implementation
- Model evaluation and metrics
- Production prediction systems
- User interface design for ML tools

---

**Built with ❤️ using PyTorch for educational and production use**

*Start your ML journey today with this comprehensive pipeline!* 🚀