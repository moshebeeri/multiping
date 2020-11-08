# Multi Ping

## Branching strategy

This project uses the the standard git-flow branching strategy
in case you are not familure with you may like to review the [github git-flow guide](https://guides.github.com/introduction/flow/)
or just get the commands on the [git-flow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

### Howto git-flow
  
  this flow is for single developer per feature, please review and refine the process for squads and teams.

  git flow feature start my_awesome_feature
  develop the feature

  when you are done
  git flow feature finish my_awesome_feature
  git flow release start my_awesome_feature
  git flow release finish my_awesome_feature

  Create Pull request in github
  after reviewing the pull request it will be merged into main branch.

## TTD Framework

TDD is done by using the pytest framework utilizing, mock and patch
While mocking the architecture first it will automatically gain the interfaces of the different software modules.
All tasks should start with tests in branching and follow with the modules development.
