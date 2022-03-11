

def revert_issues_and_file(branch):
    issues = branch.issues
    files = []
    for issue in issues :
        components = issue.components
        