import time
from weather import get_data, get_temp_forecast, get_temp, get_forecast
from chat_suite import start_client, send_message, end_client, get_prev_msg

def print_options():
    return 'gt -> get temp for 13 days\ngt [1..13] -> get specific day temperature\ngf -> get forecast for 13 days\ngf [1..13] -> get specific day temperature\nch [clear, cloud, rain, ...] -> get list of all days with the query given.\no -> list options\nq -> quit'

# BASIC STRUCTURE OF BOTS
# forever listen:
#   initialize the bot with all the info it needs
#
#   answer the user based on their query.

# start the chat bot
client = start_client("wbot")
zipcode = '' # scoping
send_message(client,"the weather bot has started... type your zipcode to get started")
# initially the chat bot is not initialized
init = False
while True:
    # don't worry about this sleep!
    time.sleep(1)

    # gets the previous message
    msg = get_prev_msg()

    # if the bot was not initalized
    if not init:
        zipcode = get_prev_msg()
        # we keep listening till we get the zipcode
        while(len(zipcode) != 5 or (len(zipcode) == 5 and int(zipcode) < 10000 and int(zipcode) > 99999)):
            time.sleep(1)
            zipcode = get_prev_msg()
        send_message(client, 'here are the options:\n' + print_options())
        init = True
    else:    # if the bot was initialized with a zipcode
        opt = msg
        if opt == 'o':
            send_message(client, print_options())
            continue
        elif opt == 'q':
            send_message(client, 'Thank you for using this bot')
            break
        elif opt == '':
            continue

        query = opt.split(' ')
        if len(query) == 1:
            if query[0] == 'gt':
                send_message(client, str(get_temp(zipcode)))
                continue
            elif query[0] == 'gf':
                send_message(client, str(get_forecast(zipcode)))
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
                    send_message(client, str(get_temp(zipcode)[val - 1]))
                elif query[0] == 'gf':
                    send_message(client, str(get_forecast(zipcode)[val - 1]))

send_message(client, "Thanks for using the weather bot!")
end_client(client)
