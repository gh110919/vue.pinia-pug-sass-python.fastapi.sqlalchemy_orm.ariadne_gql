source env/Scripts/deactivate

rm -rf "env"
rm -rf "node_modules"
rm -f "poetry.lock"

find . -type d -name "__pycache__" -exec rm -rf {} +
