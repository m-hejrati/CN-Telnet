import socket

PORT = 2300
HOST = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Connected To Server!')

while True:
    temp = input()

    with open('history.txt', 'a') as f:
        f.write(temp + '\n')

    splitted = temp.split()
    if (splitted[0] == "telnet"):

        # print (msg_type)
        # print(splitted[2:])

        message = ""
        message += " ".join(splitted[2:])

        # print(messages)

        msg_type = splitted[1]

        if (msg_type == "upload"):
            fname = message
            try:
                with open(fname, 'rb') as f:
                    s.send('upload'.encode('utf-8'))
                    s.send(fname.encode('utf-8'))        
                    data = f.read()
                    s.send(data.__sizeof__().__str__().encode('utf-8'))
                    s.send(data)
                    print ("file " + fname + " sent")

            except OSError:
                print ("Could not open file: " + fname)
        
        elif (msg_type == "exec"):
            s.send('exec'.encode('utf-8'))
            # print(message)
            s.send(message.encode('utf-8'))

        elif (msg_type == "send -e"):
            pass
        
        elif (msg_type == "send"):
            s.send('send'.encode('utf-8'))
            print(message)
            s.send(message.encode('utf-8'))

        elif (msg_type == "history"):
            if (splitted[2] == "clear"):
                open('history.txt', 'w').close()
                print("history cleared ...")
            elif (splitted[2] == "show"):
                with open('history.txt', 'r') as f:
                    print('History:\n' + f.read())
        
        elif (msg_type == "email"):
            pass

        else:
            print ("wrong message...\nwrite \"help\" to get more information ...")
        
    elif(splitted[0] == "help"):
        print ("telnet send <>  \t send simple message")
        print ("telnet history clear \t clear history file")
        print ("telnet history show \t show all previous entered command")
        print ("telnet exec <> \t\t execute a command in server side")
        print ("telnet upload <> \t send a file")
        # print ("telnet send: \t send simple message")
        print ("exit \t\t\t end the connection")

    elif (splitted[0] == "exit"):
        print('finish ...')
        break

    else:
        print ("wrong message...\nwrite \"help\" to get more information ...")
    
s.close()