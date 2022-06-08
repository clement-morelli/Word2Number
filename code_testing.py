import requests 

#this is a program to test the rest api word2number

#you need to install requests on your local computer with : pip install requests

#first modify the ip adress of the api [ipaddress]
#second modify the port to access of the api [port]
#you can modify listOfTest, which is a list of couple [test,the real result]

#to run the program just try : python3 code_testing.py 


########################Params########################
listOfTest = [["chsb","38192"],["ready","ok"],["2 Dads & 2 Moms","241419213151319"],["Dad","414"],["Dad","41123454"]]

ipaddress = "192.168.59.142"

port = "32369"
######################################################


########################Variables#####################
listfortraitement = ['status','result','{','}',' ',':','\n','"']
listOfTestFailed = []
succeded = 0
numberOfTest = len(listOfTest)
######################################################


########################Traitement####################
for i in listOfTest:
    test = i[0]
    result = i[1]
    response = requests.get("http://"+ipaddress+":"+port+"/"+test)
    response = response.text
    print(response)
    for i in listfortraitement:
        response = response.replace(i,'')
    if response == result:
        succeded += 1
    else :
        listOfTestFailed.append(test)
######################################################


########################Print#########################
print(str(succeded) + " out of "+ str(numberOfTest) + " passed")

if len(listOfTestFailed) != 0:
    print("Test Failed are "+ str(listOfTestFailed))
######################################################




