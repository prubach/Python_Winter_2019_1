while True:
    try:
        x = int(input('Please enter a number:'))
        break
    except (KeyboardInterrupt, ValueError) as e:
        print('Not a number, please try again')
        print(e)
print('I got: ' + str(x))