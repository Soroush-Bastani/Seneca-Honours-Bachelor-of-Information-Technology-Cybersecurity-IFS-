````md
# Absolute and Relative Pathnames

## Objective

The objective of this lab is to introduce **absolute** and **relative** addressing.

---

## Notes

### Absolute Pathnames

- All absolute paths begin with `/`
- All absolute pathnames to a file (or directory) are **unique**
- Absolute pathnames can be used to specify a location **unambiguously** to any user

### Relative Pathnames

Relative pathnames are relative to the:

- **Present working directory** (`pwd`), also called the *current directory*
- **Home directory** (`~` denotes the home directory)

Special directory notations:

- Parent directory (relative to current directory): `..`
- Current (present) directory: `.` (one dot)

Additional notes:

- Relative pathnames begin with anything **other than `/`**
- Relative paths can often be **shorter** than absolute paths
- Relative-to-home pathnames begin with `~`
- Relative pathnames may differ between users because:
  - `~` points to a different home directory for each user
  - `.` and `..` depend on the current working directory (`pwd`)

---

## Examples

The `ls` command is used to list files and directories using different path types.

### Absolute Path Examples

```bash
ls /
ls /etc
ls /usr/bin
````

### Relative Path Examples

#### Relative to Present Directory

```bash
ls .
ls
```

#### Relative to Parent Directory

```bash
ls ..
```

#### Relative to Home of Logged-in User

```bash
ls ~
```

#### Relative to Another User’s Home Directory

```bash
ls ~mark.fernandes
```

---

## Tips and Advice

* You must know **what you are looking for** before you can effectively search for it.
* Experiment by exploring commands in the `/bin` directory.

  * Look up each command using Wikipedia or Google.
  * Some commands may seem obscure, but each exists for a purpose.
* Use `man` to get more information about a command:

  ```bash
  man ls
  ```
* Every file whose pathname begins with `/` is **unique**.

  * Two files with the same name cannot exist in the same directory.
* Each user’s home directory:

  * Is unique
  * Is located under `/home`
  * Has the same name as the login username
  * Is the default directory after login
* To interrupt a running command, press:

  ```
  CTRL + C
  ```

  This is the universal Linux/UNIX interrupt command.

---

## Practice Questions

### Directory Structure Creation

Using **only two commands**, create the following directory structure inside the `/tmp` directory of your Debian VM.

> Lines ending with `/` are directories; others are files.

```text
rough/
├── play/
│   ├── games/
│   │   └── tetris
│   │
│   └── movies/
│       └── matrix
└── work/
    ├── reports/
    │   └── project.txt
    │
    └── scripts/
        └── ops105.bash
```

---

### Assumptions

* Your present working directory (`pwd`) at the start of each question below is:

  ```text
  movies
  ```

---

### Copying Directories

Copy the `scripts` directory (and its contents) into the `games` directory.

After each copy operation, the resulting structure should include:

```text
games/scripts/ops105.bash
```

> You may delete the copied `scripts` directory in `games` after each attempt so the directory tree returns to its original state.

---

### Copy Using `cp` in Different Ways

Copy `scripts` into `games` using the following path methods:

1. Using **absolute paths**
2. Using **relative-to-home directory** (`~`)
3. Using **relative-to-username directory** (`~user`)
4. Using **parent directory** (`..`)
5. Using **current directory** (`.`)

---

### Analysis Questions

* Which of the paths above is the **shortest**?
* If instead of copying to `games`, you copied to your present working directory (`movies`):

  * How would that further shorten the relative path?
  * Did it actually shorten the path?

---

### Cleanup Task

* Delete the `scripts` sub-directory (and its contents) that you copied into `games` using an **absolute path**.

---

## OPS105 Home

* **Last Updated:** 2025-Sep-02 (Tue) 22:08

```
```
