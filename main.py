import sys
import os

treeFile = sys.argv[1]
outputDir = sys.argv[2]

file = open(treeFile, 'r', encoding="utf-8")
lines = file.readlines()

stack = []
prevTabs = 0

for line in lines:
    currTabs = line.count('\t')
    
    if currTabs <= prevTabs:
        for i in range((prevTabs - currTabs) + 1):
            if len(stack) > 0:
                stack.pop()

    parentDir = outputDir if currTabs == 0 else stack[-1]
    currDir = os.path.join(parentDir, line.strip())
    stack.append(currDir)
    
    prevTabs = currTabs

    try:
        os.mkdir(currDir)
    except OSError:
        pass
