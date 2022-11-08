# VBZ-H5Py-Plugin

This module provides a plugin to H5Py for the VBZ (de)compression library.

## VBZ Compression

VBZ compression is a compression algorithm developed by Oxford Nanopore to reduce
file size and improve read/write performance when handling raw data in POD5/Fast5 files.
Previously, the default compression was GZIP and comparing to GZIP we see a
compression improvement of >30% and a CPU performance improvement of >10X for
compression and >5X for decompression. Further details of the implementation and
benchmarks can be found here: [Nanoporetech/vbz_compression](https://github.com/nanoporetech/vbz_compression)

# Usage

Simply import the module to register the vbz plugin with `h5py`.

``` python
import vbz_h5py_plugin
```
