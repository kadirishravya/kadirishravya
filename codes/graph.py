graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
# stack=[]
# for i in graph:
#     stack.append(graph[i])
vistied=set()
def dfs(visited,node,graph):
if node is None:

for i in