import pytest
from py._code.code import ReprEntryNative 


FAKE_CACHE = {
    'ISSUE-1': {
        'components' : [],
        'versions': [],
        'fixVersions': [],
        'status': 'open',
    },
    'ISSUE-2': {
        'components' : [],
        'versions': [],
        'fixVersions': [],
        'status': 'closed',
    },
    'ISSUE-3': {
        'components' : ['com1', 'com2'],
        'versions': [],
        'fixVersions': [],
        'status': 'open',
    },
    'ISSUE-3F': {
        'components' : ['com3', 'com4'],
        'versions': [],
        'fixVersions': [],
        'status': 'open',
    },
    'ISSUE-4': {
        'components' : ['com1', 'com2'],
        'versions': [],
        'fixVersions': [],
        'status': 'closed',
    },
    'ISSUE-5': {
        'components' : [],
        'versions': ['1.0.0', '1.0.1'],
        'fixVersions': [],
        'status': 'open',
    },
    'ISSUE-6': {
        'components' : [],
        'versions': ['1.0.0', '1.0.1'],
        'fixVersions': ['1.0.1'],
        'status': 'closed',
    },
    'ISSUE-6F': {
        'components' : [],
        'versions': ['1.0.0', '1.0.1'],
        'fixVersions': ['1.0.0'],
        'status': 'closed',
    },
    'ISSUE-7': {
        'components' : ['com1', 'com2'],
        'versions': ['1.0.0', '1.0.1'],
        'fixVersions': [],
        'status': 'open',
    },
    'ISSUE-7F': {
        'components' : ['com1', 'com2'],
        'versions': ['1.0.0'],
        'fixVersions': [],
        'status': 'open',
    },

}


TEST_INFO = {}


def pytest_runtest_makereport(item, call):
    if call.when is 'teardown':
        global TEST_INFO
        test = TEST_INFO.setdefault(item.name, {})
        if not test:
            marker = item.get_marker('jira')
            if marker:
                test['jira_marker'] = marker.args
            else:
                test['jira_marker'] = ()
            try:
                components = item.config.getini('jira_components')
                test['components'] = components
            except Exception:
                pass
            try:
                version = item.config.getini('jira_version')
                test['version'] = components
            except Exception:
                pass


def pytest_report_teststatus(report):
    if report.when == 'call':
        if hasattr(report, "wasxfail"):
            if 'expect_xfail' in report.keywords:
                if report.outcome is 'skipped':
                    del report.wasxfail
                    report.outcome = 'passed'
            elif 'expect_xpass' in report.keywords:
                if report.outcome is 'failed':
                    del report.wasxfail
                    report.outcome = 'passed'
            else:
                make_traceback(report)
                del report.wasxfail
                report.outcome = 'failed'
        else:
            if 'expect_fail' in report.keywords:
                if report.outcome is 'failed':
                    report.outcome = 'passed'
            elif 'expect_pass' in report.keywords:
                if report.outcome is 'passed':
                    report.outcome = 'passed'
            elif 'expect_skip' not in report.keywords:
                make_traceback(report)
                report.outcome = 'failed'
    if 'expect_skip' in report.keywords:
        report.outcome = 'passed'


def make_traceback(report):
    test_name = report.nodeid.split('::')[-1]
    # report.longrepr.reprtraceback = [test_name, '\n']
    import ipdb; ipdb.set_trace()


def pytest_collection_modifyitems(session, config, items):
    plug = config.pluginmanager.getplugin('jira_plugin')
    plug.issue_cache = FAKE_CACHE