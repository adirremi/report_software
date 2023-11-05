from equal_check import are_integers_equal
from views import get_guess_from_user


# Define the URL of your Flask application and the data to post



def last_compare_jobs(report1, report2):
    mistake_list = []
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2
    matched_jobs = []  # Track matched jobs from report1

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if 'total,' 'parts,' and 'zip code' are the same
            if (
                are_integers_equal(job1['total'], job2['total'])
                and are_integers_equal(job1['parts'], job2['parts'])
                and are_integers_equal(job1['zip code'], job2['zip code'])
                and not removed_from_report2  # Check if not already removed from report2
            ):
                # Collect elements to remove without modifying the list during iteration
                to_remove_report1.append(job1)
                to_remove_report2.append(job2)
                mistake_list.append([job1, "something is wrong with job address"])
                # Set the flag to True to avoid removing the same job from report2 again
                removed_from_report2 = True
                matched_jobs.append(job1)  # Mark job1 as matched

    # Remove elements from report1 and report2 after the loops
    for job1 in to_remove_report1:
        report1.remove(job1)
    for job2 in to_remove_report2:
        report2.remove(job2)

    return mistake_list, report1, report2#, print("last compare check is done")





def addandzip_compare_jobs(report1, report2):
    mistake_list = []
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2
    matched_jobs = []  # Track matched jobs from report1

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if 'address' and 'zip code' are the same
            if (
                job1['address'] == job2['address']
                and job1['zip code'] == job2['zip code']
                and not removed_from_report2  # Check if not already removed from report2
            ):
                # Collect elements to remove without modifying the list during iteration
                to_remove_report1.append(job1)
                to_remove_report2.append(job2)
                mistake_list.append([job1, "something is wrong in parts and total"])
                # Set the flag to True to avoid removing the same job from report2 again
                removed_from_report2 = True
                matched_jobs.append(job1)  # Mark job1 as matched

    # Remove elements from report1 and report2 after the loops
    for job1 in to_remove_report1:
        report1.remove(job1)
    for job2 in to_remove_report2:
        report2.remove(job2)

    return mistake_list, report1, report2#, print("2nd check is done")


def need_verify(report1, report2):
    mistake_list = []
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2
    matched_jobs = []  # Track matched jobs from report1

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if any of the specified conditions match
            if (
                (job1['address'] == job2['address'] and
                (str(job1['zip code'])[:2] == str(job2['zip code'])[:2] or
                are_integers_equal(job1['parts'], job2['parts']) or
                are_integers_equal(job1['total'], job2['total']))
             )):
                # Collect elements to remove without modifying the list during iteration
                to_remove_report1.append(job1)
                to_remove_report2.append(job2)
                # Set the flag to True to avoid removing the same job from report2 again
                removed_from_report2 = True
                matched_jobs.append(job1)  # Mark job1 as matched

        if removed_from_report2:
            break  # Exit the loop if job1 was removed from report2

    # Remove elements from report1 and report2 after the loops
    for job1 in to_remove_report1:
        report1.remove(job1)
    for job2 in to_remove_report2:
        report2.remove(job2)

    return mistake_list, report1, report2#, print("2nd check is done")

def double_check_interactive(report1, report2):
    matched_jobs = []  # Track matched jobs from report1
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if any of the specified conditions match
            if (
                (str(job1['zip code'])[:3] == str(job2['zip code'])[:3] and
                are_integers_equal(job1['parts'], job2['parts']) and
                are_integers_equal(job1['total'], job2['total'])
             )):
                matched_jobs.append(job1)  # Mark job1 as matched
                #print("Matched job from report1:")
                #print(job1)
                #print("Matched job from report2:")
                #print(job2)
                qus="Matched job from report1: \n" + str(job1) + "\nMatched job from report2: \n" + str(job2)
                decision=get_guess_from_user(qus)
                #decision = requests.post(url, data=data).text.lower()
                #decision = input("Enter 'r' to remove, 'k' to keep, or 's' to skip: ").lower()
                if decision == 'r':
                    to_remove_report1.append(job1)
                    to_remove_report2.append(job2)
                    removed_from_report2 = True
                elif decision == 'k':
                    break  # Keep this matched pair
            if removed_from_report2:
                break  # If removed from report2, move to the next job1

    # Remove collected elements from the reports after the loop
    for job1 in to_remove_report1:
        report1.remove(job1)
    for job2 in to_remove_report2:
        report2.remove(job2)

    return report1, report2#, print("Interactive check is done")





# Example usage:
def compare_reports(report1, report2):
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2
    matched_jobs = []  # Track matched jobs from report1

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if all specified conditions match
            if (
                job1['address'] == job2['address'] and
                are_integers_equal(job1['zip code'], job2['zip code']) and
                are_integers_equal(job1['total'], job2['total']) and
                are_integers_equal(job1['parts'], job2['parts'])
            ):
                # Collect elements to remove without modifying the list during iteration
                to_remove_report1.append(job1)
                to_remove_report2.append(job2)
                # Set the flag to True to avoid removing the same job from report2 again
                removed_from_report2 = True
                matched_jobs.append(job1)  # Mark job1 as matched

        if not removed_from_report2:
            for job2 in report2:
                # Check if all specified conditions match
                if (
                    job1['address'] == job2['address'] and
                    are_integers_equal(job1['zip code'], job2['zip code']) and
                    are_integers_equal(job1['total'], job2['total']) and
                    are_integers_equal(job1['parts'], job2['parts'])
                ):
                    # Collect elements to remove without modifying the list during iteration
                    to_remove_report1.append(job1)
                    to_remove_report2.append(job2)
                    matched_jobs.append(job1)  # Mark job1 as matched

    # Remove elements from report1 and report2 after the loops
    for job1 in to_remove_report1:
        if job1 in report1:
         report1.remove(job1)
    for job2 in to_remove_report2:
        report2.remove(job2)

    return report1, report2#, print("First check is done")




