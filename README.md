# NoSecerets
NoSecerets is a python script that is designed to crack hashes extremely fast. Faster even than Hashcat

# How does it work?
Instead of taking every word out of a wordlist  
and comparing it to the hash separately, the  
script simply encrypts the entire file at once,  
which makes it so that if you use the same wordlist  
twice, it can crack hashes almost instantly no matter  
the size of the wordlist

![alt text](https://github.com/MntlPrblm/NoSecerets/blob/main/screenshots/nosecerets.PNG)

![alt text](https://github.com/MntlPrblm/NoSecerets/blob/main/screenshots/nosecerets1.PNG)

# Usage
git clone https://github.com/MntlPrblm/NoSecerets.git  
cd NoSecerets  
pip install -r requirements.txt  
python main.py  
