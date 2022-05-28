# voice = "Shout | "

# print(voice * 5)

# aList = [1,2,3,4,5,6]

# print(aList * 3)


# from re import A


# age =  45

# print(age)

# age += 1

# print(age)

# age = 17
# movie = "ScaryTerry"

# if(age > 18):
#     print('Customer can watch ' + movie)
    
# else:
#         print('You cannot watch the movie')


# username: input('Username: \n')
# password: input('Password: \n')


name = input('What is your name?: \n')
allowedUsers = ['Daniel', 'Mike', 'Love']
allowedPassword = 'Password'

if(name in allowedUsers):
    password = input('Your password: \n')

    if(password == allowedPassword):
        print('Welcome %s' % name)
    else: 
        print('Password was incorrect, please try again')

else:
    print('Name not found, please try again')