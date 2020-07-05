def MinSwapsToSort(arr, n):
    arr_pos = [*enumerate(arr)] 
    arr_pos.sort(key = lambda x: x[1]) 
    vis = {k : False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if vis[i] or arr_pos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arr_pos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1)
    return ans

print(MinSwapsToSort([1, 5, 4, 3, 2], 5))