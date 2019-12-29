from github import Github
import plotly.graph_objects as go

if __name__ == '__main__':
    user = input("Enter username: \n")
    password = input("Enter password: \n")
    g = Github(user,password)
    user = g.get_user()

    repositories = [repo.name for repo in g.get_user().get_repos()]
    print(repositories)
    repository_name = input("Enter repo name: \n")
    if repository_name not in repositories:
        print("Input repository doesn't exist")

    print("count of commits: ",g.get_user().get_repo(repository_name).get_commits().totalCount)
    commits = g.get_user().get_repo(repository_name).get_commits()
    files_in_commits = {commit.sha: [file.filename for file in commit.files] for commit in commits}
    commits_name = list(files_in_commits.keys())
    last = commits[0]
    commit_list = [file.filename for file in last.files]
    print("last change: ",commit_list)

    fig = go.Figure(data=[go.Table(
        header=dict(values=commits_name,
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[files_in_commits[name] for name in commits_name],  # 1nd column
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=10000, height=1000)
    fig.show()
