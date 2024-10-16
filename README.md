# Blogging Platform API

Blogging Platform API's A personal blogging platform RESTful API.

Project URL: https://roadmap.sh/projects/blogging-platform-api

For DB schema see [main/README.md](main/README.md)
## Development \[Nix\]

```bash
# Clone & cd into project
# Enter development shell
nix develop

# Run dev server
poetry run python blog/manage.py runserver
```

## Routes

| URI                |                              Description                              |
| :----------------- | :-------------------------------------------------------------------: |
| /api/users         |                     Registers a new user. (POST)                      |
| /api/token         |                            Logs in a user.                            |
| /api/token/refresh |                           Refresh a token.                            |
| /api/posts         | Get all todos. paginated with limit (limit is 5 by default) and page. |
| /api/posts         |                       Create a new post. (POST)                       |
| /api/posts/{id}    |                        Update a post. (PATCH)                         |
| /api/posts/{id}    |                        Delete a post. (DELETE)                        |

## Technology stack

- [Django](https://www.djangoproject.com/)
- [Nix](https://nixos.org/nix/)
