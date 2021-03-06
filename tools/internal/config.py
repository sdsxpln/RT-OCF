import os

# iotivity-rt
RT_OCF_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..'))
LINUX_BUILD_DIR = os.path.join(RT_OCF_ROOT, 'os', 'linux')

RT_OCF_FUNCTIONAL_TEST = os.path.join(RT_OCF_ROOT, 'test', 'functional')

LINUX_LINUX_TEST_DIR = os.path.join(LINUX_BUILD_DIR, 'test')
LINUX_LINUX_TEST_BIN_DIR = os.path.join(LINUX_LINUX_TEST_DIR, 'bin')

TIZEN_RT_BUILD_DIR = os.path.join(RT_OCF_ROOT, 'os', 'tizenrt')
RT_OCF_ROOT_TOOLS = os.path.join(RT_OCF_ROOT, 'tools')
RT_OCF_ROOT_TOOLS_INTERNAL = os.path.join(
    RT_OCF_ROOT_TOOLS, 'internal')
RT_OCF_HOOK_PATH = os.path.join(RT_OCF_ROOT_TOOLS, 'hooks')

# TizenRT
TIZEN_RT_ROOT = os.path.abspath(os.path.join(RT_OCF_ROOT, '..', '..'))
TIZEN_RT_OS_DIR = os.path.join(TIZEN_RT_ROOT, 'os')
TIZEN_RT_TOOLS_DIR = os.path.join(TIZEN_RT_OS_DIR, 'tools')

# Result file name for ci
CI_LINT_FILE_NAME = 'ci_lint.txt'


CI_LINUX_BUILD_FILE_NAME = 'ci_linux_build.txt'
CI_TIZENRT_BUILD_FILE_NAME = 'ci_tizenrt_build.txt'

CI_LINUX_TEST_FILE_NAME = 'ci_linux_test.txt'
CI_TIZENRT_TEST_FILE_NAME = 'ci_tizenrt_test.txt'

CI_LINUX_COVERAGE_FILE_NAME = 'ci_linux_coverage.txt'

CI_LINUX_LEAK_FILE_NAME = 'ci_linux_leak.txt'
CI_LINUX_PEAK_FILE_NAME = 'ci_linux_peak.txt'

# Common list

EXCLUDE_PATH_LIST = ['extlibs', 'tools', '/mocks']
