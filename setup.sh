echo "This script assumes that Python3 is already installed."
echo "If python3 is not installed, please install it using your machine's package manager."
echo
echo "Checking Python version"
python3 --version
echo
echo "Checking pip installation"
echo
python3 -m ensurepip --upgrade
echo
echo "pip successfully / already installed"
echo "Installing OpenCV dependencies"
echo
pip install opencv-python
echo
echo "All dependencies installed."
echo "You may now run the OpenCV Demo."
echo