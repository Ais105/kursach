from github import Github
import plotly.graph_objects as go

if __name__ == '__main__':
    user = input("Enter username: \n")
    password = input("Enter password: \n")
    g = Github(user,password)
    user = g.get_user()

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
