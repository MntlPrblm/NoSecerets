import os
import hashlib
from time import sleep
from colorama import Fore

def clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')

hash_choice = 'md5'
hashtype = hashlib.md5
path_to_wordlist = "Not configured"
path_to_hashes = "Not configured"
vivacious = False
encodefilename = "Not configured"
save_encode = "False"
encoded_wordlist = "Not configured"

titlescreen = Fore.LIGHTRED_EX+"""
 _,  _,____, ____,____,____,____,____, ____,____,____, 
(-|\ |(-/  \(-(__(-|_,(-/  (-|_,(-|__)(-|_,(-|  (-(__  
 _| \|,_\__/,____)_|__,_\__,_|__,_|  \,_|__,_|,  ____) 
(     (     (    (    (    (    (     (    (    (    

By MntlPrblm, https://github.com/MntlPrblm
"""

def start():
    if os.path.exists('encoded.txt') == True:
        os.remove('encoded.txt')
    global path_to_wordlist, path_to_hashes, vivacious, encodefilename, save_encode, encoded_wordlist, hashtype, hash_choice
    clear()
    print(titlescreen)
    print(Fore.LIGHTWHITE_EX+"=================================")
    print(Fore.LIGHTRED_EX+"REQUIRED")
    print(Fore.LIGHTCYAN_EX+"Wordlist [1]: "+path_to_wordlist)
    print(Fore.LIGHTCYAN_EX+"Hashes [2]: "+path_to_hashes)
    print(Fore.LIGHTWHITE_EX+"==================================")
    print(Fore.LIGHTWHITE_EX+"OPTIONS")
    print(Fore.LIGHTCYAN_EX+"Vivacious mode [3]: "+str(vivacious))
    print(Fore.LIGHTCYAN_EX+"Save encode [4]: "+str(save_encode))
    print(Fore.LIGHTCYAN_EX+"Entry name: "+encodefilename)
    print(Fore.LIGHTCYAN_EX+"Load encoded wordlist [5]: "+encoded_wordlist)
    print(Fore.LIGHTWHITE_EX+"===================================")
    print(Fore.LIGHTCYAN_EX+"Hash type [6]: "+hash_choice)
    print(Fore.LIGHTCYAN_EX+"Show files [7]")
    print(Fore.LIGHTCYAN_EX+"Exit [0]")
    print(Fore.LIGHTRED_EX+"Type "+Fore.LIGHTWHITE_EX+"start"+Fore.LIGHTRED_EX+" to begin attack")
    print("")



    choice = input(Fore.LIGHTWHITE_EX+"Input: ")

    if choice == '1':
        path_to_wordlist = input("Path to wordlist: ")
        if os.path.exists(path_to_wordlist) == False:
            print("Wordlist not found")
            sleep(1)
            path_to_wordlist = "Not configured"
            start()
        start()
    if choice == '2':
        path_to_hashes = input("Path to hashes: ")
        if os.path.exists(path_to_hashes) == False:
            print("Hashes not found")
            sleep(1)
            path_to_hashes = "Not configured"
            start()
        start()
    if choice == '3':
        if vivacious == False:
            vivacious = True
        else:
            vivacious = False
        start()
    if choice == '4':
        if save_encode == True:
            encodefilename = 'Not configured'
            save_encode = False
            start()
        else:
            encodefilename = input("Entry name: ")
            save_encode = True
            start()
    if choice == '5':
        if path_to_hashes == "Not configured":
            print("Please configure hashes first")
            sleep(2)
            start()
        if path_to_wordlist == "Not configured":
            print("Please configure wordlist first")
            sleep(2)
            start()
        encoded_wordlist = input("Path to encoded wordlist: ")
        if os.path.exists(encoded_wordlist) == False:
            print("Encoded wordlist not found")
            sleep(2)
            encoded_wordlist = 'Not configured'
            start()
        f = open(encoded_wordlist, 'r', encoding='utf-8')
        encoded_entries = f.read().splitlines()
        f.close()
        f = open(path_to_hashes, 'r')
        hashes = f.read().splitlines()
        f.close
        f = open(path_to_wordlist, 'r', encoding='utf-8')
        wordlist = f.read().splitlines()
        f.close
        for hash in hashes:
            spot = 0
            for encoded_entry in encoded_entries:
                spot += 1
                if hash == encoded_entry:
                    with open('cracked.txt', 'a') as f:
                        f.write(hash+": "+wordlist[spot-1])
                        f.write('\n')
                        f.close
                    print(hash+": "+wordlist[spot-1])
        print("")
        print("Finished cracking!")
        print("Cracked hashes in cracked.txt")
        input("Press enter to continue: ")
        start()

    if choice == '6':
        hash_choice = input("Hash type: ")
        if hash_choice == "md5":
            hashtype = hashlib.md5
            start()
        if hash_choice == "sha224":
            hashtype = hashlib.sha224
            start()
        if hash_choice == "sha1":
            hashtype = hashlib.sha1
            start()
        if hash_choice == "sha256":
            hashtype = hashlib.sha256
            start()
        if hash_choice == "sha384":
            hashtype = hashlib.sha384
            start()
        if hash_choice == "sha512":
            hashtype = hashlib.sha512
            start()
        if hash_choice == "blake2b":
            hashtype = hashlib.blake2b
            start()
        if hash_choice == "blake2s":
            hashtype = hashlib.blake2s
            start()
        if hash_choice == "sha3_224":
            hashtype = hashlib.sha3_224
            start()
        if hash_choice == "sha3_256":
            hashtype = hashlib.sha3_256
            start()
        if hash_choice == "sha3_384":
            hashtype = hashlib.sha3_384
            start()
        if hash_choice == "sha3_512":
            hashtype = hashlib.sha3_512
            start()
        if hash_choice == "shake_128":
            hashtype = hashlib.shake_128
            start()
        if hash_choice == "shake_256":
            hashtype = hashlib.shake_256
            start()
        print("Please only enter hashes that are: sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, md5, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, or shake_256")
        sleep(3)
        start()

    if choice == '7':
        print(os.listdir())
        input("Press enter to continue")
        start()
    if choice == '0':
        quit()

    if choice != "start":
        print("Invalid command")
        sleep(0.5)
        start()
    if path_to_wordlist == "Not configured":
        print("Please configure wordlist first")
        sleep(2)
        start()
    if path_to_hashes == "Not configured":
        print("Please configure hashes")
        sleep(2)
        start()
    try:
        f = open(path_to_wordlist, 'r', encoding='utf-8')
        wordlist = f.read().splitlines()
        f.close
    except:
        f = open(path_to_wordlist, 'r', encoding='latin')
        wordlist = f.read().splitlines()
        f.close      

    print("Encoding...")
    for string in wordlist:
        hash_object = hashtype(string.encode())
        hash = hash_object.hexdigest()
        if vivacious == True:
            print(string+": "+hash)
        if save_encode == True:
            with open(encodefilename+'ENCODED.txt','a') as f:
                f.write(hash)
                f.write('\n')
        else:
            with open('encoded.txt', 'a') as f:
                f.write(hash)
                f.write('\n')
    print("Finished encoding!")
    sleep(2)

    print("Cracking... you cant hide from me :)")
    f = open(path_to_hashes, 'r')
    hashes = f.read().splitlines()
    f.close
    if save_encode == True:
        f = open(encodefilename+'ENCODED.txt', 'r')
        encoded_entries = f.read().splitlines()
        f.close()
    else:
        f = open('encoded.txt', 'r')
        encoded_entries = f.read().splitlines()
        f.close()
    for hash in hashes:
        spot = 0
        for encoded_entry in encoded_entries:
            spot += 1
            if hash == encoded_entry:
                with open('cracked.txt', 'a') as f:
                    f.write(hash+": "+wordlist[spot-1])
                    f.write('\n')
                    f.close
                print(hash+": "+wordlist[spot-1])
    print("")
    print("Finished cracking!")
    print("Cracked hashes in cracked.txt")
    input("Press enter to continue: ")
    if os.path.exists('encoded.txt') == True:
        os.remove('encoded.txt')
    start()
    




    
    

if __name__ == '__main__':
    start()
