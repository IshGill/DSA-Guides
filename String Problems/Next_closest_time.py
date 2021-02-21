# Remember the time conversions!
# *24 hour time to minutes is hours digit * 60 + minutes digits
# *For this question you need to set each converted times digit individually, hence remember:
# *Hours tens digit = total minutes / 60 / 10
# *Hours ones digit = total minutes / 60 % 10
# *Minutes tens digit = total minutes % 60 / 10
# *Minutes ones digit = total minutes % 60 % 10
# *Set up a hash set which contains all the values which you are allowed to work with
# *Every times you increment you totalminutes check if that newly incremented value has digits which are all present in the hash set, if so flag will stay True we are done! return the result!
def nextClosestTime(time):
    hoursInMins = int(time[:2]) * 60
    totalMins = hoursInMins + int(time[3:])

    hashSet = set()
    for i in time:
        if i.isdigit():
            hashSet.add(int(i))

    while True:
        totalMins = (totalMins + 1) % (1440)
        totalNewTime = str(totalMins / 60 / 10) + str(totalMins / 60 % 10) + ":" + str(totalMins % 60 / 10) + str(
            totalMins % 60 % 10)

        flag = True
        for i in totalNewTime:
            if i.isdigit():
                if int(i) not in hashSet:
                    flag = False

        if flag == True:
            return totalNewTime


def nextClosestTime(time):
    # Convert 24 hour time to minutes
    hoursInMins = int(time[:2]) * 60
    totalMins = hoursInMins + int(time[3:])

    # Build hash set with current given times in order to check if the new time we build is valid as
    # the new time must have characters from the current given time!
    hashSet = set()
    for i in time:
        if i.isdigit():
            hashSet.add(int(i))

    # Keep incrementing the minutes starting from our converted input, recall we want the next closest time which is greaters but all the digits which make it up can be found in the original input time.
    while True:
        # We need to mod the minutes by 1440 so 60 * 24 (hours * day) in order to keep it in proper 24 hour format
        totalMins = (totalMins + 1) % (1440)
        # We specify each single digit in the new string! Cannot just do hours % 1440 / 60 and mins % 1440 % 60 as we need to account for the tens and ones units.
        totalNewTime = str(totalMins / 60 / 10) + str(totalMins / 60 % 10) + ":" + str(totalMins % 60 / 10) + str(
            totalMins % 60 % 10)

        # Set a flag, this flag will change to False if there is any character in the new converted time which does not exist in the old time
        flag = True
        for i in totalNewTime:
            if i.isdigit():
                if int(i) not in hashSet:
                    flag = False

        if flag == True:
            return totalNewTime