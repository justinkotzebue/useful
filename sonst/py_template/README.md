# cloud_masking

Getting the best of FMask, IdePix, and Sen2Cor.


## Installation

1. Download and install Miniconda.

2. sen2cor
   A) download the 'standalone' zip from http://step.esa.int/main/third-party-plugins-2/sen2cor/,
      extract and copy the folder e.g. to: `PATH_TO\AppData\Local\`
   B) Add `PATH_TO\AppData\Local\Sen2Cor-2.4.0-win64\Sen2Cor-2.4.0-win64` to PATH variable  
      and verify the 'standalone' installation with:
  ```
    L2A_Process --help
  ```

 3. SNAP (needed for IDEPIX)
    Download and install SNAP from http://step.esa.int/main/download/.

4. Then use the `environment.yml` file
   to install dependencies in `cm` environment and 'cloud_mask' like so
   ```
   conda env create -f environment.yaml
   activate cm
   python setup.py install
   ```
   And verify with `cloud_mask --help`



### Important note for Landsat IdePix

if not present, create a file `s3tbx.properties` in the folder `~/.snap/etc`
containing the line
```
s3tbx.landsat.readAs=reflectance
```

Or just copy the template `s3tbx.properties` included in the `assets` folder.

## Execution

When installed, this package provides the `cloud_mask` command line
interface. Type `cloud_mask --help` to see how to make it work.
