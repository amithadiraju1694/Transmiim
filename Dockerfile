# 
FROM python:3.9-slim

# This is directory inside container
WORKDIR /cont_transmiim

# Install Git on Container to clone our repo
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Cloning code into container from a public repository
# cont_transmiim -> src, Docker, requirements.txt
RUN git clone -b feat_streamlit_gs https://github.com/amithadiraju1694/Transmiim.git .

# 
RUN pip3 install -r requirements.txt

# Expose this specific port to web traffic
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


ENTRYPOINT [ "streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0" ]