FROM apache/spark:3.5.1

WORKDIR /app

USER root

RUN pip install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    scikit-learn \
    jupyter \
    notebook \
    findspark \
    pyspark

COPY . /app

CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "case_study_colab_updated (1)"]