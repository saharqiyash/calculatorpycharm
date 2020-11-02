FROM python:3

ADD . /src

#RUN pip3 install pandas

#CMD [ "python", "/src/tests/test_calculator.py" ]

CMD ["python", "-m", "unittest", "discover", "-s","/src/tests"]