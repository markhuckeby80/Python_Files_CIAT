class Chat_session:
    
    def __init__(self, filename):
        self.membersLst = []
        self.messageLst = []
        self.tagsLst = []
        self.timeLst = []
        self.userSysLst = []
        self.cleanMessagesLst = []
        self.uniqueMembersLst = []

        file_handle = open(filename, 'r')
        records = file_handle.readlines()
        self.numThreads = 0

        for record in records:
            self.numThreads += 1
            fields = record.split()
            self.tagsLst.append(fields[0])
            self.timeLst.append(fields[1])
            self.membersLst.append(fields[2])
            self.userSysLst.append(fields[3])
            self.messageLst.append(' '.join(fields[4:]).strip())

        self.uniqueMembersLst = sorted(list(set(self.membersLst)))

        file_handle.close()

        cleanWordLst = []
        for line in self.messageLst:
            line = line.split()
            for word in line:
                cleanLst = []
                for x in word:
                    if x.isalnum() or x.isspace():
                        cleanLst.append(x)
                    cleanWrd = ''.join(cleanLst)
                cleanWordLst.append(cleanWrd)
            newWord = ' '.join(cleanWordLst)
            self.cleanMessagesLst.append(newWord.lower())
                    
    def get_members(self):
        return self.membersLst
    
    def get_messages(self):
        return self.messageLst
    
    def get_tags(self):
        return self.tagsLst
    
    def get_time(self):
        return self.timeLst
    
    def get_user_sys(self):
        return self.userSysLst
    
    def get_unique_members(self):
        return self.uniqueMembersLst
    
    def get_num_threads(self):
        return self.numThreads
    
    def get_clean_messages(self):
        return self.cleanMessagesLst
