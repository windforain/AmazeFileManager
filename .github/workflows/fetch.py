import requests
import json

try:

      actions_params = {
      'per_page': '1',
      'event': 'issue_comment',
      'status': 'success',
      }
      
      actions_response = requests.get(
        'https://api.github.com/repos/VishnuSanal/AmazeFileManager/actions/workflows/android-debug-artifact-ondemand.yml/runs',
        params=actions_params,
      )
      
      actions = json.loads(actions_response.content)
      
      # with open('actions.json', 'r') as f:
      #   actions = json.load(f) # debug
      
      check_suite_id = actions["workflow_runs"][0]["check_suite_id"]

      print("debug: check_suite_id:", check_suite_id, sep=' ', end='\n\n')

      artifacts_url = actions["workflow_runs"][0]["artifacts_url"]

      artifacts_response = requests.get(
         artifacts_url
      )

      artifacts = json.loads(artifacts_response.content)

      # with open('artifacts.json', 'r') as f:
      #   artifacts = json.load(f) # debug

      # hack - since we have only two artifacts for now
      id_one = artifacts["artifacts"][0]["id"]
      id_two = artifacts["artifacts"][1]["id"]

      print("debug: id_one:", id_one, sep=' ', end='\n\n')
      print("debug: id_two:", id_two, sep=' ', end='\n\n')

      artifact_one = "https://github.com/VishnuSanal/AmazeFileManager/suites/" + str(check_suite_id) + "/artifacts/" + str(id_one)
      artifact_two = "https://github.com/VishnuSanal/AmazeFileManager/suites/" + str(check_suite_id) + "/artifacts/" + str(id_two)

      print("debug: artifact_one:", artifact_one, sep=' ', end='\n\n')
      print("debug: artifact_two:", artifact_two, sep=' ', end='\n\n')

      comment = "The requested APKs has been built. Please get them from these links:\n" + artifact_one + "\n" + artifact_two

except:
      comment = "The requested APKs has been built. Please find them from the artifacts section of this PR."

with open('comment.md', 'w') as the_file:
    the_file.write(comment)