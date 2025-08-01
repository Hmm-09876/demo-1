import os
import yaml

# Thư mục workflow
workflow_dir = ".github/workflows"
os.makedirs(workflow_dir, exist_ok=True)
ci = {
    "name": "CI",
    "on": ["push", "pull_request"],
    "jobs": {
        "build_and_test": {
            "runs-on": "ubuntu-latest",
            # "services": {
            #     "localstack": {
            #         "image": "localstack/localstack",
            #         "ports": ["4566:4566"],
            #         "options": (
            #             #"--health-cmd 'curl -s http://localhost:4566/health | grep 'UP' ' 
            #             "--health-cmd \"curl -s http://localhost:4566/health | grep 'UP'\" " 
            #             "--health-interval=5s --health-timeout=2s --health-retries=5"
            #         ),
            #         "env": {
            #             "SERVICES": "s3,lambda",
            #             "DEBUG": "1"
            #         }
            #     }
            # },
            "steps": [
                {"uses": "actions/checkout@v3"},
                {
                    "name": "Set up Python",
                    "uses": "actions/setup-python@v4",
                    "with": {"python-version": "3.x"}
                },
                {"name": "Install dependencies", "run": "pip install pytest boto3 localstack-client"},
                {"name": "Set up LocalStack", "uses": "localstack/localstack@v3",
                 "with": {"localstack-version": "latest", "services": "s3,lambda"}},

                # {
                #     "name": "Start LocalStack",
                #     "run": (
                #         #"docker compose -f localstack/docker-compose.yml up -d && "
                #         "docker compose -f localstack/docker-compose.yml up -d localstack && "
                #         #"until curl -s http://localhost:4566/health | grep 'running'; do sleep 2; done"
                #         "until [ \"$(docker inspect --format='{{.State.Health.Status}}' localstack-main)\" = \"healthy\" ]; do sleep 1; done"

                #     )
                # },
                {"name": "Deploy LocalStack resources", "run": "python localstack/localstack.py"},
                {"name": "Run tests", "run": "PYTHONPATH=. pytest test/"},
                {"name": "Tear down LocalStack", 
                 "if": "always()",
                 "run": "docker compose -f localstack/docker-compose.yml down"}
            ]
        }
    }
}

with open(os.path.join(workflow_dir, "ci.yml"), "w") as f:
    yaml.dump(ci, f, sort_keys=False)

print("Generated CI workflow")
