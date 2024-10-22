Vulnerability Scanner Test Repository
This repository is designed to provide sample vulnerable code snippets and configurations for testing different types of security scanners, such as SAST (Static Application Security Testing), secret scanners, PII scanners, and others. It contains intentionally insecure code and configurations to trigger vulnerabilities across a wide range of scanning tools.

Disclaimer:
⚠️ Warning: The files in this repository contain deliberate security vulnerabilities. These should be used only for educational purposes or within a controlled environment to test security tools. Do not deploy these files in any production environment or any system that can be accessed publicly.

Purpose
The main goal of this repository is to allow developers, security engineers, and researchers to:

Test security scanners for detecting various vulnerabilities.
Validate the effectiveness of tools like Semgrep, MobSF, SCA (Software Composition Analysis), and others.
Practice identifying vulnerabilities like SQL Injection, XSS, Insecure Deserialization, and more.
Vulnerability Types Covered
This repository includes vulnerable code in different languages and frameworks to trigger common security vulnerabilities:

Secrets Exposure

Files containing hardcoded secrets such as API keys.
Example: secret_test.py
PII Exposure

Files with Personally Identifiable Information (PII) like emails, phone numbers, and SSNs.
Example: pii_test.txt
SAST (SEMGREP)

Sample Python code vulnerable to injection attacks.
Example: semgrep_test.py
SAST (MOBSF)

Vulnerable Android code with insecure data storage practices.
Example: android_insecure_code.java
Software Composition Analysis (SCA)

Outdated dependencies in Python, Node.js, and Java projects.
Example: requirements.txt, package.json, pom.xml
Dockerfile Security

Dockerfile with insecure practices like using outdated base images and running as root.
Example: Dockerfile
Injection Vulnerabilities

SQL Injection: Vulnerable SQL queries with no parameterization.
Command Injection: Unvalidated input used in OS commands.
LDAP Injection: Unchecked user input in LDAP queries.
File Inclusion: Vulnerable file inclusion in PHP.
Examples: sql_injection_test.py, command_injection_test.py, ldap_injection_test.py, file_inclusion_test.php
Cross-Site Scripting (XSS)

Example HTML file vulnerable to reflected XSS.
Example: xss_test.html
Cross-Site Request Forgery (CSRF)

Example HTML form that could trigger a CSRF attack.
Example: csrf_test.html
Path Traversal

Python script vulnerable to path traversal.
Example: path_traversal_test.py
Open Redirect

Flask application vulnerable to open redirect attacks.
Example: open_redirect_test.py
Insecure Deserialization

Python code vulnerable to insecure deserialization via pickle.
Example: deserialization_test.py
Insecure Direct Object Reference (IDOR)

PHP example demonstrating an IDOR vulnerability.
Example: idor_test.php
XML External Entity (XXE)

Example XML file vulnerable to XXE attacks.
Example: xxe_test.xml, xxe_test_parser.py
Structure of the Repository
The repository is structured with simple file naming conventions. Each file is clearly labeled according to the type of vulnerability it contains. Here’s the breakdown:

graphql
Copy code
.
├── Dockerfile                   # Dockerfile with insecure configurations
├── README.md                    # This file
├── android_insecure_code.java    # Java code with insecure data storage
├── command_injection_test.py     # Command injection example
├── csrf_test.html                # CSRF vulnerability example
├── deserialization_test.py       # Insecure deserialization example
├── file_inclusion_test.php       # File inclusion vulnerability in PHP
├── idor_test.php                 # Insecure Direct Object Reference (IDOR) example
├── ldap_injection_test.py        # LDAP injection example
├── open_redirect_test.py         # Open redirect example in Flask
├── package.json                  # Node.js project with vulnerable dependencies
├── path_traversal_test.py        # Path traversal vulnerability
├── pii_test.txt                  # PII exposure example
├── pom.xml                       # Java project with vulnerable dependencies
├── requirements.txt              # Python project with vulnerable dependencies
├── secret_test.py                # Secret exposure example (hardcoded secrets)
├── semgrep_test.py               # Python code to trigger Semgrep findings
├── sql_injection_test.py         # SQL injection example
├── xss_test.html                 # Cross-site scripting example
├── xxe_test.xml                  # XML file with XXE vulnerability
└── xxe_test_parser.py            # Python XML parser vulnerable to XXE
How to Use

1. Copy Repo URL

2. Run Aquilax Scan 
Run your chosen security scanners (e.g., SAST tools, secret scanners, or dependency analyzers) on the repository to verify if they can detect the vulnerabilities.

https://app.aquilax.io

3. Check the Findings

Contributing
Contributions are welcome! If you have additional examples of vulnerabilities or improvements to existing ones, feel free to submit a pull request. Please make sure your code follows the format and standards used in this repository.

License
This repository is licensed under the MIT License. Feel free to use the files for testing, but do not deploy them in production environments.

Acknowledgments
This repository was inspired by common vulnerability patterns from the OWASP Top 10 and other security guidelines. It aims to help developers and security professionals in their pursuit of securing applications.

Let me know if you need any changes to this README or further customizations!