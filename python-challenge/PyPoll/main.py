import os
import csv
election_csv = os.path.join(r"C:\Users\vanes\python-challenge\PyPoll\Resources\election_data.csv")

total_votes = 0
candidates = {}
max_votes = 0
winner = ""

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    votes = list(csvreader)
    total_votes = len(votes) - 1

    print("Election results")
    print("--------------------------")

    print("Total votes: %d" % total_votes)
    print("--------------------------")

    candidates = {}
    for row in votes[1:]:
        if row[2] not in candidates:
            candidates[row[2]] = 1

        else:
            candidates[row[2]] += 1

    for candidates, vote_count in candidates.items():
        percentage = (vote_count / total_votes) * 100 
        print(f'{candidates}: {percentage: 3f}% ({vote_count})')

        if vote_count > max_votes:
            max_votes = vote_count
            winner = candidates


    print("--------------------------")

    print(f"Winner: {winner}")

    print("--------------------------")

    with open("output.txt", "w") as f:
        
        print("Election Results", file=f)
        print("----------------------", file=f)
        print("Total Votes: %d" % total_votes, file=f)
        print("----------------------", file=f)
        print(f'{candidates}: {percentage: .3f}% ({vote_count})', file=f)
        print("----------------------", file=f)
        print(f"Winner: {winner}", file=f)


        


