import requests
import time
import random

print("Since you ba****ds do cp, we expect you to provide the correct handle of yours. Else fuck off!")
usr1 = input("Enter contestant 1 handle : ")
usr2 = input("Enter contestant 2 handle : ")
noOfProb = input("Enter number of problems u wish to solve : ")
rating = input("Enter the rating u wish to solve : ")

res = requests.get("https://codeforces.com/api/problemset.problems")
data = res.json()

problems = data["result"]["problems"]

filtered = [
    p for p in problems
    if "rating" in p and p["rating"] == int(rating)
]


totProb = len(filtered)
p1 = 1
p2 = 0
for i in range(int(noOfProb)):

    if(i == 0):
        contId = str(1450)
        probInd = "B"
    else:
        probNo = random.randint(1, totProb)
        contId = str(filtered[probNo - 1]["contestId"])
        probInd = str(filtered[probNo - 1]["index"])

    probLink = "https://codeforces.com/problemset/problem/" + contId + "/" + probInd
    print(probLink)



    while True:
        l1 = "https://codeforces.com/api/user.status?handle=" + usr1 + "&from=1&count=10"
        status1 = requests.get(l1)
        s1Data = status1.json()
        results1 = s1Data["result"]
        slvd1 = [r1 for r1 in results1 if r1["problem"]["contestId"] == int(contId) and r1["problem"]["index"] == probInd and r1["verdict"] == "OK"]

        time.sleep(2)
        l2 = "https://codeforces.com/api/user.status?handle=" + usr2 + "&from=1&count=10"
        status2 = requests.get(l2)
        s2Data = status2.json()
        results2 = s2Data["result"]
        slvd2 = [r2 for r2 in results2 if r2["problem"]["contestId"] == int(contId) and r2["problem"]["index"] == probInd and r2["verdict"] == "OK"]


        if slvd1 and not slvd2:
            print("Solved by " + usr1)
            p1 += 1
            break
        elif slvd2 and not slvd1:
            print("Solved by " + usr2)
            p2 += 1
            break
        
        if slvd1 and slvd2:
            if slvd1[0]["id"] < slvd2[0]["id"]:
                print("Solved by " + usr1)
                p1 += 1
                break
            elif slvd2[0]["id"] < slvd1[0]["id"]:
                print("Solved by " + usr2)
                p2 += 1
                break


        print("Checking...")
        time.sleep(2)


print(usr1 + " : " + str(p1) + "\n" + usr2 + " : " + str(p2))
