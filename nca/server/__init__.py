import sys
from oslo_config import cfg

from nca._i18n import _
from nca.common import config
from nca.common import profiler

def _init_configuration():
    config.init(sys.argv[1:])
    config.setup_logging()
    config.set_config_defaults()
    if not cfg.CONF.config_file:
        sys.exit(_("ERROR: Unable to find configuration file via the default"
                   " search paths (~/.nca/, ~/, /etc/nca/, /etc/) and"
                   " the '--config-file' option!"))

def boot_server(server_func):
    _init_configuration()
    try:
        server_func()
    except KeyboardInterrupt:
        pass
    except RuntimeError as e:
        sys.exit(_("ERROR: %s") % e)


def get_application():
    _init_configuration()
    profiler.setup('neutron-server', cfg.CONF.host)
    return config.load_paste_app('neutron')
