import csv

def save_to_file(file_name, jobs_db):
    file = open(f"{file_name}jobs.csv", "w") 
    writer = csv.writer(file) 
    writer.writerow(["Title", "Company", "Link"])
    for job in jobs_db:
        writer.writerow(job.values())
    file.close()