npm i

python -m venv env
source env/Scripts/activate

python -m pip install --upgrade pip

poetry add uvicorn fastapi sqlalchemy
pip install ariadne

poetry install
