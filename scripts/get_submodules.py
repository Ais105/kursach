import shutil, git, os
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

    l = g.get_user().get_repo(repository_name).html_url
    DIR_NAME = "your_clone_rep"
    REMOTE_URL = (l + ".git")

    if os.path.isdir(DIR_NAME):
        shutil.rmtree(DIR_NAME)
    os.mkdir(DIR_NAME)
    repo = git.Repo.init(DIR_NAME)
    origin = repo.create_remote('origin', REMOTE_URL)
    origin.fetch()
    origin.pull(origin.refs[0].remote_head)
    sm = repo.submodules
    arr = [submodule.name for submodule in sm]

    fig = go.Figure(data=[go.Table(
        header=dict(values=[repository_name],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[arr],
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=500, height=130000)
    fig.show()
