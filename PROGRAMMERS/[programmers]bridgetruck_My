def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge=[0]*bridge_length
    current_weight = 0
    while truck_weights>0:
        if current_weight - truck_weights[0]<=weight:
            current_weight+=truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    return answer
