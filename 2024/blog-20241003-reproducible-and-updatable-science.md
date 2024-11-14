# Reproducible, Updatable, Developable, and Independent Software Environments for Science

Reproducible builds, reproducible environments, reproducible science: it's all the rage. There are plenty solutions to the reproducibility problem: pip freeze, conda export, docker.

However, we don't just want reproducible science. We also want to be able to update our software and dependencies because of new features, bug fixes, or reductions in complexity. Further, we want as similar environments as possible on different CPU architectures and operating systems. Finally, we want different projects to have independent environments.

The aforementioned solutions - pip freeze, conda export, and docker - fail at this, though they certainly can be (and are) a part of the solution.

What is needed is a machine-generated file that saves the exact versions of each and every dependency of a dependency. That is what will allow reproducible environments. In Julia these machine-generated files are called `Manifest.toml`, in Python a good option is `conda-lock.yml`.

In the case of `conda-lock`, architecture- and OS-dependent lists can be saved. In Julia that tends to be less of a problem, though maybe it will be with optional dependencies becoming an option. 

Then, to be updatable, one also needs a human-edited file that lists the required direct dependencies. Without this it becomes very hard to update as both direct and indirect dependencies can change. In Julia this is recorded in `Project.toml`, for Python there are several options - we use `environment.yaml`.

Third, by "developable" I mean the following. We want to be able to easily change a package. In Julia this is achieved by calling `Pkg.develop(pkgname)`. In conda there used to be `conda develop`, but that is deprecated, probably because conda doesn't just do Python anymore, and "develop" would need something very different depending on the package. However, Python has editable install via pip, which is what we use. It's not as convenient to develop any given package, but probably fine for us.

Finally, if you have several projects, perhaps all using different versions of the same software packages, you want each project to have independent environments. One could even imagine nested environments, where each sub-environemnt could have a different version of the same package. However, unless you are making a Linux distribution, perhaps one by the name of Gitix, I fail to see the use case for such nested environments.

In conclusion, we don't just want reproducible environments, we also want to be able to update them, check out the git repo[^1] of any package and make changes, and we want to prevent different environments from stepping on each others' toes.


[^1]: Yes, I am hoping most packages have a git repo.
