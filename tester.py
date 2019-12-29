"""
    [X] repos
    [X] branches
    [X] files for commit
    [X] tags
    [X] submodules
    [ ] bags for changed files

"""
import shutil, git, os
from github import Github
import plotly.graph_objects as go

if __name__ == '__main__':
    user = input("Enter username: \n")
    password = input("Enter password: \n")
    g = Github(user,password)
    user = g.get_user()

    #get repos
    repositories = [repo.name for repo in g.get_user().get_repos()]
    fig = go.Figure(data=[go.Table(
        header=dict(values=[user.login],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[repositories],
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=500, height=10000)
    fig.show()


    #get all branches
    repository_name = input("Enter repo name: \n")
    print("Get all branches in repo %s:" % repository_name)
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
    
    tags = g.get_user().get_repo(repository_name).get_tags()
    tags_id_list = []
    for tag in tags:
        tags_id_list.append(tag.name)
    fig = go.Figure(data=[go.Table(
            header=dict(values=[repository_name],
                        line_color='white',
                        fill_color='rgb(206, 153, 255)',
                        align='center'),
            cells=dict(values=[tags_id_list],
                       line_color='white',
                       fill_color='rgb(230, 204, 255)',
                       align='center'))
        ])
    fig.update_layout(width=500, height=130000)
    fig.show()

    # commits_files
    print("Get all commits in repository %s:" % repository_name)
    rep_name = input("Get repo for commits: \n")
    print(g.get_user().get_repo(rep_name).get_commits().totalCount)
    commits = g.get_user().get_repo(rep_name).get_commits()
    files_in_commits = {commit.sha: [file.filename for file in commit.files] for commit in commits}
    commits_name = list(files_in_commits.keys())
    last = commits[0]
    commit_list = [file.filename for file in last.files]
    print(commit_list)

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
    fig.update_layout(width=10000, height=20000)
    fig.show()


    repo_name = input("Get repo for subs: \n")
    l = g.get_user().get_repo(repo_name).html_url
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
        header=dict(values=[repo_name],
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

    '''changedFiles = [item.a_path for item in repo.index.diff(None)]
    fig = go.Figure(data=[go.Table(
        header=dict(values=[repository_name],
                    line_color='white',
                    fill_color='rgb(206, 153, 255)',
                    align='center'),
        cells=dict(values=[changedFiles],
                   line_color='white',
                   fill_color='rgb(230, 204, 255)',
                   align='center'))
    ])
    fig.update_layout(width=500, height=130000)
    fig.show()'''

    # print("<--------------------------------------------------->")
    #количество багов для измененных файлов