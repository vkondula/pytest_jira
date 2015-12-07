import pytest
import os
import xmlrpclib

failed = pytest.mark.expect_fail
passed = pytest.mark.expect_pass
xfailed = pytest.mark.expect_xfail
xpassed = pytest.mark.expect_xpass
skiped = pytest.mark.expect_skip

@pytest.mark.skip_selenium
@pytest.mark.nondestructive
class Test_Pytest_JIRA(object):

    @passed
    def test_no_jira_marker_passed(self):
        assert True

    @failed
    def test_no_jira_marker_failed(self):
        assert False

    @pytest.mark.jira
    @passed
    def test_jira_marker_no_args_passed(self):
        assert True

    @pytest.mark.jira
    @failed
    def test_jira_marker_no_args_failed(self):
        assert False

    @pytest.mark.jira('there is no issue here')
    @passed
    def test_jira_marker_bad_args_passed(self):
        assert True

    @pytest.mark.jira('there is no issue here')
    @failed
    def test_jira_marker_bad_args_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-2')
    @passed
    def test_closed_no_comp_no_version_passed(self):
        assert True

    @pytest.mark.jira('ISSUE-2')
    @failed
    def test_closed_no_comp_no_version_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-1')
    @xpassed
    def test_open_no_comp_no_version_xpassed(self):
        assert True

    @pytest.mark.jira('ISSUE-1')
    @xfailed
    def test_open_no_comp_no_version_xfailed(self):
        assert False

    @pytest.mark.jira('ISSUE-3')
    @xpassed # xpassed
    def test_open_match_comp_no_version_xpassed(self):
        assert True

    @pytest.mark.jira('ISSUE-3')
    @xfailed
    def test_open_match_comp_no_version_xfailed(self):
        assert False

    @pytest.mark.jira('ISSUE-3F')
    @passed
    def test_open_no_match_comp_no_version_passed(self):
        assert True

    @pytest.mark.jira('ISSUE-3F')
    @failed
    def test_open_no_match_comp_no_version_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-4')
    @passed
    def test_closed_match_comp_no_version_passed(self):
        assert True

    @pytest.mark.jira('ISSUE-4')
    @failed
    def test_closed_match_comp_no_version_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-5')
    @xpassed
    def test_open_no_comp_match_version_xpassed(self):
        assert True

    @pytest.mark.jira('ISSUE-5')
    @xfailed
    def test_open_no_comp_match_version_xfailed(self):
        assert False

    @pytest.mark.jira('ISSUE-6')
    @passed
    def test_closed_no_comp_match_version_passed(self):
        assert True

    @pytest.mark.jira('ISSUE-6')
    @xfailed #failed
    def test_closed_no_comp_match_version_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-6F')
    @xpassed 
    def test_closed_for_diff_version_xpassed(self):
        assert True

    @pytest.mark.jira('ISSUE-6F')
    @xfailed
    def test_closed_for_diff_version_xfailed(self):
        assert False

    @pytest.mark.jira('ISSUE-7')
    @xpassed
    def test_open_match_comp_match_version_xpassed(self):
        assert True

    @pytest.mark.jira('ISSUE-7')
    @xfailed
    def test_open_match_comp_match_version_xfailed(self):
        assert False

    @pytest.mark.jira('ISSUE-7F')
    @passed
    def test_open_for_diff_version_passed(self):
        assert True

    @pytest.mark.jira('ISSUE-7F')
    @failed
    def test_open_for_diff_version_failed(self):
        assert False

    @pytest.mark.jira('ISSUE-7F', run=False)
    @skiped
    def test_run_false_skipped(self):
        assert False
