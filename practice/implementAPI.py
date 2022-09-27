def implementAPI(logs):
    # Write your code here
    log_status = False
    log_user_name = ''
    user_name = []
    user_password = []
    for i in logs:
        request = i.split(' ')
        if request[0] == "register":
            if request[1] not in user_name:
                user_name.append(request[1])
                user_password.append(request[2])
                print("Registered Successfully")
            else:
                print("Username already exists")
        elif request[0] == "login":
            if log_status is False and user_password[user_name.index(request[1])] == request[2]:
                log_user_name = request[1]
                log_status = True
                print("Logged In Successfully")

            else:
                print("Login Unsuccessful")
        else: # request[0] == "logout"
            if log_status is True and log_user_name == request[1]:
                log_user_name = ''
                log_status == False
                print("Logged Out Successfully")

            else:
                print("Logout Unsuccessful")

logs = ["register david david123", "register adam 1Adam1", "login david david123", "login adam 1adam1", "logout david"]
implementAPI(logs)




