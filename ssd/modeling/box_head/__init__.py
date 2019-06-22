from ssd.modeling import registry
from .box_head import SSDBoxHead

__all__ = ['SSDBoxHead']


def build_box_head(cfg):
    # TODO: make it more general
    return registry.BOX_HEADS['SSDBoxHead'](cfg)
