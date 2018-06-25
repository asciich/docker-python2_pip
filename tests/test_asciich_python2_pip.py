import pytest

@pytest.fixture(scope='module')
def container_image():
    return 'asciich/python2_pip'

class TestAsciichPython2Pip(object):

    def test_python2_installed(self, docker_container):
        version_cmd = 'python -c "import sys; print(\'{}.{}\'.format(sys.version_info.major, sys.version_info.minor))"'
        python_version_output = docker_container.check_output(version_cmd)
        assert b'2.7' in python_version_output

    def test_pip_installed(self, docker_container):
        assert b'pip 10.0' in docker_container.check_output('pip --version')