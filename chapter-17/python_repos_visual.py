"""Visual representation of TOP Python repos."""
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Create API call and save answer
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Save answer in variable
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]
my_layout = {
    'title': 'Most-Starred Python projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
