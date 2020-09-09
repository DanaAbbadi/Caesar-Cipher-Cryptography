import nltk
nltk.download('words')

words_list= nltk.corpus.words.words()


def encrypt(msg,key):
    """
     Encrypt a massage using Ceasar Cipher, basically by shifting the msg by a certain number.

     Arguments:
        msg -- {string} the massage/phrase to be encrypted
        key -- {integer} Number of shifts
    
     Output:
        The encrypted massage 

    """
    encrypted_msg = ''
    msg = msg.lower()

    # in case key is larger than 26
    key = key % 26


    for char in msg:

        # if char is not a letter, just add it without shifting
        if ord(char) not in range(97, 123):
            encrypted_msg += char
        
        else:
            new_letter = (ord(char) + key) 

            # if new_letter exceeded alphabet range then repeat from the start
            if new_letter > 122:
                # Find how far char is from z letter(last letter in alphabet)
                dist_from_z = 122 - ord(char) 

                # How many steps needed
                steps = key - dist_from_z -1

                # Finally add the steps value to 'a' letter to repeat over
                start_from_a = 97 + steps

                encrypted_msg += chr(start_from_a)

            else:
                encrypted_msg += (chr(ord(char) + key))

    return encrypted_msg

def decrypt(msg,key):
    return encrypt(msg,-key)

def is_english(msg):
    """
     Will determine if a sentence is english or not, by counting english words inside.
     If half of the words are english, then the sentence is considered english.
    """
    words = msg.split()
  
    word_count = 0

    for word in words:
        if word in words_list:
            word_count += 1
    
    # if more than half of the words are english words consider text as english 
    # devide (how many words are english) over (how many words are in the sentence)
    if (word_count/len(words)) > 0.5:
        # print(words)
        return word_count
    else: 
        return 0



def cipher_breaker(msg):
    """
     This function breaks the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
     
     Algorithm:
        * we have 26 options (alphabet letters)
        * call decrypt 26 times
        * after each call, count how many english words are in the returned msg
        * keep a max_english value, will contain the sentance with the most english words (max)
        * after each is_english compare the count with max 
    """

    max = 0
    max_english_sentence = ''
    msg =msg.lower()
    for key in range(26):
        decrypted_msg = decrypt(msg ,(key))
        count_words = is_english(decrypted_msg)

        if count_words > max:
            max_english_sentence = decrypted_msg

    return max_english_sentence



if __name__ == "__main__":
    
    words_list= nltk.corpus.words.words()

    msg = encrypt('nice work',6)
    
    print(f'Encrypted msg is:  {msg}')
    print(f'Decrypted msg is:  {cipher_breaker(msg)}')
  

