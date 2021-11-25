# server.py
import socket
from _thread import start_new_thread

import Other.global_variable
from Other import global_variable
from monitor import Init_game
from structure.Player_file import Player

list_of_clients = []

preflop = 0; flop = 1; turn = 2; river = 3

# Using the below function, we broadcast the message to all clients
def broadcast(message):
    for clients in list_of_clients:
        try:
            clients.send(message)
        except:
            clients.close()
            # if the link is broken, we remove the client
            remove(clients)


# The following function simply removes the object from the list
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


def clientthread(conn, addr, i):
    # Initialisation code game
    from Other.global_variable import liste_player

    liste_player.append(Player.__init__(Player, i, global_variable.starting_stack))

    etat = preflop

    while True:
        # si le client reçoit premier tour alors faire ceci, si le client fold alors mettre le client en attente
        if etat == preflop:
            print("preflop")
        elif etat == flop:
            print("flop")
        elif etat == turn:
            print("turn")
        elif etat == river:
            print("river")
        try:
            message = conn.recv(2048)
            if message:

                print("<" + addr[0] + "> " + message)

                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send)

            else:
                """message may have no content if the connection
                is broken, in this case we remove the connection"""
                remove(conn)

        except:
            continue


def run_server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # takes the first argument from command prompt as IP address
    IP_address = "127.0.0.1"

    # takes second argument from command prompt as port number
    Port = 9999
    # close port kill 9999 with "exit" command

    # bind to the port
    serversocket.bind((IP_address, Port))

    # queue up to 5 requests
    serversocket.listen(Other.global_variable.nb_player)

    i = 0

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()

        list_of_clients.append(clientsocket)

        start_new_thread(clientthread, (clientsocket, addr, i))

        print("Got a connection from %s" % str(addr))

        i += 1

        # start la partie
        if i == Other.global_variable.nb_player:
            # passe le relai à init_game
            server_game()

    conn.close()
    server.close()


def server_game():
    Init_game.tour()
