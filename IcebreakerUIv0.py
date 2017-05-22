# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:48:12 2016

@author: kramerPro
"""
'''
Node interface prototype
'''

##example
#import time
#import sys
#
#print "Please enter your name."
#userName=raw_input();
#print "Now let's wait a few seconds, {}.".format(userName)
#sys.stdout.flush() # <- *** it goes here ***
#time.sleep(3)
#print "Did you lose your patience?"


#file in working directory

import pickle
import sys
import time
import random

# adding to pickle a first answer
response_list = []
email_list = []
ans = "I struggle with procrastination. Over and over again I've watched opportunities pass away because of my inability to work on a project when I want to. I feel like a slave because I don't have the freedom to do what I want with my life. No matter how many times I try to change my behaviour; I find myself putting off work for days, weeks, sometimes years things I need to do. Instead of doing whatever task is at hand, I'll find myself oversleeping, or watching Netflix. It's not even interesting. Do you have any experience with this? What works for you?"
ans1 = 'kramer102@gmail.com'
response_list.append(ans)
email_list.append(ans1)
# need to save a list of answers and index of response the answer is to
answer_list = []
with open('response.txt', 'wb') as res:
    pickle.dump(response_list, res)
    pickle.dump(email_list, res)
    pickle.dump(answer_list, res)

def get_data():
    with open('response.txt', 'rb') as f:
        response_list = pickle.load(f)
        email_list = pickle.load(f)
        answer_list = pickle.load(f)
    return response_list, email_list, answer_list

def store_data(response_list, email_list, answer_list):
    with open('response.txt', 'wb') as f:
        pickle.dump(response_list, f)
        pickle.dump(email_list, f)
        pickle.dump(answer_list, f)

def smile_response(response_list, email_list, answer_list):
    print("Thank You")
    sys.stdout.flush()
    time.sleep(1)
    print("I couldn't have done it without you!")
    sys.stdout.flush()
    time.sleep(1)
    print("My heart broke while worrying about my friend's problem")
    sys.stdout.flush()
    time.sleep(1)
    print('')
    print("Could you help with this: ")
    i = random.randint(0,len(response_list)-1)
    print(response_list[i])
    print('')
#    print("type yes or no. Hit return when finished")
#    ans1 = raw_input()
#    if ans1 != 'yes':
#        print"awe shucks, well have a nice day"
#        return
    print('Please type a helpful response and only press return when finished')
    ans2 = raw_input()
    answer_list.append([ans2,i])
    print("Thank You So MUCH!!!")
    sys.stdout.flush()
    time.sleep(1)
    print("You must have something you're struggling with too")
    sys.stdout.flush()
    time.sleep(1)
    print("Type in a summary and ask a question then press return")
    ans3 = raw_input()
    response_list.append(ans3)
    print("I'll have to ask around and think about it")
    sys.stdout.flush()
    time.sleep(1)
    print("If you give me your email address, I'll get back to you when I get an answer")
    sys.stdout.flush()
    time.sleep(1)    
    print("I'll do my very best to keep it a secret, but I'm sorry I can't guarantee it")
    sys.stdout.flush()
    time.sleep(1)    
    print("Is that okay? please type yes or no and then hit return")
    ans4 = raw_input()
    if ans4 != 'yes':
        print"awe shucks, well have a nice day"
        return
    print("Great! Enter your email and press return")
    ans5 = raw_input()
    email_list.append(ans5)
    print("Thanks for all your help! Hopefully we can help each other again!")
    
    store_data(response_list, email_list, answer_list)
    
def run():
    while True:
        response, email, answers = get_data()
        smile_response(response, email, answers)
        print("HELP......HELP.......HELP \n\n\n\n\n\n\n")
        a = raw_input()
        
