# Good practice to be specific about the version
# so that the build is truly reproducible
FROM python:3.7.4-slim-buster

# Another good practice is to copy dependency file
# first and install, so in future pulls you can
# leverage layer caching; this layer will only repull
# if requirements.txt changes with new dependencies
COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

# No need to RUN mkdir, as WORKDIR makes the directory
# and does a cd into it for you as well
WORKDIR /app

# now we copy the rest of the app code, excluding things 
# that are in .dockerignore like .venv and generated files
COPY . .

RUN python dataPresenter.py

# could get fancy and wrap all this stuff in Flask or something
# but we're just going simple and using python's built-in http server
CMD ["python", "-m", "http.server", "47150"]