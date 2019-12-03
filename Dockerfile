FROM ubuntu:18.04
RUN apt-get update && apt-get install \
    -y --no-install-recommends python3 python3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#set environments
ENV DISCORD_TOKEN={DISCORD_TOKEN_HERE}
ENV API_ACCESS_CODE={API_ACCESS_CODE_HERE}
ENV API_BASE_URL="https://yrmfkazv8g.execute-api.ca-central-1.amazonaws.com/dev_ca_central_1"
COPY *.py /
CMD ["python", "bot.py"]
