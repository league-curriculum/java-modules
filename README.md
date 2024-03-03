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

### Pushing modules

To push modules to the repos where students will acess them: 

```bash
jtl  java push --level_dir levels
```

You can also push only a subset of levels, 

```bash
jtl  java push --level_dir levels/Level0/Module0
```

### Update metadata

```bash
jtl java meta
```