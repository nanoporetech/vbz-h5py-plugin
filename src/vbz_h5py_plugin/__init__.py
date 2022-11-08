""" vbz_hdf_plugin imported at module import-time"""

# pylint: disable=E1101,C0415

import sys


def get_vbz_resource_path() -> str:
    """Get the path to the vbz plugin (lib) resource"""

    vbz_package = "vbz_h5py_plugin"
    vbz_target = "lib"

    # importlib.resources superseeded pkg_resources from python3.9+
    if sys.version_info.major == 3 and sys.version_info.minor > 8:
        import importlib.resources

        vbz_lib = importlib.resources.files(vbz_package) / vbz_target
        with importlib.resources.as_file(vbz_lib) as path:
            return str(path.absolute())
    else:
        import pkg_resources

        return pkg_resources.resource_filename(vbz_package, vbz_target)


def register_plugin() -> str:
    """Register the vbz hdf plugins with h5py"""

    lib_path = get_vbz_resource_path()
    try:
        # Add the vbz library path to the h5 plugin search paths
        from h5py import h5pl

        h5pl.prepend(bytes(lib_path, "UTF-8"))
    except (ImportError, AttributeError):
        # We don't have the plugin library in h5py<2.10 so we fall
        # back on an environment variable
        import os

        os.environ["HDF5_PLUGIN_PATH"] = lib_path
    return lib_path


register_plugin()
