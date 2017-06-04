from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/etc/nginx",
        "/etc/nginx/snippets",
        "/etc/nginx/sites-enabled",
        "/etc/nginx/sites-available"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    def test_files(File):
    present = [
        "/etc/nginx/nginx.conf"
    ]
    absent = [
        "/etc/nginx/sites-enabled/default"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file
    if absent:
        for file in absent:
            d = File(file)
            assert not d.exists



def test_service(Service):
    present = [
        "nginx"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_running
            assert s.is_enabled


def test_packages(Package):
    present = [
        "nginx"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed
