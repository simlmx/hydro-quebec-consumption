Prerequisites
============

- python 3.6 or more recent


Installation
============

    python3 -m venv ve
    source ve/bin/activate
    pip install -r requirements
    jupyter nbextension install --sys-prefix --py vega
    jupyter nbextension enable --sys-prefix --py vega


Running
=========

1. Put your daily consumption `.csv` files from hydro-quebec in the `data` folder.
2. Start jupyter with `jupyter notebook`
3. Open the `hydro-analysis.ipynb` file and run it.


Testing
=========

    pytest .
