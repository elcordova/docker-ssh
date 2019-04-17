FROM rastasheep/ubuntu-sshd:14.04
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN sudo apt-add-repository ppa:jonathonf/python-3.6
RUN sudo apt-get update
RUN sudo apt-get install python3.6 -y
Run sudo apt-get install python3-pip
COPY myscript.py /src/
RUN python3.6 -V