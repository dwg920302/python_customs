def solution(participant, completion):
    [participant.remove(i) for i in completion]
    return participant.pop()
