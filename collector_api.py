import gitlab
import os

# get access token and API URL from environment variables
access_token = os.environ['GITLAB_ACCESS_TOKEN']
api_url = os.environ['GITLAB_API_URL']
group_id = os.environ['GITLAB_GROUP_ID']



# create GitLab API client
gl = gitlab.Gitlab(api_url, private_token=access_token)

# group_id = 1217 #piistore group


group_a = gl.groups.get(group_id)

projects = group_a.projects.list()


for project in projects:
    print(project.id)

# # get project ID from project path
# project_path = 'dataoffice/piistore/piistore-infra' # replace with your project path
# project = gl.projects.get(project_path)
# project_id = project.id

# # get list of commits
# commits = project.commits.list(all=True)

# # print commit details
# for commit in commits:
#     print(commit.id, commit.title, commit.author_name, commit.created_at)
