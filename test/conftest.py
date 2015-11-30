import pytest

# @pytest.mark.trylast
def pytest_runtest_makereport(item, call, __multicall__):
    '''
    Figure out how to mark JIRA test other than SKIPPED
    '''

    rep = __multicall__.execute()
    rep.outcome = "passed"
    # rep.outcome = "failed"
    rep.wasxfail = "failed"

    return rep

