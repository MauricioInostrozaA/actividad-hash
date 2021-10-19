import math
import hashlib
import time

def entropy(hashtxt):
    uchar = len(set(hashtxt))
    E = len(hashtxt) * math.log(uchar,2)
    return(E)

text = input("string a hashear: ")
######################
######## MD5 #########
time1 = time.perf_counter()
md5 = hashlib.md5()
md5.update(text.encode('utf8'))
r_md5 = md5.hexdigest()
e_md5 = entropy(r_md5)
print("MD5| {} | {} | {} | {}seg".format(text, r_md5, e_md5, (time.perf_counter() - time1)))

######################
####### SHA256 #######
time2 = time.perf_counter()
s256 = hashlib.sha256()
s256.update(text.encode('utf8'))
r_s256 = s256.hexdigest()
e_s256 = entropy(r_s256)
print("SHA256| {} | {} | {} | {}seg".format(text, r_s256, e_s256, (time.perf_counter() - time2)))

######################
####### SHA256 #######
time3 = time.perf_counter()
sha1 = hashlib.sha1()
sha1.update(text.encode('utf8'))
r_sha1 = sha1.hexdigest()
e_sha1 = entropy(r_sha1)
print("SHA1| {} | {} | {} | {}seg".format(text, r_sha1, e_sha1, (time.perf_counter() - time3)))
######################




