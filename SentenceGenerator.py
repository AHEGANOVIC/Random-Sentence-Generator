import smtplib, ssl, random

# The paths which have the noun file, adjective file, and verb file
noun_file = r"YOUR PATH TO THE NOUN.TXT FILE"
adjective_file = r"YOUR PATH TO THE ADJECTIVE.TXT FILE"
verb_file = r"YOUR PATH TO THE VERB.TXT FILE"

# Various variables that help connect to outlook STMP's server 
smtp_server = "smtp-mail.outlook.com"
port = 587  # For starttls
sender_email = input("What email will you be using to send the auto generated emails?)
receiver_email = input("Who would you like to send this email to?")
password = input("Type your password and press enter: ")
context = ssl.create_default_context()

def randomizer(noun_file, adjective_file, verb_file): 
    
    # Opens set files with many adjectives, nouns, and verbs
    nouns = open(noun_file)
    adjectives = open(adjective_file)
    verbs = open(verb_file)

    # Sorts the list of each file so that one line will be able to be chosen
    noun_line = nouns.read().split("\n")
    adjective_line = adjectives.read().split("\n")
    verb_line = verbs.read().split("\n")

    # Random chooses one line in the entirety of the noun file, 4 lines will be randomly chosen
    noun_random = random.choice(noun_line)
    noun_random2 = random.choice(noun_line)
    noun_random3 = random.choice(noun_line)
    noun_random4 = random.choice(noun_line)

    # Random chooses one line in the entirety of the adjective file, 4 lines will be randomly chosen
    adjective_random = random.choice(adjective_line)
    adjective_random2 = random.choice(adjective_line)
    adjective_random3 = random.choice(adjective_line)
    adjective_random4 = random.choice(adjective_line)

    # Random chooses one line in the entirety of the verb file, 4 lines will be randomly chosen
    verb_random = random.choice(verb_line) 
    verb_random2 = random.choice(verb_line)
    verb_random3 = random.choice(verb_line)
    verb_random4 = random.choice(verb_line)

    # Files are closed
    nouns.close()
    adjectives.close()
    verbs.close()

    # Returns all saved variables so they can be used in the other functions 
    return noun_random, noun_random2, noun_random3, noun_random4, adjective_random, adjective_random2, adjective_random3, adjective_random4, verb_random, verb_random2,  verb_random3, verb_random4
  

def turns_sentence():
    
    # Allows user to choose how many different emails that they decide to send out 
    n = input("How many generated emails would you like to send?")
    
    # This function creates the randomly generated sentences and creates as many as the user previously wanted 
    for turn in range(int(n)):
        noun_random, noun_random2, noun_random3, noun_random4, adjective_random, adjective_random2, adjective_random3, adjective_random4, verb_random, verb_random2,  verb_random3, verb_random4 = randomizer(noun_file, adjective_file, verb_file)
        sentence_func_sender(noun_random, noun_random2, noun_random3, noun_random4, adjective_random, adjective_random2, adjective_random3, adjective_random4, verb_random, verb_random2,  verb_random3, verb_random4)
        

def sentence_func_sender(noun, adjective, verb, noun2, adjective2, verb2, noun3, adjective3, verb3, noun4, adjective4, verb4):
    
    # Sentence creation based on the randomly selected nouns, adjectives, and verbs
    sentence = f"The {noun} {adjective} {verb}. It {adjective2} and it {adjective3} helped in the action of {verb2}. Now, {noun2} and {noun3} are both {verb3} while {noun4} {adjective4} {verb4}" 
    
    # Preventing bug that will send original f-string instead of the auto generated email from previous function 
    if sentence == "The noun adjective verb. It adjective2 and it adjective3 helped in the action of verb2. Now, noun2 and noun3 are both verb3 while noun4 adjective4 verb4":
        exit()   
    
    # Creates basic email structure that will capture your auto generated sentence
    message = f"""\
        Subject: Hi there

        {sentence}."""  
    
    # Sends email out to whoever is chosen and connects securely to outlook's STMP server
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
    # In case of any errors that occur
    except Exception as e:
    # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 
    
# Functions called so that the file is ran 
randomizer(noun_file, adjective_file, verb_file)
turns_sentence()
sentence_func_sender('noun', 'adjective', 'verb', 'noun2', 'adjective2', 'verb2', 'noun3', 'adjective3', 'verb3', 'noun4', 'adjective4', 'verb4')
