from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')
client = genai.Client(api_key=API_KEY)

prompt = """
I'm working on a CTF challenge and need a detailed analysis. 
Please provide your analysis following this structure:

[분석을 한국어로 제공해주시기 바랍니다]

Challenge Details:
- Category: {problem_category}
- Tech Stack: {problem_tech_stack}
  * If version information is provided, please include:
    - Known CVEs for this version
    - Specific version vulnerabilities
    - Common exploit patterns
- Objective: {problem_goal}

Here's the code to analyze:
{problem_code}

Please ensure your analysis includes:
1. Code Analysis (코드 분석)
   - Logic flow and potential vulnerabilities
   - Suspicious functions or patterns
   - Input handling weaknesses

2. Version-specific Analysis (버전 관련 분석)
   - CVE details if version information is available
   - Historical vulnerabilities in the tech stack
   - Known exploit techniques for identified CVEs
   - Mitigation status and patch information

3. Exploitation Path (공격 방법)
   - Step-by-step approach to exploitation
   - Required conditions or prerequisites
   - Potential limitations or challenges
   - Tools or scripts needed

If no version information is provided, please focus on general vulnerability patterns and potential security issues in the code.
"""

problem_category = 'WEB'
problem_tech_stack = 'python 3.8, flask, etc..'
problem_goal = 'find flag'
problem_code = '''
code...



'''

response = client.models.generate_content(
    model='gemini-2.0-pro-exp-02-05',
    contents=prompt.format(problem_category=problem_category, problem_tech_stack=problem_tech_stack, problem_goal=problem_goal, problem_code=problem_code)
)

print(response.text)