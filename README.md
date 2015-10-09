# Intro
A [pytest][pytest] plugin for JIRA integration.

This plugin links tests with JIRA tickets. The plugin behaves similar to the [pytest-bugzilla](https://pypi.python.org/pypi/pytest-bugzilla) plugin.

| variable | description |
|----:|:----|
|v|used version|
|Va|affected versions|
|Vf|fixed in versions|
|C|used components|
|Ca|affected components|


| CONDITION | Test Passed | Test Failed |
|---------|:---------:|:---------:|
| | **Basic** | |
| Run = False | skipped | skipped
| Unresolved | xpassed | xfailed |
| Resolved | passed | failed |
| Not found  | passed | failed |
| Not specified | passed | failed |
| | **Advanced** | |
| *Resolved:* | 
| v ∉ Va | passed | failed |
| v ∈ Va ∧ v ∈ Vf | passed | failed |
| v ∈ Va ∧ v ∉ Vf | xpassed | xfailed |
| *Unresolved:*| 
| C ∩ Ca ∧ v = not specified | xpassed | xfailed |
| C ∩ Ca ∧ Va = not specified | xpassed | xfailed |
| C ∩ Ca ∧ v ∈ Va | xpassed | xfailed |
| C ∩ Ca ∧ v ∉ Va | passed | failed |
| ¬(C ∩ Ca) | passed | failed |



The plugin does not close JIRA tickets, or create them. It just allows you to link tests to existing tickets.

This plugin currently assumes the following workflow:

A JIRA issue with status in ['Closed', 'Resolved'] is assumed to be resolved.
All other issues are considered unresolved.

Please feel free to contribute by forking and submitting pull requests or by
submitting feature requests or issues to [issues][githubissues].

## Requires
* pytest >= 2.2.3
* jira-python >= 0.13

## Installation
``pip install pytest_jira``

## Usage
1. Create a `jira.cfg` in the root of your tests

    ```ini
    [DEFAULT]
    url = https://jira.atlassian.com
    username = USERNAME (or blank for no authentication)
    password = PASSWORD (or blank for no authentication)
    ```

Options can be overridden with command line options.

 ``py.test --help``

2. Mark your tests with jira marker and issue id.
 ``@pytest.mark.jira('issue_id')``

3. Run py.test with jira option to enable the plugin.
 ``py.test --jira``

[pytest]: http://pytest.org/latest/
[githubissues]: https://github.com/jlaska/pytest_jira/issues
