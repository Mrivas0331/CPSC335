function connections(n, m):
    edge_list = []
    
    for i in (1, m + 1):
        edge_list + (u, v, cost)
    sort edge_list

    int answer

    connect(x):
        If p[x] not equal x: //recursion to not create cycle
            p[x] = connect(p[x])
        return p[x]
    
    for connection e in edge_list:
        x = e[0] - 1
        y = e[1] - 1
        cost = e[2]
        if connect(x) equals connect(y):
            continue to next
        p[connect(x)] = connect(y)
        answer += cost

        if (all nodes connected):
            return answer
    
    return -1