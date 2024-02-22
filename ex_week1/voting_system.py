class voter():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    # one vote only

class vote():
    def __init__(self, id, candidate):
        self.id = id
        self.candidate = candidate

class candidate():
    def __init__(self, name, positions):
        self.name = name
        self.positions = [positions]

    def add_position(self,position):
        self.positions.append(position)
    # can have multiple positions

class VotingSystem:
    def __init__(self):
        self.voters = []
        self.candidates = []
        self.votes = []
            
    def add_voter(self, name, age, address):
        # extra :: encrypt the name and enter it to list if voters - to make sure no voter can submit twice 
        new_voter = voter(name, age, address)
        self.voters.append(new_voter)

    def add_candidate(self, name, position):
        new_candidate = candidate(name, position)
        self.candidates.append(new_candidate)

    def cast_vote(self, vote_id, candidate_name):
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                new_vote = vote(vote_id, candidate_name)
                self.votes.append(new_vote)
                return True
        return False

    def validate_voter(self):
        # make sure that voter did not vote previusly
        pass

    def results(self):
        # sum votes for each candidate
        res = {}
        for i in self.votes:
            print(i.candidate)
            if i.candidate in res.keys():
                res[i.candidate] += 1
            else:
                res[i.candidate] = 1
        return res
    
voting_system = VotingSystem()

# Add voters
voting_system.add_voter("A", 30, "123 Main St")
voting_system.add_voter("B", 25, "456 Elm St")
voting_system.add_voter("C", 70, "200 Main St")
voting_system.add_voter("D", 18, "34 Elm St")

# Add candidates
voting_system.add_candidate("Candidate A", "President")
voting_system.add_candidate("Candidate B", "Mayor")

# Cast votes
voting_system.cast_vote(1, "Candidate A")
voting_system.cast_vote(2, "Candidate B")
voting_system.cast_vote(3, "Candidate A")
voting_system.cast_vote(4, "Candidate B")

# Count votes
print(voting_system.results())