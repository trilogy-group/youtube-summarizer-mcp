# Remove existing virtual environment if it exists
if [ -d ".venv" ]; then
    rm -rf .venv
fi

# Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Verify the Python version and environment
echo "Using Python version: $(python --version)"
echo "Python executable: $(which python)"

# Install required packages
pip install -r requirements.txt

# Run the client and server
python MCP/server.py

# Deactivate the virtual environment
deactivate