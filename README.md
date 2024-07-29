# mov

### install
```bash
# main
$ pip install git+https://github.com/Nicou11/movie.git

# branch
$ $ pip install git+https://github.com/Nicou11/movie.git@<BRANCH_NAME>
```
### start dev
```
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pytest

# option
$ pdm venv create
```

### setting env
```bash
cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"
```
