import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl
import datetime
from email.utils import formataddr
import os 

sender_name = "RishikTechAI"
sender_email = os.getenv("SENDER_MAIL") 
sender_password = os.getenv("SENDER_PASSWORD")  
recipient_email = os.getenv("DESTINATION_MAIL")  

time = datetime.datetime.now()
ddmm = str(time.day)+str(time.month)

d = {
    "241":["LeetCode topic: Fast & Slow Pointers","complete Portfolio website in 3 days","Revise 2 LeetCode old problems","completelly apply to all available internships right today"],
    "251":["LeetCode topic: LinkedList In-place Reversal","workon LinkedIn profile,connections,jobs","complete Portfolio website in 2 days","Revise 2 LeetCode old problems"],
    "261":["LeetCode topic: Monotonic Stack","Apply for Internships","complete Portfolio website today","Revise 2 LeetCode old problems","Check and update Rishik Tech Mail Sender(RTMS)"],

    "271":["LeetCode topic: Top ‘K’ Elements","Update Resume","prepare for launching portfolio website","workon Portfolio website","workon AI chatbot project","Revise 2 LeetCode old problems"],
    "281":["LeetCode topic: Overlapping Intervals","Apply for Internships","start launching portfolio website: lauch a demo","Revise 2 LeetCode old problems"],
    "291":["LeetCode topic: Modified Binary Search","Update Github","start launching portfolio website: lauch a demo","Revise 2 LeetCode old problems"],
    "301":["LeetCode topic: Binary Tree Traversal","Apply for Internships","launch portfolio website","Revise 2 LeetCode old problems"],
    "311":["LeetCode topic: Depth-First Search (DFS)","Apply for Internships","launch portfolio website","Revise 2 LeetCode old problems"],
    "12":["LeetCode topic: Breadth-First Search (BFS)","workon LinkedIn profile,connections,jobs","post about portfolio website on LinkedIn","Revise 2 LeetCode old problems"],
    "22":["LeetCode topic: Matrix Traversal","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems","update RTMS"],

    "32":["LeetCode topic: Backtracking","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "42":["LeetCode topic: Dynamic Programming Patterns: Fibonacci Sequence","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "52":["LeetCode topic: Kadane's Algorithm","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "62":["LeetCode topic: 0/1 Knapsack","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "72":["LeetCode topic: Unbounded Knapsack","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "82":["LeetCode topic: Longest Common Subsequence (LCS)","workon LinkedIn profile,connections,jobs","Learn React Native","Revise 2 LeetCode old problems"],
    "92":["LeetCode topic: Longest Increasing Subsequence (LIS)","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems","update RTMS"],

    "102":["LeetCode topic: Palindromic Subsequence","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "112":["LeetCode topic: Edit Distance","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "122":["LeetCode topic: Subset Sum","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "132":["LeetCode topic: String Partition","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "142":["LeetCode topic: Catalan Numbers","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "152":["LeetCode topic: Matrix Chain Multiplication","workon LinkedIn profile,connections,jobs","Learn React Native","Revise 2 LeetCode old problems"],
    "162":["LeetCode topic: Count Distinct Ways","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems","update RTMS"],

    "172":["LeetCode topic: DP on Grids","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "182":["LeetCode topic: DP on Trees","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "192":["LeetCode topic: DP on Graphs","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "202":["LeetCode topic: Digit DP","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "212":["LeetCode topic: Bitmasking DP","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "222":["LeetCode topic: Probability DP","workon LinkedIn profile,connections,jobs","workon new project","Revise 2 LeetCode old problems"],
    "232":["LeetCode topic: State Machine DP","Apply for Internships","workon new project","Revise 2 LeetCode old problems","update RTMS"],

    "242":["3 LeetCode problems","Update Resume/Update Github","workon new project","Revise 2 LeetCode old problems"],
    "252":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "262":["3 LeetCode problems","Update Github","workon new project","Revise 2 LeetCode old problems"],
    "272":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "282":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
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
