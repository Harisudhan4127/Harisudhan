name = input("Enter the Name : ")  # "John Doe"
designation = input("Enter the designation : ")  # "Software Engineer"
company = input("Enter the company or working place : ")  # "ABC Corp"
leave_dates = input("Enter the leave dates : ")  # "March 10 - March 15"
reason = input("Enter the reason : ")  # "personal matters"

def generate_leave_letter(name, designation, company, leave_dates, reason):
    letter = f"""
    From,
    {name},
    dept of AIML,
    {company},
    
    To,
    The Principal ,
    {company}
    
    Subject: Request for Leave 
    
    Dear {designation},
    
    I hope this letter finds you well. I am writing to formally request leave from {leave_dates} due to {reason}.
    
    I assure you that I will complete any pending work before my leave and make necessary arrangements for a smooth workflow in my absence.
    
    I kindly request you to grant my leave application. Your consideration will be greatly appreciated.
    
    Thank you.
    
    Sincerely,
    {name}
    """
    return letter


print(generate_leave_letter(name, designation, company, leave_dates, reason))
