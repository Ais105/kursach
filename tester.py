"""
    [X] repos
    [X] branches
    [ ] files for commits
    [X] tags
"""
from github import Github
import plotly.graph_objects as go
if __name__ == '__main__':
    # user = input("Enter username: \n")
    # password = input("Enter password: \n")
    g = Github(user,password)
    user = g.get_user()
    #
    repositories = [repo.name for repo in g.get_user().get_repos()]
    fig = go.Figure(data=[go.Table(
        header=dict(values=[user.login],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[repositories],  # 1nd column
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=500, height=10000)
    fig.show()
    #get all branches
    repository_name = input()
    print(g.get_user().get_repo(repository_name).get_commits().totalCount)
    print("Get all branches in repo %s:" % repository_name)
    if repository_name not in repositories:
        print("Input repository doesn't exist")
    branches = [branch.name for branch in g.get_user().get_repo(repository_name).get_branches()]
    fig = go.Figure(data=[go.Table(
        header=dict(values=[repository_name],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[branches],  # 1nd column
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=400, height=500)
    fig.show()
    tags = g.get_user().get_repo(repository_name).get_tags()
    tags_id_list = []
    for tag in tags:
        tags_id_list.append(tag.name)
    fig = go.Figure(data=[go.Table(
            header=dict(values=[repository_name],
                        line_color='white',
                        fill_color='rgb(206, 153, 255)',
                        align='center'),
            cells=dict(values=[tags_id_list],  # 1nd column
                       line_color='white',
                       fill_color='rgb(230, 204, 255)',
                       align='center'))
        ])
    fig.update_layout(width=500, height=130000)
    fig.show()
    # commits
    #branch_name = input()
    print("Get all commits in repository %s:" % repository_name)
    # if branch_name not in branches:
    #     print("Input branch doesn't exist")
    commits = g.get_user().get_repo(repository_name).get_commits()
    last = commits[0]
    commit_list = [last.files]
    # for comm in commits:
    #     commit_list.append(commits.commit.message)
    fig = go.Figure(data=[go.Table(
        header=dict(values=[repository_name],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[commit_list],  # 1nd column
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=400, height=10000)
    fig.show()
    # print("<--------------------------------------------------->")
    #список субмодулей
    #список файлов для коммита
    #количество багов для измененных файлов
