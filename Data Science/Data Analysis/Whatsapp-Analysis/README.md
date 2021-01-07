# Whatsapp-Analysis
This project is created using Python libraries such as regex, matplotlib, emoji, pandas, and so on. It provides an exploratory data analysis and visualisation to understand the active members in the group.

# Overview
### Data Collection
You can export either a group chat WhatsApp conversation or altogether all the chats from WhatsApp. You can even capture the data using regular expressions.

### Data Preparation
The conversation can be automatically broken down to raw message into 4 tokens (date, time, author, message)
You can detext date and time(using regex), author (using regex), and the remaining string portion is the message
In order to split multi-line messages, each line can be broken based on separator(, / -) tokens and lastly capture all data in a tabular format

### Questions Answered
1. Who is highly talkative?
2. Number of messages with no authors(not a saved number)? 
3. What is the letter count and word count of each message? 
4. What is the Total word count in the entire conversation? 
5. Number of words vs author and Number of messages vs date?
6. Number of messages vs time? Number of messages vs hour of the day? 
7. Who deleted how many messages? 
8. Which are the top 5 emojis used by a person? 
9. Who sent how many media files?

*Any improvement or feedback is welcome!*
