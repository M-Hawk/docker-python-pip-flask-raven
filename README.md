# Docker Env for Python Terminal Game

# Running Game

This command builds a docker image with the code of this repository and runs the repository's terminal game

```sh
./build_docker.sh battle-robots
docker run --rm -it battle-robots
```

# Running Tests

This command builds a docker image with the code of this repository and runs the repository's tests

```sh
./build_docker.sh battle-robots
docker run --rm battle-robots ./run_tests.sh -v
```

```
[+] Building 45.6s (11/11) FINISHED                                                      docker:desktop-linux 
 => [internal] load build definition from Dockerfile                                                     0.0s 
 => => transferring dockerfile: 317B                                                                     0.0s 
 => [internal] load metadata for docker.io/library/python:3.13.2-alpine3.21@sha256:323a717dc4a010fee21e  1.8s 
 => [internal] load .dockerignore                                                                        0.0s 
 => => transferring context: 85B                                                                         0.0s 
 => [1/6] FROM docker.io/library/python:3.13.2-alpine3.21@sha256:323a717dc4a010fee21e3f1aac738ee10bb485  5.0s 
 => => resolve docker.io/library/python:3.13.2-alpine3.21@sha256:323a717dc4a010fee21e3f1aac738ee10bb485  0.0s 
 => => sha256:b0d8a12effa95e69eeae00f331cd5c50b0d9c8ed631b6e681fbe08a5902971ff 249B / 249B               0.3s 
 => => sha256:85be7329d6c2da132d82c42a32407595e174c5d8452d99a78201e96a553f1ed0 12.53MB / 12.53MB         4.4s 
 => => sha256:a507b793f9af8c58adcae308a17d0d4c2e8074a530b01b6abec958e9b7476cbb 458.61kB / 458.61kB       1.4s 
 => => sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870 3.64MB / 3.64MB           3.3s 
 => => extracting sha256:f18232174bc91741fdf3da96d85011092101a032a93a388b79e99e69c2d5c870                0.1s 
 => => extracting sha256:a507b793f9af8c58adcae308a17d0d4c2e8074a530b01b6abec958e9b7476cbb                0.2s 
 => => extracting sha256:85be7329d6c2da132d82c42a32407595e174c5d8452d99a78201e96a553f1ed0                0.4s 
 => => extracting sha256:b0d8a12effa95e69eeae00f331cd5c50b0d9c8ed631b6e681fbe08a5902971ff                0.0s 
 => [internal] load build context                                                                        0.0s 
 => => transferring context: 26.98kB                                                                     0.0s 
 => [2/6] WORKDIR /app                                                                                   0.4s 
 => [3/6] COPY requirements.txt .                                                                        0.1s 
 => [4/6] RUN apk add --no-cache build-base bash ncurses                                                23.0s 
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                             4.0s 
 => [6/6] COPY . .                                                                                       0.1s
 => exporting to image                                                                                  10.6s
 => => exporting layers                                                                                  8.8s
 => => exporting manifest sha256:c18d33307faf0bd9c348c1e366b33a962d91619ccc326030b2ead5d3b9ccae18        0.0s
 => => exporting config sha256:fa602762de441802c4386b37859d9d20543f3b041a1caa6c4bd5ff56c7d3c9c8          0.0s
 => => exporting attestation manifest sha256:cc3e48d55b52510db0393b7750ee714bd006b8eba3b6b9d0b47d164028  0.0s
 => => exporting manifest list sha256:440a9a034ab6e67db37446cdb2771458552ee90cb49e236d3c85553c316fa5fb   0.1s
 => => naming to docker.io/library/battle-robots:latest                                                  0.0s
 => => unpacking to docker.io/library/battle-robots:latest
....
----------------------------------------------------------------------
test_computer_player_initialization (__main__.TestComputerPlayer.test_computer_player_initialization) ... ok
test_weap_body_dmg (__main__.TestGame.test_weap_body_dmg) ... ok
test_weap_weap_dmg (__main__.TestGame.test_weap_weap_dmg) ... ok
test_damage (__main__.TestPlayer.test_damage) ... ok
test_getters (__main__.TestPlayer.test_getters) ... ok
test_setters (__main__.TestPlayer.test_setters) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.039s

OK
```
# Running a specific test

This example runs a single test in the class TestGame, with the name "test_weap_body_dmg"

```sh
./build_docker.sh battle-robots
docker run --rm battle-robots ./run_tests.sh -v TestGame.test_weap_body_dmg
```
