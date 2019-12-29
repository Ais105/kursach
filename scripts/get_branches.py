from github import Github
import plotly.graph_objects as go

if __name__ == '__main__':
    user = input("Enter username: \n")
    password = input("Enter password: \n")
    g = Github(user,password)
    user = g.get_user()
    repositories = [repo.name for repo in g.get_user().get_repos()]
    print(repositories)
#get all branches
    repository_name = input("Enter repo name: \n")
    if repository_name not in repositories:
        print("Input repository doesn't exist")
    branches = [branch.name for branch in g.get_user().get_repo(repository_name).get_branches()]
    fig = go.Figure(data=[go.Table(
        header=dict(values=[repository_name],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[branches],
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=400, height=500)
    fig.show()