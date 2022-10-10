# Create virtual environment 
- name: api
# Activate the virtual environment from the command line 
- api\Scripts\activate.bat
# Install fastapi [(ll module)
- pip install fastapi[all]
# Check all dependencies installed 
- pip freeze 
# Run the live server 
- uvicorn main:app --reload
