# chicken-disease

## Project Workflow:

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml (Only After all the pipeline steps are completed)

To Ignore artifacts file, add the {foler name}/* at the end of ".gitignore" file 

No pipeline required for "prepare Callbacks 03" 

ECR Repo URL:
905418405560.dkr.ecr.ap-southeast-2.amazonaws.com/chicken