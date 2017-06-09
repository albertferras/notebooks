FROM python:3.6-slim

RUN pip3 install asynctest ipython[notebook]

WORKDIR /app

# Install custom extensions
RUN mkdir /nbextensions
COPY nbextensions/* /nbextensions/
RUN ln -s /nbextensions/* $(ipython locate)/nbextensions \
    && jupyter nbextension enable toc

CMD jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --port=8899
