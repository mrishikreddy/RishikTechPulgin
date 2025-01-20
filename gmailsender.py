import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl
import datetime
from email.utils import formataddr



# Email credentials and content
sender_name = "RishikTechAI"
sender_email = "rishiktechcore@gmail.com"  # Replace with your email
sender_password = "sabq jsgm puef nuip"  # Replace with your email password
recipient_email = "malerishikreddy@gmail.com"  # Replace with recipient email


time = datetime.datetime.now()
ddmm = str(time.day)+str(time.month)
d = {

    "201":["LeetCode topic: Prefix sum","Google NLP: Course Introduction and NLP on Google cloud","workon Portfolio website","Revise 2 LeetCode old problems"],
    "211":["LeetCode topic: Two Pointers","Update Resume","Google NLP: NLP with vertex AI","workon Portfolio website","Revise 2 LeetCode old problems"],
    "221":["LeetCode topic: Sliding Window","Apply for Internships","Google NLP: Text representation","workon Portfolio website","Revise 2 LeetCode old problems"],
    "231":["LeetCode topic: Fast & Slow Pointers","Apply for Internships","Google NLP: NLP models","workon Portfolio website","Revise 2 LeetCode old problems"],
    "241":["LeetCode topic: LinkedList In-place Reversal","workon LinkedIn profile,connections,jobs","Google NLP: Advanced NLP models","workon Portfolio website","Revise 2 LeetCode old problems"],
    "251":["LeetCode topic: Monotonic Stack","Apply for Internships","Google NLP: Course summary and Your next steps","IBM AI Engineering:Fundamentals of AI Agents Using RAG and LangChain","workon AI chatbot project","Revise 2 LeetCode old problems"],
    "261":["LeetCode topic: Top ‘K’ Elements","Update Resume","IBM AI Engineering: Generative AI Applications with RAG and LangChain","workon Portfolio website","workon AI chatbot project","Revise 2 LeetCode old problems"],
    "271":["LeetCode topic: Overlapping Intervals","Apply for Internships","IBM AI developer: Create Your Own ChatGPT-like Website and Create a Voice Assistant","workon Portfolio website","Revise 2 LeetCode old problems"],
    "281":["LeetCode topic: Modified Binary Search","Update Github","IBM AI developer: Generative AI-Powered Meeting Assistant","workon Portfolio website","Revise 2 LeetCode old problems"],
    "291":["LeetCode topic: Binary Tree Traversal","Apply for Internships","IBM AI developer: Summarize Your Private Data with Generative AI & RAG","workon Portfolio website","Revise 2 LeetCode old problems"],
    "301":["LeetCode topic: Depth-First Search (DFS)","Apply for Internships","IBM AI developer: Babel Fish with LLM and STT TTS","Revise 2 LeetCode old problems"],
    "311":["LeetCode topic: Breadth-First Search (BFS)","workon LinkedIn profile,connections,jobs","Revise 2 LeetCode old problems"],
    "12":["LeetCode topic: Matrix Traversal","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "22":["LeetCode topic: Backtracking","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "32":["LeetCode topic: Dynamic Programming Patterns: Fibonacci Sequence","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "42":["LeetCode topic: Kadane's Algorithm","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "52":["LeetCode topic: 0/1 Knapsack","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "62":["LeetCode topic: Unbounded Knapsack","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "72":["LeetCode topic: Longest Common Subsequence (LCS)","workon LinkedIn profile,connections,jobs","Learn React Native","Revise 2 LeetCode old problems"],
    "82":["LeetCode topic: Longest Increasing Subsequence (LIS)","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "92":["LeetCode topic: Palindromic Subsequence","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "102":["LeetCode topic: Edit Distance","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "112":["LeetCode topic: Subset Sum","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "122":["LeetCode topic: String Partition","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "132":["LeetCode topic: Catalan Numbers","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "142":["LeetCode topic: Matrix Chain Multiplication","workon LinkedIn profile,connections,jobs","Learn React Native","Revise 2 LeetCode old problems"],
    "152":["LeetCode topic: Count Distinct Ways","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "162":["LeetCode topic: DP on Grids","Update Resume/Update Github","Learn React Native","Revise 2 LeetCode old problems"],
    "172":["LeetCode topic: DP on Trees","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "182":["LeetCode topic: DP on Graphs","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "192":["LeetCode topic: Digit DP","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "202":["LeetCode topic: Bitmasking DP","Apply for Internships","Learn React Native","Revise 2 LeetCode old problems"],
    "212":["LeetCode topic: Probability DP","workon LinkedIn profile,connections,jobs","workon new project","Revise 2 LeetCode old problems"],
    "222":["LeetCode topic: State Machine DP","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "232":["3 LeetCode problems","Update Resume/Update Github","workon new project","Revise 2 LeetCode old problems"],
    "242":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "252":["3 LeetCode problems","Update Github","workon new project","Revise 2 LeetCode old problems"],
    "262":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "272":["3 LeetCode problems","Apply for Internships","workon new project","Revise 2 LeetCode old problems"],
    "282":["3 LeetCode problems","workon LinkedIn profile,connections,jobs","workon new project","Revise 2 LeetCode old problems"]
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
