
def HW2_Student(hospitalCount, studentCount, hospPrefLists, studentPrefLists, hospOpenSlots):
    ################# YOUR CODE GOES HERE ##################
    final = []
    myHospList = {}
    for student in studentPrefLists:            #Checking for each hospital
        #displaced = None
        #print("Student:",student)-----------------------
        currSPrefList = studentPrefLists[student]
        picNum = 0
        while picNum < hospitalCount:
            pick = currSPrefList[picNum]
            for hospital in hospPrefLists:
                if hospital == pick:
                    if hospOpenSlots[hospital] > 0:
                        tentativeMatch = (hospital, student)
                        #print("Tentative Match: (hospital:",tentativeMatch[0],"student:",tentativeMatch[1],")")-------------
                        final.append(tentativeMatch)
                        #print("Hospital:",hospital,"has:",hospOpenSlots[hospital],"open slots")---------------
                        hospOpenSlots[hospital] = hospOpenSlots[hospital] - 1
                        #print("Hospital:",hospital,"has:",hospOpenSlots[hospital],"open slots")----------
                        picNum = hospitalCount
                        myHospList[str(hospital)] = student
                    else:
                        if str(hospital) in myHospList:
                            #print("hospital:",hospital)--------
                            #print("picNumEarly:",picNum)
                            #print("the current match is:",x)----------------
                            old = myHospList[str(hospital)]
                            placedStudent = old
                            currHPreflist = hospPrefLists[hospital]
                            indexOfCurr = currHPreflist.index(placedStudent)
                            indexOfProposing = currHPreflist.index(student)
                            #print("index of curr:",indexOfCurr,"<?","index of proposing:",indexOfProposing)-------------
                            if indexOfCurr < indexOfProposing:
                                #print("Cant Match! Index of Curr is less than index of proposing")---------------------
                                picNum = picNum + 1
                                #spl = studentPrefLists[student]
                                #hospital = spl[picNum]
                                #print("picNum:",picNum)-------------------------
                                #print("hospital should now be:",hospital)
                                #break
                            else:
                                print("hospital:",hospital)
                                print("old:",old)
                                final.remove((hospital,old))
                                #print("Override Match: (hospital:",hospital,"student:",student,")")------
                                final.append((hospital, student))
                                #print("A better match was found, now displacing Student:",x[1])-------------
                                myHospList[str(hospital)] = student
                                student = old
                                currSPrefList = studentPrefLists[student]
                                picNum = 1
                                #print("picNum:",picNum)-----------
                                #break

    #print("==========================================================================================================================================================================================")      
    return final # Return empty list for now

