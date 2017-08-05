import time
from chat_suite import start_client, send_message, end_client, get_prev_msg
# import python files that call an api that you need

# let's start the client
client = start_client("YOUR BOT NAME")

# variables all bots need!
field1 = ''
field2 = 0

# loop begins!
while True:
    # we get the previous messages sent to the server
    time.sleep(1)
    msg = get_prev_msg()

    # if it is the first time the bot is being used
    if not init:
        msg2 = get_prev_msg()
        # wait til the input is in the correct format
        correct = False
        while (!correct):
            time.sleep()
            msg2 = get_prev_msg()
        # we got the correct format
        # we have initialized the bot!
        init = True
    else:   # if the bot was initialized before
        # do commands for the user based on their input!
        # if they want to quit, let them quit!
        if msg == 'q':
            break

# so we are done with the bot :(
# so let's end the bot formally
end_client(client)
