from chatSession import Chat_session

def member_search():

    session = Chat_session(r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week5\Class_Work\REAL_WORLD_EXAMPLE\iphone_07_18-1.annot')

    memberIndices = []
    uniqueMembers = session.get_unique_members()
    membersLst = session.get_members()
    messages = session.get_messages()

    for member in uniqueMembers:
        indexList = []
        for i in range(len(membersLst)):
            if member in membersLst[i]:
                indexList.append(i)
        memberIndices.append(indexList)

    message_finder = int(input('Enter the index you would like to find : \n'))
    print(f'{uniqueMembers[message_finder]} appears in indices {memberIndices[message_finder]}')
    for value in memberIndices[message_finder]:
        print(messages[value])


if __name__ == '__main__':
    member_search()
