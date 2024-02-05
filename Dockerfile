# 
FROM python:3.8-slim

# This is directory inside container
WORKDIR /cont_transmiim

# 
COPY ./requirements.txt /cont_transmiim/requirements.txt

# 
RUN pip3 install --no-cache-dir --upgrade -r /cont_transmiim/requirements.txt

# copy current source container to desitnation containers 
COPY ./src /cont_transmiim/src

# Inside container, go to src->main.py-> and run app variable with host and ports
CMD ["python3" , "-m" , "uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8002"]