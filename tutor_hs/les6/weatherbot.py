import time
from weather import get_data, get_temp_forecast, get_temp, get_forecast
from chat_suite import start_client, send_message, end_client, get_prev_msg

# here is a function that returns a string of all the function
def print_options():
    return 'gt -> get temp for 13 days\ngt [1..13] -> get specific day temperature\ngf -> get forecast for 13 days\ngf [1..13] -> get specific day temperature\nch [clear, cloud, rain, ...] -> get list of all days with the query given.\no -> list options\nq -> quit'

# BASIC STRUCTURE OF BOTS
# forever listen:
#   initialize the bot with all the info it needs
#
#   answer the user based on their query.

# start the chat bot like how we did in the chat client
client = #TODO
zipcode = ''

# let's offically tell the user that the bot has started
send_message(client,"the weather bot has started... type your zipcode to get started")
# initially the chat bot is not initialized
init = False
while True:
    # don't worry about this sleep!
    time.sleep(1)

    # gets the previous message using get_prev_msg()
    msg = #TODO
    # if the bot was not initalized
    if not init:
        zipcode = get_prev_msg()
        # we keep listening till we get the zipcode
        while(complete me!): #TODO
            time.sleep(1)
            zipcode = #TODO
        # TODO: print out the options
        # TODO: set init to true since we finished initializing
    else:    # if the bot was initialized with a zipcode
        opt = msg
        if opt == 'o':
            #TODO: send the print_option
            continue
        elif opt == 'q':
            #TODO: send the bye bye message
            break
        elif opt == '':
            continue

        query = opt.split(' ')
        if len(query) == 1:
            if query[0] == 'gt':
                # TODO: send the temperature data using get_temp(zipcode)
                continue
            elif query[0] == 'gf':
                # TODO: send the temperature data using get_forecast(zipcode)
                continue
        elif len(query) == 2:
            if query[0] == 'ch':
                forecast = get_forecast(zipcode)
                days = list()
                for i in range(len(forecast)):
                    if query[1] in forecast[i]:
                        days.append(i + 1)
                send_message(client, str(days))
                continue
            if query[0] != 'gt' and query[0] != 'gf':
                continue
            val = int(query[1])
            if val >= 1 and val <= 13:
                if query[0] == 'gt':
                    #TODO: Get the temperature data of a particular day using get_temp(zipcode)... remember that computers count from 0
                elif query[0] == 'gf':
                    #TODO: Get the temperature data of a particular day using get_forecast(zipcode)... remember that computers count from 0

# TODO: provide an exit message!
end_client(client)
