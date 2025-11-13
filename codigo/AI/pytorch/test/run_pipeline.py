#!/usr/bin/env python3
"""
Launcher script for the PyTorch ML Pipeline
==========================================

This script serves as the main entry point for the complete ML pipeline.
Run this script to start the menu-driven interface.

Usage:
    python run_pipeline.py

Or simply:
    python ml_pipeline.py
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed."""
    required_packages = ['torch', 'pandas', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Installing missing packages...")
        
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
                return False
        
        print("✅ All dependencies installed successfully!")
    
    return True

def main():
    """Main launcher function."""
    print("🚀 PyTorch ML Pipeline Launcher")
    print("=" * 40)
    
    # Check if we're in the correct directory
    if not os.path.exists('ml_pipeline.py'):
        print("❌ Error: ml_pipeline.py not found in current directory")
        print("Please run this script from the codigo/AI/pytorch/test/ directory")
        return 1
    
    print("📋 Checking dependencies...")
    if not check_dependencies():
        print("❌ Failed to install dependencies. Please install manually:")
        print("pip install torch pandas numpy")
        return 1
    
    print("✅ All dependencies ready!")
    print("\n🎯 Starting ML Pipeline...")
    print("=" * 40)
    
    # Run the main pipeline
    try:
        subprocess.run([sys.executable, 'ml_pipeline.py'])
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error running pipeline: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)