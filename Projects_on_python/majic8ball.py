import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Concentrate and ask again"
    elif answerNumber == 6:
        return "Ask again later"
    elif answerNumber == 7:
        return "Outlook not so good"
    elif answerNumber == 8:
        return "My reply is no"
    else:
        r = random.randint(1, 8)
        return getAnswer(r)

fortune = getAnswer(random.randint(1, 9))
print(fortune)