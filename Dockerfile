FROM python:3.11-slim

WORKDIR /app

# Update pip to latest version
RUN pip install --upgrade pip

# Create a script to download packages at runtime so they persist to mounted volume
RUN echo '#!/bin/bash\n\
echo "Downloading Ansible packages for Windows..."\n\
pip download \\\n\
    --platform win_amd64 \\\n\
    --python-version 3.11 \\\n\
    --only-binary=:all: \\\n\
    --dest /app/ansible_packages \\\n\
    --verbose \\\n\
    ansible ansible-navigator\n\
echo "Download complete! Packages saved to /app/ansible_packages/"\n\
ls -la /app/ansible_packages/\n\
' > /app/download_packages.sh && chmod +x /app/download_packages.sh

# Run the download script
CMD ["/app/download_packages.sh"]