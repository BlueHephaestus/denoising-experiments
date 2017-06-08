# Description

This repository was originally made to help with [the LIRA Project](https://github.com/DarkElement75/lira), however it was made to be standalone as well, so that others might learn from it and overrall find it useful. It works on the problem of "de-noising", or removing random noise from an image. It can also be thought of as smoothing. The main two files are post_processing.py, which implements the actual algorithm, and lira_testing.py, which tests the algorithm on several predictions from the LIRA project.

*post_processing.py* is well-documented with how everything works, however at the core of it is an equation from [this article](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0051947), which they derive there. Unfortunately, as is often the case with research papers, it's not explained very well. I have my own notes on it, however they are handwritten and I haven't scribed them into a pdf yet. When I do, i'll put them here. However, until then, know that I derived the main formula for denoising from this paper, and credit goes to them for that. Hopefully for now their explanation will suffice, but contact me with any questions that you may have if needed.

*lira_testing.py* uses some predictions from the LIRA project to test the algorithm, provided in the predictions.h5 file, and generates the results found in our results/ directory and below. 

I've done my best to document both of these as best as I can, with the only exception being the rather important equation in post_processing.py, which will require a pdf to explain. That will be added to this repo, when I get to it, until then view the paper linked in resources below.

Good luck, have fun!

-Blake Edwards / Dark Element


# Results (Before -> After)

![Image 11](/results/11.jpg)
![Image 2](/results/2.jpg)
![Image 9](/results/9.jpg)
![Image 0](/results/0.jpg)

# Resources

[The main paper fundamentally behind this denoising algorithm](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0051947) - http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0051947

Sparse matrices and their compression algorithms - [My Notes](/notes/sparse%20matrices.pdf), [Scipy's documentation on sparse matrices](https://docs.scipy.org/doc/scipy/reference/sparse.html), and [Scipy's documentation on CSR Sparse matrices specifically](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix)

Adjacency matrices [Wikipedia](https://en.wikipedia.org/wiki/Adjacency_matrix)

Least Squares - [Wikipedia](https://en.wikipedia.org/wiki/Least_squares) and [Khan Academy](https://www.youtube.com/watch?v=MC7l96tW8V8)

