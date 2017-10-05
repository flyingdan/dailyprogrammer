import fileinput

messages = {}
for line in fileinput.input():
    # Split the line into at most 4 elements and take the first 3
    mID, pID, mSize = line.split(maxsplit=3)[:3]

    if mID not in messages:
        # Initialize dictionary element with list object
        messages[mID] = [int(mSize)] # easy way to keep track of message size for later

    # Append list of [packetID, "full line"]
    messages[mID].append([int(pID), line.strip()])
    #dictionary is now {mID, [mSize, [pID, "full line"]]}
    if len(messages[mID])-1 == messages[mID][0]:
        # Sort the list of lists using pID as index
        for message in sorted(messages[mID][1:]):
            print(message[1])
