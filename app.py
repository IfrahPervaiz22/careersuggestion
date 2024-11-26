#for career suggestion
print("We are here to suggest you the best for your career.")
print("You have to give answer of few questions.")
while True:
    field=input("Enter your intermediate subject (pre):").lower()
    interest=input("Enter your area of interest:").lower()
    will= input("Are you willing to work in different locations? (yes/no): ").lower()
    salaryexp=input("What is your salary expectation (low, medium, high)? ").lower()
    suggestions = 0
    for i in range(1):  
        if field=="engineering" and interest=="software":
            if salaryexp=="high":
                print(f"Career suggestion {i+1}: Software Architect. High salary and great opportunities.")
            elif salaryexp=="medium":
                print(f"Career suggestion {i+1}: Software Developer. Good salary and room for growth.")
            else:
                print(f"Career suggestion {i+1}: Web Developer. A good start in the tech industry.")
            suggestions+=1
        elif field=="engineering" and interest=="civil":
            if salaryexp=="high":
                print(f"Career suggestion {i+1}: Civil Engineer for large infrastructure projects.")
            elif salaryexp=="medium":
                print(f"Career suggestion {i+1}: Structural Engineer in mid-sized firms.")
            else:
                print(f"Career suggestion {i+1}: Construction Manager. Starting with a practical role.")
            suggestions+=1
        elif field=="engineering" and interest=="machines":
            if salaryexp=="high" and will=="yes":
                print(f"Career suggestion {i + 1}: Mechanical Engineer (with high salary potential).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: Mechanical Engineer (good career prospects).")
            else:
                print(f"Career suggestion {i + 1}: Mechanical Technician (start with a solid role).")
            suggestions+=1
        elif field=="engineering" and interest == "electronic":
            if salaryexp=="high":
                print(f"Career suggestion {i + 1}: Electronics Engineer (work in high-tech companies).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: Electronics Engineer (great stability in industries).")
            else:
                print(f"Career suggestion {i + 1}: Electronics Technician (a good start in the field).")
            suggestions+=1
        elif field=="engineering" and interest == "aerospace":
            if salaryexp=="high" and will=="yes":
                print(f"Career suggestion {i + 1}: Aerospace Engineer (excellent pay and job satisfaction with opportunities to go abroad).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: Aerospace Engineer (great prospects).")
            else:
                print(f"Career suggestion {i + 1}: Aerospace Technician (good entry-level position).")
            suggestions+=1
        elif field=="medical" and interest=="neurologist":
            if salaryexp== "high":
                print(f"Career suggestion {i + 1}: Neurologist (excellent pay and growing demand).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: Neurologist (good long-term career).")
            else:
                print(f"Career suggestion {i + 1}: Neurology Assistant (entry level in the medical field).")
            suggestions+=1
        elif field=="medical" and interest=="dentist":
            if salaryexp=="high":
                print(f"Career suggestion {i + 1}: Dentist (high earning potential with specialization).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: General Dentist (good earning opportunities).")
            else:
                print(f"Career suggestion {i + 1}: Dental Assistant (good entry-level role).")
            suggestions+=1
        elif field=="medical" and interest=="dermatologist":
            if salaryexp=="high":
                print(f"Career suggestion {i + 1}: Dermatologist (excellent earning and job stability).")
            elif salaryexp=="medium":
                print(f"Career suggestion {i + 1}: Dermatology Specialist (good earning and growth).")
            else:
                print(f"Career suggestion {i + 1}: Dermatology Nurse (good entry-level option).")
            suggestions+=1
