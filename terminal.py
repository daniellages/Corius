from subprocess import Popen, PIPE

def send_terminal(message):
    pipe = Popen(message, shell=True, stdout=PIPE).stdout
    output = pipe.read()
    return output