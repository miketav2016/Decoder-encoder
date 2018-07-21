
alfabit_elementary = [x for x in input()]
alfabit_finished = [x for x in input()]

string_elementary = [x for x in input()]
string_finished = [x for x in input()]

encryption={}
for i in range(len(alfabit_finished)):
    encryption[alfabit_elementary[i]]=alfabit_finished[i]

decryption={}
for i in range(len(alfabit_finished)):
    decryption[alfabit_finished[i]]=alfabit_elementary[i]

string_encryption=''
for i in range(len(string_elementary)):
        string_encryption+=encryption[string_elementary[i]]

string_decryption=''
for i in range(len(string_finished)):
        string_decryption+=decryption[string_finished[i]]

print(string_encryption)
print(string_decryption)


