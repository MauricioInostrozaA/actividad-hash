import math
import hashlib
import time

def entropy(hashtxt):
    uchar = len(set(hashtxt))
    E = len(hashtxt) * math.log(uchar,2)
    return(E)
######################
######## MD5 #########
def md5H(msg):
    md5 = hashlib.md5()
    md5.update(msg.encode('utf8'))
    r_md5 = md5.hexdigest()
    return(r_md5)

######################
####### SHA256 #######
def s256H(msg):
    s256 = hashlib.sha256()
    s256.update(msg.encode('utf8'))
    r_s256 = s256.hexdigest()
    return(r_s256)

######################
####### SHA256 #######
def sha1H(msg):
    sha1 = hashlib.sha1()
    sha1.update(msg.encode('utf8'))
    r_sha1 = sha1.hexdigest()
    return(r_sha1)
######################

if __name__ == '__main__':

    print("[1] MD5")
    print("[2] SHA1")
    print("[3] SHA256")
    print("[0] Exit")

    option = int(input("Enter your option: "))
    while option != 0:
        if option == 1:
            value = input("Input a file you wanna hඞsh: ")
            file1 = open(value, 'r')
            count = 0
            time1 = time.perf_counter()
            for line in file1:
                count += 1
                eline = line.strip()
                print("MD5| {} | {}".format(eline, md5H(eline)))
            print("Tiempo total: " + str(time.perf_counter() - time1) + "seg")

            break
        
        elif option == 2:
            value = input("Input a file you wanna hඞsh: ")
            file1 = open(value, 'r')
            count = 0
            time1 = time.perf_counter()
            for line in file1:
                count += 1
                eline = line.strip()
                print("SHA1| {} | {}".format(eline, sha1H(eline)))
            print("Tiempo total: " + str(time.perf_counter() - time1) + "seg")

            break

        elif option == 3:
            value = input("Input a file you wanna hඞsh: ")
            file1 = open(value, 'r')
            count = 0
            time1 = time.perf_counter()
            for line in file1:
                count += 1
                eline = line.strip()
                print("SHA256| {} | {}".format(eline, s256H(eline)))
            print("Tiempo total: " + str(time.perf_counter() - time1) + "seg")

            break
        
        else:
            print("Invalid option.")
            break


    print("cya ඞ")