
# Breadth First Traversal for a Graph

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Depth First Traversal for a Graph

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=' ')
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)        



# Count the number of nodes at given level in a tree using BFS

def count_nodes_at_level(graph, start, target_level):
    visited = set()
    queue = [(start, 0)]
    visited.add(start)
    count = 0
    
    while queue:
        node, level = queue.pop(0)
        
        if level == target_level:
            count += 1
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, level + 1))
                visited.add(neighbor)
    
    return count


# Count number of trees in a forest

def count_trees(graph):
    def dfs(node, visited):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    visited = set()
    tree_count = 0
    
    for node in graph:
        if node not in visited:
            dfs(node, visited)
            tree_count += 1
    
    return tree_count


# Detect Cycle in a Directed Graph

def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        if node in recursion_stack:
            return True

        if node in visited:
            return False
        
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        recursion_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    
    return False
