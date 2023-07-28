# Installation
Prerequisites:
```
Have Python3 with pip
```
Clone the Git repository:
```bash
git clone https://....
```
Install the Python dependencies:
```bash
# Unix OS based
pip3 install -r requirements.txt
# Windows
pip install -r requirements.txt
```

# Run
A script has been created to check with mypy that the Python code is correctly typed before execution. Therefore, you need to run a bash script:
```bash
./run.sh
```
To execute without the control (not recommended):
```bash
python3 api.py
```