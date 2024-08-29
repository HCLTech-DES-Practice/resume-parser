FROM python:3.11.8-slim

# Expose port you want your app on
EXPOSE 8000

RUN pip install -U pip

COPY requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /app
WORKDIR /app

# run it!
CMD streamlit run --server.port=8000 app.py