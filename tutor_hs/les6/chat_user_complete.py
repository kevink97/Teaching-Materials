from chat_suite import start_client, send_message, end_client, get_prev_msg
# start_client(username) -> returns a client
# send_message(client, msg)
# end_client(client) -> removes the client

print("Welcome to the chat app")

# ask the user for a username
username = input("Choose a username: ")

# Here we start the client and connect it to the server
client = start_client(username)

print("press ctrl-c to quit")
print("this symbol (>) signifies where your message should be")

while True:
    try: # don't worry about this!
        msg = input(">")
        send_message(client, msg)
    except KeyboardInterrupt: # if the user quits
        break

# we should end the client here :)
print("goodbye!")
end_client(client)
