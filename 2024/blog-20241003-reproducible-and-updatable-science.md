# Reproducible, Updatable, and Developable Science Software

Reproducible builds, reproducible environments, reproducible science: it's all the rage. There are plenty solutions to the reproducibility problem: pip freeze, conda export, docker.

However, we don't just want reproducible science. We also want to be able to update our software and dependencies because of new features, bug fixes, or reductions in complexity. Further, we want as similar environments as possible on different CPU architectures and operating systems.

The aforementioned solutions - pip freeze, conda export, and docker - fail at this, though they certainly can be (and are) a part of the solution.

What is needed is a machine-generated file that saves the exact versions of each and every dependency of a dependency. That is what will allow reproducible environments. In Julia these machine-generated files are called `Manifest.toml`, in Python a good option is `conda-lock.yml`.

In the case of `conda-lock`, architecture- and OS-dependent lists can be saved. In Julia that tends to be less of a problem, though maybe it will be with optional dependencies becoming an option. 

Then, to be updatable, one also needs a human-edited file that lists the required direct dependencies. Without this it becomes very hard to update as both direct and indirect dependencies can change. In Julia this is recorded in `Project.toml`, for Python there are several options - we use `environment.yaml`.

Finally, by "developable" I mean the following. We want to be able to easily change a package. In Julia this is achieved by calling `Pkg.develop(pkgname)`. In conda there used to be `conda develop`, but that is deprecated, probably because conda doesn't just do Python anymore, and "develop" would need something very different depending on the package. However, Python has editable install via pip, which is what we use. It's not as convenient to develop any given package, but probably fine for us.