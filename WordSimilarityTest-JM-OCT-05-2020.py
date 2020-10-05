#so this is how it works:
#it will calculate two different metrics
#the first being how much overlap in distinct words there are, regardless of usage counts of each, this is the word_simi object
#the second being the overlap of total words; this one does take into account how many times each word is used, this is the word_count_simi object
#these two are not weighted equally in the final score
#originally created in python 3.8
#
from time import sleep #importing to be able to use the sleep function
user_input1 =''; user_input2 = '' #empty input variables, to loop/validate input
while not user_input1 or not user_input2: #if there's an empty value entered, it will ask them to try again
    user_input1 = input('Please input text to compare.\n')
    user_input2 = input('Please input your second text to compare.\n')
    if user_input1 == '' or user_input2 == '':
        print("Looks like you forgot to input some values, let's try that again.",end='\n\n')
user_input1 = user_input1.strip() #strips any leading and trailing whitespace that may have been accidentally entered
user_input2 = user_input2.strip()
user_input1 = user_input1.replace(',',' ,')#seperating punctuation from texts
user_input2 = user_input2.replace(',',' ,')
user_input1 = user_input1.replace('.',' .')
user_input2 = user_input2.replace('.',' .')
user_input1 = user_input1.replace(':',' :')
user_input2 = user_input2.replace(':',' :')
user_input1 = user_input1.replace('  ',' ')#replaces double spaces with single space
user_input2 = user_input2.replace('  ',' ')
user_input1 = user_input1.strip() #strips any leading or trailing blank spaces that may have been added by seperation process
user_input2 = user_input2.strip()
print('Analyzing Data...') #for excitement
sleep(1) #intentional delay, adds suspense
print('Almost there...')
sleep(1)
user_input1_low = user_input1.lower(); user_input2_low = user_input2.lower() #lowers the strings,
input1_low_list = user_input1_low.split(' ') #inputs the words into list
input2_low_list = user_input2_low.split(' ')
input1_low_set = set(input1_low_list) #copies the lists into sets, so that only unique values exist, will be used for word_simi
input2_low_set = set(input2_low_list)
input1_dict = {} #initializing empty dictionaries to insert into later
input2_dict = {}
equal_word_count = 0 #for word_count_simi, number of instances of matching words
total_word_count = len(input1_low_list) + len(input2_low_list) #for word_count_simi, calculates the total number of words
word_simi_count = 0
set_lengths = len(input1_low_set) + len(input2_low_set)
for word in input1_low_set: #looping, to start comparing the overlap in unique words, aka word_simi
    if word in input2_low_set:
        word_simi_count += 2
word_simi = word_simi_count / set_lengths #the number for overlap in distinct words
for word in input1_low_set: #next two for statements input the word counts into dictionaries, with the word itself as the key and the count as the value
    input1_dict.update({word: input1_low_list.count(word)})
for word in input2_low_set:
    input2_dict.update({word: input2_low_list.count(word)})
for entry in input1_dict.keys(): #decides what to do when comparing the word counts between text, if no match then it skips loop, otherwise chooses the lesser of the two and doubles it
    if entry not in input2_dict.keys():
        continue
    if input1_dict[entry] == input2_dict[entry]:
        equal_word_count += (input1_dict[entry] + input2_dict[entry])
    if input1_dict[entry] > input2_dict[entry]:
        equal_word_count += (input2_dict[entry] * 2) #if a word appears 3 times in one text, and 2 times in another, it should count as 4 matching for the word count 
    if input2_dict[entry] > input1_dict[entry]:
        equal_word_count += (input1_dict[entry] * 2)
word_count_simi = equal_word_count / total_word_count
final_percent = (word_count_simi * 0.8) + (word_simi * 0.2) #adds the two in a weighted manner for the final score
if user_input1 == user_input2:
    print('Well would you look at that, a perfect match.','The similarity score is: 1',sep='\n') #if two inputs are exactly the same this message will appear
elif user_input1.lower() == user_input2.lower():
    print('Cheeky, who would have thunk it, same text, just different capitalization.','The similarity score is: 0.95',sep='\n') #not optimal hardcoding a value if the only difference is capitalization, but a distinction still ought be made
else:
    print('Not quite the same.', 'The similarity score is: ',  round(final_percent,2))#otherwise it will display the weighted calculated value
#print(word_count_simi, word_simi)
user_input2 = input('Enter Q to quit\n') #so ends my first program