import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl
import datetime
from email.utils import formataddr
import os 

sender_name = "Rishik Tech Assistant"
sender_email = os.getenv("SENDER_MAIL") 
sender_password = os.getenv("SENDER_PASSWORD")  
recipient_email = os.getenv("DESTINATION_MAIL")  

time = datetime.datetime.now()
ddmm = str(time.day)+str(time.month)

d = {
    
    "291":["LeetCode topic: Top 'k' elements",          "Build Rishik Portfolio and Gen AI application: 8 days Remaining", "Apply for Internships"],
    "301":["LeetCode topic: Overlapping Intervals",     "Build Rishik Portfolio and Gen AI application: 7 days Remaining", "Apply for Internships"],
    "311":["LeetCode topic: Modified Binary Search",    "Build Rishik Portfolio and Gen AI application: 6 days Remaining", "Apply for Internships"],
    "12":["LeetCode topic: Binary Tree Traversal",      "Build Rishik Portfolio and Gen AI application: 5 days Remaining", "Prepare an Introduction speech", "Post on Instagram"],
    "22":["LeetCode topic: Depth-First Search (DFS)",   "Update Rishik Tech Assistant(optional)", "Movie Night 🥳", ],


    "32":["LeetCode topic: Breadth-First Search (BFS)", "Build Rishik Portfolio and Gen AI application: 3 days Remaining", "Apply for Internships", "Form a Github Profile: 1day remaining", "Start going to GYM"]
    "42":["LeetCode topic: Matrix Traversal",           "Build Rishik Portfolio and Gen AI application: 2 days Remaining", "Apply for Internships", "Form a Github Profile"],
    "52":["LeetCode topic: Backtracking",                "Build Rishik Portfolio and Gen AI application: 1 day Remaining", "Apply for Internships", "workon on LinkedIn"],
    "62":["LeetCode topic: Dynamic Programming Patterns: Fibonacci Sequence",   "Launch Portfolio and Gen AI application ✨", "Apply for Internships"],
    "72":["LeetCode topic: Kadane's Algorithm",         "Update Github and LinkedInd with information about latest project", "Apply for Internships"],
    "82":["LeetCode topic: 0/1 Knapsack",               "Revise 2 LeetCode old problems", "Update Resume", "Post on Instagram" ],
    "92":["LeetCode topic: Unbounded Knapsack",         "Revise 2 LeetCode old problems", "Update Rishik Tech Assistant(optional)", "Movie Night 🥳"],


    "102":["LeetCode topic: Longest Common Subsequence (LCS)",      "Revise 2 LeetCode old problems", "Build contactless web application: 9 days Remaining", "Apply for Internships", "Start going to GYM"]
    "112":["LeetCode topic: Longest Increasing Subsequence (LIS)",  "Revise 2 LeetCode old problems", "Build contactless web application: 8 days Remaining", "Apply for Internships", "workon on Github Profile" ],
    "122":["LeetCode topic: Palindromic Subsequence",               "Revise 2 LeetCode old problems", "Build contactless web application: 7 days Remaining", "Apply for Internships", "workon on LinkedIn"],
    "132":["LeetCode topic: Edit Distance",                         "Revise 2 LeetCode old problems", "Build contactless web application: 6 days Remaining", "Apply for Internships",],
    "142":["LeetCode topic: Subset Sum",                            "Revise 2 LeetCode old problems", "Build contactless web application: 5 days Remaining", "Apply for Internships" ],
    "152":["LeetCode topic: String Partition",                      "Revise 2 LeetCode old problems", "Build contactless web application: 4 days Remaining", "Apply for Internships", "Post on Instagram" ],
    "162":["LeetCode topic: Catalan Numbers",                       "Revise 2 LeetCode old problems", "Update Rishik Tech Assistant(optional)", "Movie Night 🥳"],


    "172":["LeetCode topic: Matrix Chain Multiplication",           "Revise 2 LeetCode old problems", "Build contactless web application: 2 days Remaining",               "Apply for Internships", "Start going to GYM"]
    "182":["LeetCode topic: Count Distinct Ways",                   "Revise 2 LeetCode old problems", "Build contactless web application: 1 day Remaining",                "Apply for Internships", "workon on Github Profile"],
    "192":["LeetCode topic: DP on Grids"                            "Revise 2 LeetCode old problems", "Launch contactless web application ✨",                             "Apply for Internships", "workon on LinkedIn" ],
    "202":["LeetCode topic: DP on Trees",                           "Revise 2 LeetCode old problems", "Update Github and LinkedInd with information about latest project", "Apply for Internships" ],
    "212":["LeetCode topic: DP on Graphs",                          "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"                        "Update Resume"],
    "222":["LeetCode topic: Digit DP",                              "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"                        "Apply for Internships", "Post on Instagram"],
    "232":["LeetCode topic: Bitmasking DP",                         "Revise 2 LeetCode old problems", "Update Rishik Tech Assistant(optional)", "Movie Night 🥳"],


    "242":["LeetCode topic: Probability DP",                           "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"   "Apply for Internships", "Start going to GYM"],
    "252":["LeetCode topic:State Machine DP",                          "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"   "Apply for Internships"],
    "262":["Do 3 LeetCode Problems", "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"                                     "Apply for Internships"],
    "272":["Do 3 LeetCode Problems", "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"                                     "Apply for Internships"],
    "282":["Do 3 LeetCode Problems", "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos"]
    "13": ["Do 3 LeetCode Problems", "Revise 2 LeetCode old problems", "watch and learn the React Native: 10 videos", "Post on Instagram"]
    "
}

tasks = d.get(ddmm, ["No tasks for today"])

subject = "Your Tasks for Today"
html_content = f"""
<html>
    <body>
        <h1>Hello Boss!</h1>
        <h3>Here are your tasks for today:</h3>
        <ul>
            {''.join(f'<li>{task}</li>' for task in tasks)}
        </ul>
        <br/>
        <a href="https://drive.google.com/file/d/1gxBEQvYNQ8pbkBIJzihSyzIhmae3ndQ8/view?usp=sharing" style="display: inline-block; padding: 10px 20px; background-color: black; color: white; text-decoration: none; border-radius: 5px;">Know more</a>
        <h5>Complete these tasks with first priority, Have a good day</h5> 
        <h5>Happy coding 😊</h5>
    </body>
</html>
"""


# Create the email content
message = MIMEMultipart("alternative")
message["From"] = formataddr((sender_name, sender_email))
message["To"] = recipient_email
message["Subject"] = Header(subject, "utf-8")

# Attach the HTML content to the email
html_part = MIMEText(html_content, "html", "utf-8")
message.attach(html_part)

# Establish a secure connection using SSL and send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())