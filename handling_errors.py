while True:
    try:
        x = int(input('Please type a number'))
        break
    except:
        print('That\'s not a number value')
    # except ValueError:
        # print('Enter correct value')
    # except KeyboardInterrupt:
        # print('No value entered!!')
        # break
    finally:
        print(f'Number entered is {x} !!!')