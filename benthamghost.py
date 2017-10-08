#This is a program designed to 'simulate' the ghost of Jeremy Bentham, who has decided he will haunt UCL Society events
#Created by Chris, Nithin and Konrad on 07-10-2017
import datetime
import tweepy
import requests
import random
import json
import re
from datetime import timedelta

#Authorisations; will eventually want to movve this to another file
consumer_key = '8WEOJXx7LQqCQPcAuXEzPGRW4'
consumer_secret = 'mNMUCm0xTF0CO4cUbE3O2zS4qUVXqZ35qqks6riw6xcCqByCA7'
access_token = '916623899969904641-RTE5G4ONKebr4abWouqhqTxZ0VMmQhL'
access_token_secret = 'iuoaBzL7VWLSxLUNUKUvGkPVZpR7SMqOwtTuSBmpb1pxe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Gets the current date/time, along with the date/time in 24 hours, and converts into a string usable in the parameters
now = datetime.datetime.now()
s = str(now)

part1, part2 = s.split(' ')
part3, part4 = part2.split('.')
timeform = part1 + "T" + part3 + "+01:00"

tomorrow = now + timedelta(days=1)
t = str(tomorrow)
apart1, apart2 = t.split(' ')
apart3, apart4 = apart2.split('.')
endtimeform = apart1 + "T" + apart3 + "+01:00"

#Filters for Society events, for the current 24-hour period only
params = {
    "token" : "uclapi-7f533839ae57f3-b7a99752050ed2-ff055207f9cbec-4d64e6c02dd955",
    "start_datetime": timeform,
    "end_datetime": endtimeform,
    "contact": "Society"

}
r = requests.get("https://uclapi.com/roombookings/bookings", params=params)

#The sentence frameworks for Jeremy's tweets
openings = ["Can't wait to go to the ", "Who else is going to the ", "Hyped to go to the ", "Heading out to the ", "Might float on over to the ", "Gonna grab some I-scream before the ", "Think I'll haunt the ", "Gonna grab some boos from Phineas then head to the "]
endings = ["See you all there!", "Ghosts got to go places too!", "Who says ghosts can't attend events?", "Hope there's lots of cuties!", "Can't let you mortals have all the fun!", "Don't be alarmed at any supernatural occurences, it's just me!", "Let's gooooooo!", "Hopefully it won't rain today, that'd dampen my spirit...", "I'm gonna have a wail of a time!", "Hopefully the mood's not dead...", "Nice to see my uni's still going strong!", "I may be dead but I'm still full of life!"]
hindu_endings = ["Reincarnation is making a comeback!"]
drama_endings = ["Good luck pulling me off stage!", "Phantom of the Opera eh?", "Let's get dramatic!"]

#Picks an ending and opening line at random
openingsno = openings.__len__() - 1
endingsno = endings.__len__() - 1
hindu_endingsno = hindu_endings.__len__() - 1
drama_endingsno = drama_endings.__len__() - 1

j = r.json()
#Takes the number of available results and converts it into an integer value
nom = j['count']
num = int(nom) - 1
rand = random.randint(0,num) #Chooses the society that Jeremy will haunt that day

#Edits the contact element to only include the Society name
string_to_be_sliced = j['bookings'][rand]['contact']

society_name = re.findall(r'- (.*?) Society', string_to_be_sliced)

#Gives the options for society-specific endings
if 'Drama' in society_name:

    combined_endings = endings + drama_endings
    combined_endingsno = combined_endings.__len__() - 1

    formattedtweet = (openings[random.randint(0, openingsno)] + j['bookings'][rand]['roomname'] + " for the " + society_name[0] + " Society " + j['bookings'][rand]['description'] + " today! " + combined_endings[random.randint(0, combined_endingsno)] + "\n#UCL")

if 'Hindu' in society_name:

    combined_endings = endings + hindu_endings
    combined_endingsno = combined_endings.__len__() - 1

    formattedtweet = (openings[random.randint(0, openingsno)] + j['bookings'][rand]['roomname'] + " for the " + society_name[0] + " Society " + j['bookings'][rand]['description'] + " today! " + combined_endings[random.randint(0, combined_endingsno)] + "\n#UCL")

else:
    formattedtweet = (openings[random.randint(0, openingsno)] + j['bookings'][rand]['roomname'] + " for the " + society_name[0] + " Society " + j['bookings'][rand]['description'] + " today! " + endings[random.randint(0, endingsno)] + "\n#UCL")


#Constructs Jeremy's tweet for the day
format
#Publishes the constructed tweet. If desired, could be set to run daily, or at whatever desired interval, with the sleep command and a server
print(formattedtweet)
tweet = formattedtweet
api.update_status(status=tweet)
