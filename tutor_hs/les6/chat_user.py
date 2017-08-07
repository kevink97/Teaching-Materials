from chat_suite import start_client, send_message, end_client, get_prev_msg
# start_client(username) -> returns a client
# send_message(client, msg)
# end_client(client) -> removes the client

print("Welcome to the chat app")

# ask the user for a username
# Write your code here

# Here we start the client and connect it to the server
# We have a method called start_client which takes in a username.
# The function gives back a user.
# let the function = to the client variable here
# Write your code below:
client = 

# Here are some instructions for the user
print("press ctrl-c to quit")
print("this symbol (>) signifies where your message should be")

# we just keep looping til the client quits
# We do this so that the user can keep sending messages.
while True:
    try: # don't worry about this!
        # ask for an input... like it says on line 20
        # write code here

        #then send the message using the send_message function.
        # it takes in the client and the message
        # write code here
    except KeyboardInterrupt: # if the user quits
        # how do we exit a loop?

# we should end the client here :)
print("goodbye!")
# use the end_client function which takes in client to logoff the client
