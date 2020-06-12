def matchJobs(jobsPreferences, candidatesPreferences):
    matches = []                                     # the list of matches, initially its empty
    freeCandidates = [i for i in jobsPreferences]    # candidates who still does not have a job, initially its every candidates
    while len(freeCandidates) > 0:                   # if there are still candidates who does not have a job, continue the loop to find match
        for c in freeCandidates:
            for j in jobsPreferences[c]:             # for every candidate c, j is their preference
                tempMatch = [match for match in matches if j in match]    # find if their preference has been matched to a candidate
                if len(tempMatch) == 0:              # if have not been match yet
                    matches.append([c, j])           # add the match to matches list
                    freeCandidates.remove(c)         # remove candidate from freeCandidate list
                    break
                else:                                # else has been matched 
                    if candidatesPreferences[j].index(c) < candidatesPreferences[j].index(tempMatch[0][0]):    # compare c to matched candidate
                        freeCandidates.remove(c)     # if c is more preferable than the matched candidate, remove c from the freeCandidates list
                        freeCandidates.append(tempMatch[0][0])    # and add matched candidate to the freeCandidates list
                        tempMatch[0][0] = c          # changed the matched candidate to c
                        break
    return matches

jobsPreferences = {"c1": ["j4", "j1", "j2", "j3"], "c2": ["j1", "j2", "j4", "j3"], "c3": ["j1", "j3", "j4", "j2"], "c4": ["j1", "j3", "j4", "j2"]}
candidatesPreferences = {"j1": ["c3", "c4", "c2", "c1"], "j2": ["c2", "c3", "c1", "c4"], "j3": ["c4", "c2", "c3", "c1"], "j4": ["c4", "c3", "c1", "c2"]}

print(matchJobs(jobsPreferences, candidatesPreferences))
