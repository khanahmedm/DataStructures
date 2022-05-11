from py_wikiracer.internet import Internet
from typing import List
import copy
import sys
from heapq import heapify, heappush, heappop

internet = Internet()
html = internet.get_page("/wiki/Henry_Krumrey")
#print(html)

def get_links_in_page(html):
    list_href = []
    #with open('test2.html') as testfile:
    #for line in testfile:
    html = html.split()
    for line in html:
        #print(line)
        line = line.strip()
        if 'href' in line:
            start_pos_href = 0
            start_pos_href = line.find('href', start_pos_href)
            end_pos_href = line.find('>', start_pos_href)
            href_text = line[start_pos_href: end_pos_href]
            href_text = href_text.replace(' ','').replace('href=','').replace('"','')
            disallowed = Internet.DISALLOWED
            #print(disallowed)
            if href_text.startswith('/wiki/'):
                #print(href_text)
                if not any(char in href_text[6:] for char in disallowed):
                    #print(href_text)
                    #print(href_text[6:])
                    if href_text not in list_href:
                        list_href.append(href_text)

            start_pos_href = end_pos_href

    #print(list_href)
    #print(len(list_href))
    return list_href

def generate_graph(source, goal, alg_type):
    internet = Internet()
    graph = {}
    source_html = internet.get_page(source)
    graph[source] = get_links_in_page(source_html)
    goal_found = False
    if goal in graph[source]:
        return graph

    visited = []

    while 1:
        if goal_found:
            break

        #temp = graph.copy()
        temp = copy.deepcopy(graph)
        for vertex, edges in temp.items():
            if goal_found:
                break

            if vertex in visited:
                continue
            else:
                visited.append(vertex)
                print('visiting vertex:', vertex)

            if alg_type == 'bfs':

                for edge in edges:
                    print('visiting edge:', edge)
                    edge_html = internet.get_page(edge)
                    graph[edge] = get_links_in_page(edge_html)

                    if goal in graph[edge]:
                    #if edge == goal:
                        goal_found = True
                        break
            count = 0
            if alg_type == 'dfs':
                #while count < 10:
                while 1:
                    edge = edges.pop()
                    if edge in visited:
                        continue

                    print('visiting edge:', edge)
                    edge_html = internet.get_page(edge)
                    graph[edge] = get_links_in_page(edge_html)
                    #print('graph[edge]:', graph[edge])
                    visited.append(edge)
                    if goal in graph[edge]:
                        goal_found = True
                        #goal_html = internet.get_page(goal)
                        #graph[goal] = get_links_in_page(goal_html)
                        break
                    edges = graph[edge]
                    count += 1



    return graph

def bfs(source, goal):
    graph = generate_graph(source, goal, 'bfs')
    #print('graph:', graph)
    queue = []
    visited = []
    graph_keys = list(graph.keys())
    graph_keys.sort()
    #print('graph keys:', graph_keys)
    queue.append([source])
    while queue:
        path = queue.pop(0)
        #print('queue after pop:',queue)
        node = path[-1]

        print('path:',path)
        print('node:',node)
        if node == goal or goal in graph[node]:
            path.append(goal)
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

        if not node in visited:
            visited.append(node)

        #graph_keys.sort()
        visited.sort()

        if visited == graph_keys:
            if goal in graph[node]:
                path.append(goal)
                return path
            else:
                return None

def dfs(source, goal):
    graph = generate_graph(source, goal, 'dfs')
    #print('graph:', graph)
    graph_keys = list(graph.keys())
    #print('graph keys:', graph_keys)
    #print('graph:', graph)
    path = graph_keys.copy()
    path.append(goal)
    return path
    '''
    stack = [(source, [source])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        #print('path:', path)
        if vertex not in visited:
            if vertex == goal:
                if not vertex in path or vertex == source:
                    path.append(goal)
                return path
            visited.add(vertex)
            #print('visited:', visited)
            #print('graph[vertex]:', graph[vertex])
            if vertex in graph_keys:
                for neighbor in graph[vertex]:
                    stack.append((neighbor, path + [neighbor]))
    '''

def dijkstra(source, goal):
    path = [source]
    inf = sys.maxsize
    graph = {}
    node_data = {}
    node_data[source] = {'cost':0, 'pred':[]}
    visited = []
    temp = source
    internet = Internet()
    #html = internet.get_page(source)
    #links = get_links_in_page(html)
    costFn = lambda source, goal: len(goal)

    #for link in links:
    #    if source == link:
    #        graph[source][link] = 0
    #    else:
    #        graph[source][link] = costFn(source, link)

    while 1:
        if not temp in visited:
            visited.append(temp)
            min_heap = []
            html = internet.get_page(temp)
            links = get_links_in_page(html)
            graph[temp] = {}
            #node_data[temp] = {}
            for link in links:
                if temp == link:
                    graph[temp][link] = 0
                    #node_data[temp]['cost'] = 0
                else:
                    graph[temp][link] = costFn(source, link)
                    #node_data[link]['cost'] = costFn(source, link)
                    node_data[link] = {}
                    node_data[link] = {'cost':inf, 'pred':[]}


                print('graph[temp] details:', temp, link, 'cost:', graph[temp][link])
                #print('graph:', graph[temp])

            if goal in graph[temp]:
                print('goal found...')
                print(node_data[goal])
                node_data[goal]['pred'].append(goal)
                path.append(node_data[goal]['pred'])
                return path


            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    print('cost:', cost)
                    #node_data[j] = {}
                    #node_data[j] = {'cost':inf, 'pred':[]}
                    print('j:', j)
                    print("node_data[j]['cost']:", node_data[j]['cost'])
                    print("node_data[j]['pred']:", node_data[j]['pred'])
                    if cost < node_data[temp]['cost']:
                        node_data[j]['cost'] = cost
                        #node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                        node_data[temp]['pred'].append(temp)
                    print("node_data[j]['cost']:", node_data[j]['cost'])
                    print("node_data[j]['pred']:", node_data[j]['pred'])
                    heappush(min_heap, (node_data[j]['cost'],j))
        heapify(min_heap)
        temp = min_heap[0][1]

        if temp == goal:
            node_data[goal]['pred'].append(goal)
            break

    return node_data[goal]['pred']


#print(get_links_in_page(html))
#source='/wiki/Washington_University_in_St._Louis'
#goal='/wiki/Lenox,_Massachusetts'
#source='/wiki/ASDF'
#goal='/wiki/ASDF'
#source='/wiki/ASDF'
#goal='/wiki/FITS'
source="/wiki/Reese_Witherspoon"
goal="/wiki/Academy_Awards"
#source="/wiki/Calvin_Li"
#goal="/wiki/Wikipedia"
#source="/wiki/Calvin_Li"
#goal="/wiki/Quebecor"
#print(generate_graph(source, goal))
#print(bfs(source, goal))
#print(dfs(source, goal))
print(dijkstra(source, goal))
