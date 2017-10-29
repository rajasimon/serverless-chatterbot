FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Download non wheel packages
RUN pip download MarkupSafe
RUN pip download ruamel.yaml
RUN pip download SQLAlchemy

# Create wheel package
RUN pip wheel MarkupSafe
RUN pip wheel ruamel.yaml
RUN pip wheel SQLAlchemy

RUn pip install --target=/app MarkupSafe-1.0-cp36-cp36m-linux_x86_64.whl
RUN pip install --target=/app ruamel.yaml-0.15.34-cp36-cp36m-manylinux1_x86_64.whl
Run pip install --target=/app SQLAlchemy-1.1.14-cp36-cp36m-linux_x86_64.whl

