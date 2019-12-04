from github import Github
import plotly.graph_objects as go
if __name__ == '__main__':
    user = input()
    password = input()
    g = Github(user,password)
    print("Get all repos:")
    user = g.get_user()
    repositories = [repo.name for repo in g.get_user().get_repos()]
    #get all repos
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
    fig.update_layout(width=400, height=10000)
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
    fig.update_layout(width=300, height=300)
    fig.show()
    # tags = [g.get_user().get_repo(repository_name).get_commit(sha="7d08aedbab9e735274e0426d96b2b67d83817781")]
    # fig = go.Figure(data=[go.Table(
    #         header=dict(values=[repository_name],
    #                     line_color='white',
    #                     fill_color='rgb(206, 153, 255)',
    #                     align='center'),
    #         cells=dict(values=[tags],  # 1nd column
    #                    line_color='white',
    #                    fill_color='rgb(230, 204, 255)',
    #                    align='center'))
    #     ])
    # fig.update_layout(width=300, height=300)
    # fig.show()
    #branch_name = input()
    # print("Get all commits in branch %s:" % branch_name)
    # if branch_name not in branches:
    #     print("Input branch doesn't exist")
    #branch = g.get_user().get_repo(repository_name).get_branch(branch_name)
    #comments = [commit.message for commit in branch.commit]
    # fig = go.Figure(data=[go.Table(
    #     header=dict(values=[branch_name],
    #                 line_color='white',
    #                 fill_color='rgb(206, 153, 255)',
    #                 align='center'),
    #     cells=dict(values=[comments],  # 1nd column
    #                line_color='white',
    #                fill_color='rgb(230, 204, 255)',
    #                align='center'))
    # ])
    # fig.update_layout(width=400, height=10000)
    # fig.show()
    # print("<--------------------------------------------------->")

    # print("Get last commit message in repo %s:" % repository_name)
    # branch = g.get_user().get_repo(repository_name).get_branch("master")
    # lastCommit = branch.commit.value.commit
    # print("\t%s" % lastCommit.message.value)

    print("<--------------------------------------------------->")
    #получить список всех тегов;