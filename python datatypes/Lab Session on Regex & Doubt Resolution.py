'''Q5. Extract Valid Emails
Problem Description

You are given a list of email addresses, some of which are valid and some are invalid. Your task is to write a function validate_emails(emails) that takes a list of email addresses as input and returns a list containing only the valid email addresses.

A valid email address should adhere to the following rules:

It must contain exactly one "@" symbol.
It must contain at least one character before the "@" symbol.
It must contain at least one character after the "@" symbol.
It must end with a valid domain extension such as ".com", ".org", ".net", ".edu", or ".gov".
The local part (characters before the "@") can only contain alphanumeric characters, dots ".", underscores "_", or hyphens "-".
Characters after the "@", cannot contain any special character except dots ".", alphabets or numbers.
Your function should use regular expressions to validate each email address and return only the valid ones.

Input Format
Emails a list containing various emails

Output Format
A list of valid emails

Example Input
[ "john@example.com", "alice@company.org", "bob@email", "susan@123.com", "invalid.email", "no_domain@", "@missing_local", "invalid@@domain.com", "john.doe@my_example.com"]

Example Output
['john@example.com', 'alice@company.org', 'susan@123.com']'''

import re

def validate_emails(emails):
    """
    Given a list of email strings, return only those that match:
    - Exactly one '@'
    - Allowed characters in local part: A-Z, a-z, 0-9, dot, underscore, hyphen.
    - Domain part: alphanumeric and dots only.
    - Ends with .com, .org, .net, .edu, or .gov.
    """
    pattern = re.compile( r'^[A-Za-z0-9._-]+@[A-Za-z0-9.]+\.(?:com|org|net|edu|gov)$' )

    return [email for email in emails if pattern.match(email)]
