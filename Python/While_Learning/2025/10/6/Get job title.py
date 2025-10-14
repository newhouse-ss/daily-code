def get_job_title(company, employee_id):
    for department, employees in company.items():
        if employee_id in employees:
            print(f"Department: {department}")
            return employees[employee_id]
    return None
    

company = {
    "Tech":{
        'Shu':"ML",
        'Leon':'Backend',
        'K':'frontend'
    },
    "Marketing":{
        'su':'a',
        'tu':'p',
        'tt':"k"
    }
}
print(get_job_title(company, "Shu"))

print(company.items())