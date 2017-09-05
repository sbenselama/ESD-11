#######################################################
#title - client                                       #
#date - 05/09/2017                                    #
#######################################################

################# importation fonction externe ########

import socket, sys

################# fonction ############################

H = '10.94.73.3'
P = 50000	

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((H , P))
print "connexion echouer"

print "connexion etablie"
