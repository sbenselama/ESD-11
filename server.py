#######################################################
#title - server                                       #
#date - 05/09/2017                                    #
#######################################################

#######################################################

################# importation fonction externe ########

import socket


################# fonction ############################

H = '10.94.73.3'
P = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((H, P))
socket.error


while 1 :
	print "serveur en attente..."
	server_socket.listen(5)

	connexion, adresse = server_socket.accept()
	print "connexion etablie"
