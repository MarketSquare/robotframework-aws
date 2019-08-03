Contributing

This project is at the beginning stages of development. We are looking for individuals who have or want to gain exposure to AWS boto3 api to create keywords for all services that have use cases for test automation.

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

Pull Request Process
Ensure any dependencies have been updated in the requirements file and explain reasoning behind the additional dependency.
Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent. 

You may merge the Pull Request in once you have the sign-off with a maintainer of the repository.

Testing your branch
We use Travis CI and Tox to automate unit tests when you push your changes. Every method that is written needs to be followed with a unit test, located in the tests directory. Every file represents a class and will begin with test_{name}.py After pushing your changes. Tox will run all unit tests and travis ci will show a pass/fail build.

Deploying to Pypi is automated on a successful merge.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

