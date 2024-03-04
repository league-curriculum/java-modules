# Java Modules

This repository contains ( well, should  contain ) all of the leveled modules
for the league Java curriculum. These levels, in the `levels` directory, 
are pushed to the [League-Java](https://github.com/League-Java) repos with 

## Development

The main development tasks are: 

* Pushing modules to repos after updating them
* Rebuilding metadata for other programs.


First, install the lesson-builder program using `pipx`

```bash 
pipx install git+https://github.com/league-infrastructure/lesson-builder.git
```

TLDR, here is a complete creation, build and deployment of a level website: 

```bash 
jtl -v java web -l Level0
jtl -v  java build -l Level0
jtl -v  java deploy -l Level0
```


### Update metadata

The metadata file ``meta.yaml`` is important for other tools, particularly the website builder, 
so it should be updated after making changes to modules. 

```bash
jtl java meta
```


### Pushing modules

To push modules to the repos where students will acess them: 

```bash
jtl  java push --level_dir levels
```

You can also push only a subset of levels, 

```bash
jtl  java push --level_dir levels/Level0/Module0
```

### Create or Clone a new Level Website

To get the local clone of a website repo, run:

```bash
jtl -v  java web -l <level1>
```

This command will create the website repo on github if it does not already exists, and
will clone or pull it if it does. The repo will be in ``_build/<level>``

Then, to update the website from the modules: 

```bash 
jtl  -v java build -l l<level>
```

To run the development server:

```bash
jtl java serve -l <level>
```


