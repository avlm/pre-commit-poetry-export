# pre-commit-poetry-export
pre-commit hook to keep requirements.txt updated

### Why?
Your life is easier and the build is faster if you use requirements.txt file to install dependencies inside a docker image. But, it's not hard to forget to update the requirements file using poetry export and remember only when CI can't build the image.

### How it Works
In every commit this hook runs the following steps:
- If requirements.txt doesn't exist
    - It will be created and hook fails

- If requirements.txt exists
    - The hook will copy it's content to a file named old.requirements.txt
    - Then it will generate another requirements.txt using `poetry export` and compare the content of the two files
    - If they match you're good to go, if not the hook fails with 'requirements updated' message

If the hook has updated or created your requirements file, you can now `git add requirements.txt` and finish your commit.

Found any issues or want to suggest an improvement in the code?
Please contribute, open an issue /[here](https://github.com/avlm/pre-commit-poetry-export/issues/new)

Thanks! :)
