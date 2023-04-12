import gitlab
import os

# get access token and API URL from environment variables
access_token = os.environ['GITLAB_ACCESS_TOKEN']
api_url = os.environ['GITLAB_API_URL']
group_id = os.environ['GITLAB_GROUP_ID']



# create GitLab API client
gl = gitlab.Gitlab(api_url, private_token=access_token)

### hardcoded path
project_id_a = 1944 #to delete, used just for debugging
project_a = gl.projects.get(project_id_a)


group_a = gl.groups.get(group_id)

projects = group_a.projects.list()
commits = project_a.commits.list(all=True)


# total_commits = 0
# for project in projects:


#     # get the commit count for the repository
#     commit_count = len(list(project.commits.list()))

#     # print the project ID and commit count
#     print(f"Project ID: {project.id}, Commit Count: {commit_count}")

#     # add the commit count to the total
#     total_commits += commit_count

# # print the total commit count for all projects
# print(f"Total Commits: {total_commits}")

# for project in projects:
#     print(project.id)

# for commit in commits:
#     print(commit.id)

total_commits = 0

commit_count = len(commits)

print(commit_count)
print(commits)

# # get project ID from project path
# project_path = 'dataoffice/piistore/piistore-infra' # replace with your project path
# project = gl.projects.get(project_path)
# project_id = project.id

# # get list of commits
# commits = project.commits.list(all=True)

# # print commit details
# for commit in commits:
#     print(commit.id, commit.title, commit.author_name, commit.created_at)
