# Java Modules

This repository contains ( well, should  contain ) all of the leveled modules
for the league Java curriculum. These levels, in the `levels` directory, 
are pushed to the [League-Java](https://github.com/League-Java) repos with these scripts

## Development

The main development tasks are: 

* Updating the level repositories and the README files within
* Pushing modules to repos after updating them
* Rebuilding metadata for other programs.


First, install the lesson-builder program using `pipx`

```bash 
pipx install git+https://github.com/league-infrastructure/lesson-builder.git
```

TLDR, here is a complete creation, build and deployment of a level website: 

```bash 
jtl -v java web -l Level5
jtl -v  java build -l Level5
jtl -v  java deploy -l Level5
```

You can also commit and push all of the level websites at once:

* ``scripts/commit_all_levels.sh`` Commits the level websites
* ``scipts/update_all_levels.sh`` runs ``java web``, ``java build``, and ``java deploy`` on all level websites. 


### Update metadata

The metadata file ``meta.yaml`` is important for other tools, particularly the website builder, 
so it should be updated after making changes to modules. 

```bash
jtl java meta
```

The metadata collected is actually nearly alll of the text context of the
module so **you must run ``jtl java meta`` if you change any ``README.md`` 
files.** You can also use the `-m` option to `jtl java build`


### Editing Content

There are two levels of content you can edit: The level website content, and the content for a module. 

If you want to edit the content for a module, edit it in the module directory from the `level/` directory. For instance, here is the lesson for The Riddler in Level 0, Module 1: 

https://league-java.github.io/Level0/lessons/Module1/04_int/

The code and content for this lesson is in:

`levels/Level0/Module1/src/_04_int/_1_riddler`


You can edit ``README.md`` files in these directories to change website content, but then you must rebuild the metadata with either `jtl java meta` or  `jtl java build -m ... `


However, if you want to edit the Introduction for the Level, 

https://league-java.github.io/Level0/

Then you will edit files in the `_build/Levels/Level0/` directory. This
directory was cloned by `jtl web`, and if you change anything in it, you must
commit and push. 


### Pushing modules

You can edit both the code in a Level and the level's website from the level
directories in `levels/`. When you comit these changes, the will be committed
to this repository, but will not be made available to students. To push
modules to the repos where students will access them: 

```bash
jtl  java  push [-l <level> ] [-m <module>]
```

This will take the modules from the `levels` directory and copy them into  the level directories, which are

* https://github.com/League-Java/Level0.git
* https://github.com/League-Java/Level1.git
* https://github.com/League-Java/Level2.git
* https://github.com/League-Java/Level3.git
* https://github.com/League-Java/Level4.git
* https://github.com/League-Java/Level5.git


### Create or Clone a new Level Website

Each level has a level website:

* https://league-java.github.io/Level0/
* https://league-java.github.io/Level1/
* https://league-java.github.io/Level2/
* https://league-java.github.io/Level3/
* https://league-java.github.io/Level4/
* https://league-java.github.io/Level5/

These websites are built from the module's README files. For instance,  the
`jtl java build` will read the metadata generated from `jtl java meta`  and
combine it with the `README.md` files in `levels/Level0` to create lessons in
`lesson-builder` format in `_build/levels/Level0`. Later, `jtl java build`
will turn the lesson builder files into vuepress files, and `jtl java deploy`
will beuild those viewpress files into `_build/levels/Level0/docs`. From
there `jtl java deploy` will turn the vuepress files into HTML, which will be
pushed to the levels website repo. 


To get the local clone of a website repo, run:

```bash
jtl -v  java web -l <level1>
```

This command will create the website repo on github if it does not already exists, and
will clone or pull it if it does. The repo will be in ``_build/<level>``

Then, to update the website from the modules: 

```bash 
jtl  -v java build -m -l l<level>
```

To run the development server:

```bash
jtl java serve -l <level>
```


