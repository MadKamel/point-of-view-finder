GOING = True
import os
while GOING:
    os.system('clear')
    text = input('Please copy+paste the text here: ')
    splittext = text.split(' ')
    debug = input('Debug output? [y/n] ') == 'y'
    sec = 0
    frst = 0
    thrd = 0
    try:
        splittext = splittext.split('.')
    except:
        pass

    for i in range(len(splittext)):
        if splittext[i].lower() in ['you', 'your', 'yours', 'yourself']:
            sec = sec + 1
        elif splittext[i].lower() in ['i', 'me', 'we', 'our', 'my', 'i\'m', 'myself', 'ours', 'us']:
            frst = frst + 1
        elif splittext[i].lower() in ['he', 'she', 'they', 'him', 'her', 'himself', 'herself', 'their', 'his', 'hers', 'theirs']:
            thrd = thrd + 1

    print('\n')
    if debug:
        print('First Person count: ' + str(frst))
        print('Second Person count: ' + str(sec))
        print('Third Person count: ' + str(thrd))

    print('\n====[RESULT]====')
    if thrd > sec:
        if thrd > frst:
            print('Third Person.')
        else:
            print('First Person.')
    elif frst < sec:
        print('Second Person.')
    elif sec < frst:
        print('First Person.')
    else:
        print('I cannot tell. Try using the debug feature.')
        
    GOING = input('\n\nAgain? [y/n] ') == 'y'

