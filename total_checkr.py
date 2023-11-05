from equal_check import are_integers_equal
def total_rate_mistake(report1, report2):
    mistake_list = []
    to_remove_report1 = []  # Collect elements to remove from report1
    to_remove_report2 = []  # Collect elements to remove from report2
    matched_jobs = []  # Track matched jobs from report1

    for job1 in report1:
        if job1 in matched_jobs:
            continue  # Skip already matched job
        removed_from_report2 = False  # Flag to track if a job has been removed from report2
        for job2 in report2:
            # Check if the 'address,' 'parts,' and 'zip code' are the same
            if (
                job1['address'] == job2['address']
                and are_integers_equal(job1['parts'], job2['parts'])
                and are_integers_equal(job1['zip code'], job2['zip code'])
                and not removed_from_report2  # Check if not already removed from report2
            ):
                # Collect elements to remove without modifying the list during iteration
                to_remove_report1.append(job1)
                to_remove_report2.append(job2)
                mistake_list.append([job1, "total rate is not the same"])
                # Set the flag to True to avoid removing the same job from report2 again
                removed_from_report2 = True
                matched_jobs.append(job1)  # Mark job1 as matched

    # Remove elements from report1 and report2 after the loops
    for job1 in to_remove_report1:
        report1.remove(job1)
    for job2 in to_remove_report2:
        if job2 in report2:
         report2.remove(job2)

    return mistake_list
