# Matplotlib Inline Back-end for IPython and Jupyter

## Installation:

With pip:

```bash
pip install matplotlib-inline
```

With conda:

```bash
conda install -c conda-forge matplotlib-inline
```

## Usage

In a Jupyter Notebook:

```python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp');
```
