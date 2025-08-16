FROM python:3.11-slim

WORKDIR /app

# Update pip to latest version
RUN pip install --upgrade pip

# Create pyinfra_packages directory
RUN mkdir -p /app/pyinfra_packages

# Create a script to download packages when container runs
RUN echo '#!/bin/bash\n\
echo "Downloading PyInfra <3.0 for Windows (ArcGIS Pro 3.1.2 compatibility)..."\n\
pip download --dest /app/pyinfra_packages --platform win_amd64 --python-version 3.9.16 --only-binary=:all: "pyinfra<3"\n\
echo "Downloading additional Windows dependencies..."\n\
pip download --dest /app/pyinfra_packages --platform win_amd64 --python-version 3.9.16 --only-binary=:all: colorama sspilib\n\
echo "Download complete! Packages saved to /app/pyinfra_packages/"\n\
ls -la /app/pyinfra_packages/\n\
echo "Container will exit."\n\
' > /app/download.sh && chmod +x /app/download.sh

# Run the download script
CMD ["/app/download.sh"]