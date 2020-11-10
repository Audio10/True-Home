FROM python:3
ENV PYTHONUNBUFFERED 1
RUN pip install -U pip pipenv
RUN mkdir /true_Home
WORKDIR /true_Home
COPY ["./true_Home/Pipfile", "/true_Home/"] 
COPY ["./true_Home/Pipfile.lock", "/true_Home/"] 
RUN pipenv install --ignore-pipfile --system --deploy 
COPY ["./true_Home/", "/true_Home/"] 