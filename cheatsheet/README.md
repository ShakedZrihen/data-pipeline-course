# cheatsheet

## Git

Clone repo

```bash
git clone https://github.com/ShakedZrihen/data-pipeline-course.git
```

Create new branch

```bash
git checkout -b <branch_name>
```

Commit to branch

``` bash
git add . 
git commit -m "<feat>|<fix>|<test> message"
git push
```

## Docker

Run container

```bash
docker run <container_name>
```

Build image from Dockerfile

```bash
docker build -t <name_for_image> .
```

Pull image from a repository (for example: from dockerhub)

```bash
docker pull <docker_image_tag>
```

List all running containers

```bash
docker ps
```
